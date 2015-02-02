#!/usr/bin/env python3
import datetime

from flask import Flask, render_template, g
from imgurpython import ImgurClient

from submission import Submission

app = Flask(__name__)
app.config.from_pyfile('_privatecfg.py')
app.config['client'] = ImgurClient(app.config['CLIENT_ID'],
                                   app.config['CLIENT_SECRET'])


@app.before_request
def _before_api_request():
    g.client = app.config['client']


@app.route('/api/feeds/<iun>.rss', methods=['GET'])
def index(iun):
    now = datetime.datetime.now()
    submitted = g.client.get_account_submissions(iun)
    return render_template(
        'userfeed.jinja2',
        iun=iun,
        now=now.strftime('%a, %d %b %Y %H:%M:%S %Z'),
        subs=[Submission(entry) for entry in submitted]
    )


if __name__ == '__main__':
    app.run(debug=True)

