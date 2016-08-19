class Torrent(object):
    def __init__(
        self,
        id=None,
        percent=None,
        size=None,
        status=None,
        upload=None,
        download=None,
        something=None,
        is_downloading=None,
        name=None
    ):
        self.id = id
        self.percent = percent
        self.size = size
        self.status = status
        self.upload = upload
        self.download = download
        self.something = something
        self.is_downloading = is_downloading
        self.name = name

class TorrentList(object):

    torrents = []

    def __init__(self, torrent_list=[]):
        self.torrents = [
            Torrent(*tor)
        for tor in torrent_list ]
