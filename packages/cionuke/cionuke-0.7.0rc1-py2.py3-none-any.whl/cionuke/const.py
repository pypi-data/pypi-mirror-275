import os

NOT_CONNECTED = "-                 NOT CONNECTED                 -"
INVALID = "INVALID - Please press Connect"

FEATURE_DEV = os.environ.get("CIO_FEATURE_DEV", False)

VERSION = "dev.999"
PLUGIN_DIR = os.path.dirname(__file__)

CONDUCTOR_COMMAND_PATH = os.path.join(os.path.dirname(PLUGIN_DIR), "bin", "conductor")

COPY_CAT_MODES = {'single_instance': 'Single Instance',
                  'distributed_local': 'Distributed (local Main)',
                  'distributed_remote':  'Distributed (remote Main)'}

try:
    with open(os.path.join(PLUGIN_DIR, "VERSION")) as version_file:
        VERSION = version_file.read().strip()
except BaseException:
    pass
