#!/usr/bin/env python3
from flask import Flask, render_template
import datetime

from submission import Submission

app = Flask(__name__)


@app.route('/api/feeds/<iun>.rss', methods=['GET'])
def index(iun):
    now = datetime.datetime.now()
    return render_template('userfeed.jinja2',
                           iun=iun,
                           now=now.strftime('%a, %d %b %Y %H:%M:%S %Z'),
                           subs=[Submission({
                               'title': "My most recent drawing. Spent over 100 hours. I'm pretty proud of it.",
                               'id': 'OUHDm',
                               'datetime': 1349051625
                           })])


if __name__ == '__main__':
    app.run(debug=True)

