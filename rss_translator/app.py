import datetime

import flask as fl
from flask import g

from .feed_loader import FeedLoader
# noinspection PyUnresolvedReferences
# Loads feed types
from . import feed_types

app = fl.Flask(__name__)
app.config.from_envvar('RSS_TRANSLATOR_CONFIG')


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
