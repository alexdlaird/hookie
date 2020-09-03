import json
import sys
import xml.dom.minidom

import click

__author__ = "Alex Laird"
__copyright__ = "Copyright 2020, Alex Laird"
__version__ = "0.0.7"

BLUEPRINT_PLUGIN = "blueprint"
REQUEST_PLUGIN = "request"
RESPONSE_PLUGIN = "response"

VALID_PLUGIN_TYPES = [BLUEPRINT_PLUGIN, REQUEST_PLUGIN, RESPONSE_PLUGIN]
REQUIRED_PLUGINS = ["blueprint_default"]


class PrintUtil:
    def __init__(self, config):
        self.config = config

    @property
    def console_width(self):
        return self.config.get("console_width")

    def print_config_update(self, msg):
        click.secho("\n--> {}\n".format(msg), fg="green")

    def print_open_header(self, title, delimiter="-", fg="green"):
        width = int((self.console_width - len(title)) / 2)

        click.echo("")
        click.secho("{}{}{}".format(delimiter * width, title, delimiter * width), fg=fg, bold=True)
        click.echo("")

    def print_close_header(self, delimiter="-", fg="green"):
        click.secho(delimiter * self.console_width, fg=fg, bold=True)

    def print_dict(self, title, data, fg="green"):
        click.secho("{}: {}".format(title, json.dumps(data, indent=4)), fg=fg)

    def print_xml(self, title, data, fg="green"):
        click.secho("{}: {}".format(title, xml.dom.minidom.parseString(data).toprettyxml()), fg=fg)


def is_python_3():
    return sys.version_info >= (3, 0)
