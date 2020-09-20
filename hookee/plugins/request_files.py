from hookee.pluginmanager import REQUEST_PLUGIN
from hookee.util import PrintUtil

__author__ = "Alex Laird"
__copyright__ = "Copyright 2020, Alex Laird"
__version__ = "1.2.2"

plugin_type = REQUEST_PLUGIN
print_util = None  # type: PrintUtil


def setup(hookee_manager):
    global print_util

    print_util = hookee_manager.print_util


def run(request):
    if request.files:
        print_util.print_dict("Files", dict(request.files), color=print_util.request_color)

    return request
