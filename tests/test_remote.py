import unittest
from transmission.remote import TransmissionRemote

class TestTransmissionRemote(unittest.TestCase):
    def setUp(self):
        self.remote = TransmissionRemote()

    def test_parse_torrent_string(self):
        test_torrent =  "1*  100%   399.6 MB  Done         0.0     0.0   43.1  Stopped      The.Aliens.S01E01.PROPER.HDTV.x264-TLA[ettv]"
        output = self.remote.parse_torrent_string(test_torrent)
        self.assertEqual(
            output,
            ['1*', '100%', '399.6 MB', 'Done', '0.0', '0.0', '43.1', 'Stopped', 'The.Aliens.S01E01.PROPER.HDTV.x264-TLA[ettv]']
        )

