import datetime


class Submission:
    def __init__(self, api_v3_data):
        self.title = api_v3_data['title']
        self._where = api_v3_data['id']
        self._when = api_v3_data['datetime']
    
    @property
    def when(self):
        when = datetime.datetime.fromtimestamp(self._when)
        return when.strftime('%a, %d %b %Y %H:%M:%S %Z')
    
    @property
    def where(self):
        return 'http://imgur.com/gallery/' + self._where
