import datetime


class Submission:
    def __init__(self, gallery_data):
        self.title = gallery_data.title
        self._where = gallery_data.id
        self._when = gallery_data.datetime
    
    @property
    def when(self):
        when = datetime.datetime.fromtimestamp(self._when)
        return when.strftime('%a, %d %b %Y %H:%M:%S %Z')
    
    @property
    def where(self):
        return 'http://imgur.com/gallery/' + self._where
