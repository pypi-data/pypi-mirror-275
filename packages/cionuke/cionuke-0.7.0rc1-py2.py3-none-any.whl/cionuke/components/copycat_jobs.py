import nuke
import pathlib

import cionuke.copycat_poller

THREAD_POOL = {}

class ThreadTracker:
    '''
    Data structure to keep track of all the components that need to be 
    modified when a thread is started or stopped.
    '''

    def __init__(self, jid, thread, button, status_label):

        self.jid = jid
        self.button = button
        self.thread = thread
        self.status_label = status_label

def polling_updated(jid, *args, **kwargs):
    '''
    Everything to update when a thread is started or stopped.
    '''

    global THREAD_POOL

    if jid in THREAD_POOL and THREAD_POOL[jid].thread:

        THREAD_POOL[jid].thread.stop()
        THREAD_POOL[jid].thread = None
        THREAD_POOL[jid].button.setLabel("Start Polling")
        print ("Thread stopped for {}".format(jid))

    else:
        THREAD_POOL[jid].thread = start_thread(jid, submitter=THREAD_POOL[jid].button.node())
        THREAD_POOL[jid].button.setText("Stop Polling")

def build(submitter, jid):
    """
    Build custom UI knob and a string knob for storage.

    The storage knob contains JSON.
    """

    global THREAD_POOL

    copycat_tab = submitter.knob("CopyCat jobs")

    if copycat_tab is None:
        copycat_tab = nuke.Tab_Knob("CopyCat jobs")
        submitter.addKnob(copycat_tab)

    jid_knob = nuke.String_Knob("cio_cc_jid_{}".format(jid), "Job ID")
    submitter.addKnob(jid_knob)
    jid_knob.setValue(jid)

    status_knob = nuke.String_Knob("cio_cc_status_{}".format(jid), "Status")
    status_knob.clearFlag(nuke.STARTLINE)
    submitter.addKnob(status_knob)
    status_knob.setValue("RUNNING")

    polling_checkbox = nuke.PyScript_Knob("cio_cc_polling_{}".format(jid), "Stop Polling", "import cionuke.components.copycat_jobs as c; c.polling_updated('{}')".format(jid))
    polling_checkbox.clearFlag(nuke.STARTLINE)
    submitter.addKnob(polling_checkbox)

    new_thread = start_thread(jid, submitter)
    THREAD_POOL[jid] = ThreadTracker(jid=jid, thread=new_thread, button=polling_checkbox, status_label=status_knob)

def start_thread(jid, submitter):
    '''
    Start a new polling thread
    '''

    data_path = pathlib.Path(submitter.input(0).knob("dataDirectory").getValue())
    new_thread = cionuke.copycat_poller.CopyCatPoller(jid, data_path)
    new_thread.start()
    return new_thread

def update_thread_ui(jid, job_status):
    '''
    Update the CopyCat jobs tab with a new status
    '''

    global THREAD_POOL
    THREAD_POOL[jid].status_label.setValue(job_status.upper())