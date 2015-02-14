# RSSTranslator - Build RSS feeds from REST APIs #

We all use quite a few sites that we would like to receive updates from. There
 exists a way of viewing feeds from any site that supports it in one handy
 location. This way is called RSS (there also exists Atom, which is similar -
 if I understand correctly, just a slightly different file format). However,
 a lot of sites don't seem to like to create RSS feeds for us, so we are
 constantly having to re-open many sites frequently to check for updates. If
 only there were a better way, right?

Well, as it turns out, many of these sites _do_ provide a REST API that does
 list updates. While they don't all conform to a standard like RSS does, an
 API does make it possible to generate an RSS feed.

Enter RSSTranslator. This web app is designed to generate RSS feeds from REST
 APIs. It currently supports:

|     Feed description      |                   Endpoint                    |
| ------------------------- | --------------------------------------------- |
| Imgur gallery submissions | /feed/imgur/gallery-subs/{imgur_username}.rss |

The format for feeds is `/feed/{app_name}/{feed_type}/{feed_descriptor}.rss`,
 where:

- `{app_name}`: The name of the app that provides the standard service. Some
    examples could be `imgur`, `twitter`, or `youtube`.
- `{feed_type}`: A short name describing the point of this feed. Just in case
    we need multiple feed types for each app.
- `{feed_descriptor}`: Uniquely identifies the actual RSS feed. This is usually
    the username of someone (e.g. the app username or whoever we are following).

You can currently find the app on Heroku at `http://rss-translator.herokuapp.com`.
 Be aware that it is on the lowest hosting level, so it can't handle high
 traffic. There is currently no index page.


## Running ##

1. Get API keys
1. Create a virtual environment (recommended)
    - `pip install virtualenv`
    - `virtualenv env`
        - You may need to specify `-p python3`
2. Activate virtualenv (only if you did step 1)
    - `. env/bin/activate`
3. Install dependencies
    - `pip install -r requirements.txt`
4. Run development server locally
    - `python dev_debug_server.py`
5. Run production server locally (requires Heroku toolbelt)
    - `foreman start`


## Roadmap ##

- [x] Create a dynamic RSS feed of recent submitted posts using Imgur API
- [ ] Genericize to provide extensibility to create more feed types
- [ ] Add a couple more feed types
    - [ ] Twitter 'following' feeds
    - [ ] Maybe YouTube subscriptions feeds?
- [ ] Create a simple way to view said feeds in the browser (i.e. a UI)
- [ ] Provide an API to easily add simple feeds
