from ..feed_loader import FeedLoader


class ImgurGallerySubmissionsLoader(FeedLoader):
    def __init__(self, app):
        super().__init__(app, 'https://api.imgur.com/3')
        self.app_name = 'imgur'
        self.feed_type = 'gallery-subs'
        self.translators = {
            'title': 'title',
            'where': 'id',
            'when': 'datetime',
            'desc': ''
        }
    
    def get_feed_info(self, feed_descriptor):
        return {
            'title': feed_descriptor + "'s submissions",
            'desc': 'Imgur gallery submissions for ' + feed_descriptor,
            'link': 'http://imgur.com/user/' + feed_descriptor + '/submitted/'
        }
    
    def get_request_headers(self, app):
        return {
            'Authorization': 'Client-ID ' + app.config['IMGUR_CLIENT_ID']
        }
    
    def get_endpoint(self, feed_descriptor):
        return '/account/' + feed_descriptor + '/submissions'
    
    def extract_data(self, data):
        return data['data']
    
    def get_where(self, item):
        return 'http://imgur.com/gallery/' + super().get_where(item)

FeedLoader.FEED_TYPES.append(ImgurGallerySubmissionsLoader)
