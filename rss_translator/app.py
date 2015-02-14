import datetime

import flask as fl
from flask import g
from imgurpython import ImgurClient

from .submission import Submission
from .feed_loader import FeedLoader
from . import feed_types

app = fl.Flask(__name__)
app.config.from_envvar('RSS_TRANSLATOR_CONFIG')
app.config['client'] = ImgurClient(app.config['IMGUR_CLIENT_ID'],
                                   app.config['IMGUR_CLIENT_SECRET'])

#

@app.before_request
def _before_api_request():
    g.client = app.config['client']


for feed_type in FeedLoader.FEED_TYPES:
    inst = feed_type(app)
    route = '/feeds/{}/{}/<feed_descriptor>.rss'.format(inst.app_name,
                                                        inst.feed_type)

    @app.route(route, methods=['GET'])
    def get_feed(feed_descriptor):
        inst.load_feed_info(feed_descriptor, app, g)
        feed_info = inst.get_feed_info(feed_descriptor)
        feed_data = inst.get_feed_data(g)
        return fl.render_template(
            'feed.j2',
            feed_info=feed_info,
            feed_data=feed_data
        )


@app.route('/api/feeds/<iun>.rss', methods=['GET'])
def index(iun):
    now = datetime.datetime.now()
    submitted = g.client.get_account_submissions(iun)
    return fl.render_template(
        'userfeed.jinja2',
        iun=iun,
        now=now.strftime('%a, %d %b %Y %H:%M:%S %Z'),
        subs=[Submission(entry) for entry in submitted]
    )
