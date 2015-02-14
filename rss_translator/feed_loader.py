from urllib.request import Request, urlopen
import json
import datetime


class FeedLoader:
    FEED_TYPES = []
    
    def __init__(self, app, hostname):
        self._hostname = hostname
        self.app_name = self.feed_type = ''
        self.translators = {
            'title': 'title',
            'where': 'url',
            'when': 'posted',
            'desc': 'desc'
        }
    
    def get_feed_info(self, feed_descriptor):
        return {
            'title': '<< blank feed >>',
            'desc': '<< blank feed >>',
            'link': 'about:blank'
        }
    
    def get_request_headers(self, app):
        return {}
    
    def get_endpoint(self, feed_descriptor):
        return '/api'
    
    def load_feed_info(self, feed_descriptor, app, g):
        response = urlopen(Request(
            url=self._hostname + self.get_endpoint(feed_descriptor),
            headers=self.get_request_headers(app)
        ))
        result = json.loads(response.read().decode())
        g.feed_info = result
    
    def extract_data(self, data):
        return data
    
    def get_feed_data(self, g):
        return [{
            'title': self.get_title(item),
            'where': self.get_where(item),
            'when': self.get_when(item),
            'desc': self.get_desc(item)
        } for item in self.extract_data(g.feed_info)]

    def get_title(self, item):
        api_attr_name = self.translators['title']
        if api_attr_name:
            return item[api_attr_name]
        else:
            return ''

    def get_where(self, item):
        api_attr_name = self.translators['where']
        if api_attr_name:
            return item[api_attr_name]
        else:
            return ''

    def get_when(self, item):
        api_attr_name = self.translators['when']
        if api_attr_name:
            return datetime.datetime.fromtimestamp(item[api_attr_name])
        else:
            return datetime.datetime.now()
    
    def get_desc(self, item):
        api_attr_name = self.translators['desc']
        if api_attr_name:
            return item[api_attr_name]
        else:
            return ''
