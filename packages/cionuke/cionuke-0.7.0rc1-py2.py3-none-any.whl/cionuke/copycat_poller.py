import datetime
import json
import pathlib
import requests.exceptions
import threading
import time

import nuke

import ciocore.api_client

class CopyCatPoller(threading.Thread):

    POLLING_INTERVAL = 15.0

    def __init__(self, jid, data_path, *args, **kwargs):

        super(CopyCatPoller, self).__init__(*args, **kwargs)
        self.jid = jid
        self.tid = None
        self.master_tid = None
        self.job_status = None
        self._cancel = False

        timestamp = datetime.datetime.now().strftime("%y%m%d")
        self._summary_file = pathlib.Path(data_path, "Training_{}_{:0>6}.summary".format(timestamp, jid))

    def stop(self):
        '''
        Gracefully stop the thread. Must be called from outside the thread.
        '''
        self._cancel = True
        self.join(timeout=5.0)

    def run(self, *args, **kwargs):
        '''
        Executed within the new thread.

        Polls the given jid for status and logs.

        Attempts to find to find the main CopyCat task based on log output.

        Once the main task has been identified, the log is parsed to place data
        in the CopyCat summary file which populates the progress graph in Nuke.
        '''

        loops = 0
        last_line = 0

        import cionuke.components.copycat_jobs
        client = ciocore.api_client.ApiClient()

        self.tid = None
        last_step = 0

        while not self._cancel:

            loops += 1

            uri = 'api/v1/client/jobs/{}'.format(self.jid)
            result = client.make_request(verb="GET", uri_path=uri, use_api_key=True)
            job_data = json.loads(result[0])['data']
            self.job_status = job_data["status"]
            print ("Got job status({}): {}".format(self.jid, self.job_status))

            nuke.executeInMainThread(cionuke.components.copycat_jobs.update_thread_ui, (self.jid, self.job_status))

            if self.job_status in ("success", "downloaded", "preempted", "killed", "failed"):
                print("Job {} has completed: {}. Stopping thread".format(self.jid, self.job_status))
                time.sleep(15) # Give time to grab the end of the log. Another 15s at the end of the loop
                self._cancel = True
                nuke.executeInMainThread(cionuke.components.copycat_jobs.THREAD_POOL[self.jid].button.setLabel, ("Start Polling",))


            if self.job_status in ("running", "success", "downloaded", "preempted", "killed", "failed"):

                if self.tid is None:

                    # An optimization here would be to sort tasks by time started as the first task
                    # started is most likely to be the main node
                    for task in range(0, int(job_data['tasks'])):
                        tid = "{:0>3}".format(task)
                        uri = 'get_log_file?job={}&task={}&num_lines%5B%5D=0'.format(self.jid, tid)
                        
                        try:
                            result = client.make_request(verb="GET", uri_path=uri, use_api_key=True)
                        
                        except requests.exceptions.HTTPError as errMsg:
                            print("No log exists for {}-{} yet: {}".format(self.jid, tid, str(errMsg)))
                            continue
                        
                        data = json.loads(result[0])

                        for log_line in data['logs'][0]['log']:

                            if "Writing IP into lock file." in log_line:
                                print("Task {} is the primary node.".format(tid))
                                self.tid = tid
                                # Once we know the primary node, wait a bit to ensure the log
                                # lines will be in the correct order
                                time.sleep(30)

                            elif "Reading IP address of primary render node" in log_line:
                                print("Task {} is a worker.".format(tid))
                                break

                if self.tid:

                    uri = 'get_log_file?job={}&task={}&num_lines%5B%5D={}'.format(self.jid, self.tid, last_line)
                    result = client.make_request(verb="GET", uri_path=uri, use_api_key=True)
                    data = json.loads(result[0])

                    # Debug
                    # print ("Got lines {}-{} of log.".format(last_line, len(data['logs'][0]['log'])+last_line))

                    # with self._summary_file.with_name("{}.log".format(self.jid)).open(mode='a') as fh:
                    #     fh.write("{}-------{}\n".format(last_line, len(data['logs'][0]['log'])+last_line))
                    #     fh.writelines(l+"\n" for l in data['logs'][0]['log'])

                    # with self._summary_file.with_name("{}.requests.log".format(self.jid)).open(mode='a') as fh:
                    #     fh.write(uri + "\n")
                    #     fh.write(str(result))
                    #     fh.write("\n----------------\n\n")

                    for line_num, log_line in enumerate(data['logs'][0]['log']):

                        if log_line.startswith("[Step:"):
                            step = int(log_line.split("/")[0][6:])
                            loss_value = log_line.split(":")[-1]

                            # If the logs are not being returned in order, stop and make a new request
                            # from the current line
                            if ( #(last_step > 0) and 
                                 (last_step + 10 != step)):
                                print("-------------detected out of order lines (line {})".format(line_num))
                                line_num -= 2
                                break                            

                            with open(self._summary_file, 'a') as fh:
                                fh.write("{},{},".format(step, loss_value))
                                last_step = step
  
                    last_line = line_num + last_line + 1

            time.sleep(self.POLLING_INTERVAL)