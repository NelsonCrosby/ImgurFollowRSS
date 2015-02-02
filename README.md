# ImgurFollowRSS - Create RSS feeds of Imgur users #

If someone in particular sparks your interest, this thing allows you to create
 a feed for them so you can stay updated in your favourite RSS reader.

I'm not in a position to host it myself right now, but maybe I will manage it
 someday.


## Dependencies ##

Depends on:

- [Flask](http://flask.pocoo.org)
- [imgurpython](https://github.com/Imgur/imgurpython)


## Roadmap ##

- [x] Create a dynamic RSS feed of recent submitted posts using Imgur API
- [ ] Create a simple way to view said feeds in the browser (i.e. a UI)

At some point I should probably find a way to host it.


## Non-goals ##

- Any kind of "discovery" system. There is a reason that this is missing from the main Imgur system - it conflicts with the way the community is grown and how it works (or something to that effect). Some, however, have an interesting 'series' type thing going on (e.g. [CaptRawesome](http://imgur.com/user/CaptRawesome/submitted)) that would be _really_ good to be able to subscribe to.
