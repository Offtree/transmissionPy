import re

from command import ListCommand
from torrent import TorrentList
TORRENT_SPLIT_REGEX = '\s+'

class TransmissionRemote(object):

    def get_torrents(self):
        list_output = ListCommand().run_command()
        torrent_arr = list_output.split('\n')
        return TorrentList([
            self.parse_torrent_string(arr)
        for arr in torrent_arr[1, -1]])

    def parse_torrent_string(self, torrent_string):
        def handle_units(arr):
            units = arr.pop(3)
            arr[2] = "{0} {1}".format(arr[2], units)
            return arr

        torrent_arr = re.split(TORRENT_SPLIT_REGEX, torrent_string)
        torrent_arr = handle_units(torrent_arr)
        return torrent_arr
