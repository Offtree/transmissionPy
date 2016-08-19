"""
This module contains everything that calls command line calls.
"""


class Command(object):
    base_cmd = ['transmission-remote']
    args = []

    def run_command(self):
        return subprocess.check_output(self.base_cmd + self.args, stderr=subprocess.STDOUT)


class ListCommand(Command):
    args = ['-l']


class RemoveCommand(Command):
    def __init__(self, torrent_id):
        self.args = ['--remove={0}'.format(torrent_id)]

