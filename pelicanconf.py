#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Paul Moss'
SITENAME = ':w! Ramblings'
SITESUBTITLE = 'Hazy visions through a crack in the world'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/scorpionrespons'),
          ('github', 'https://github.com/ScorpionResponse'),
          ('envelope', 'mailto:moss.paul@gmail.com'))

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'theme'

STATIC_PATHS = ['extra', 'images']

EXTRA_PATH_METADATA = {'extra/robots.txt': {'path': 'robots.txt'},
                       'extra/favicon.ico': {'path': 'favicon.ico'},
                       'extra/CNAME': {'path': 'CNAME'}}

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

FOOTER_INCLUDE = 'footer_custom.html'

SHOW_FULL_ARTICLE = True

PLUGINS = ['plugins.embed_tweet']

DISPLAY_PAGES_ON_MENU = True
