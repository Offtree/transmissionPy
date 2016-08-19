import unittest
from transmission.torrent import Torrent, TorrentList

class TestTorrentList(unittest.TestCase):
    def setUp(self):
        self.torrent_list = TorrentList([[1, 10],[2, 20],[3, 30]])
    
    def test_creates_torrents(self):
        self.assertEqual(
            len(self.torrent_list.torrents),
            3
        )

    def test_torrents_have_correct_id(self):
        self.assertEqual(
            [t.id for t in self.torrent_list.torrents],
            [1,2,3]
        )

    def test_torrents_have_correct_percent(self):
        self.assertEqual(
            [t.percent for t in self.torrent_list.torrents],
            [10,20,30]
        )

