#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Paul Moss"
SITENAME = u":w! Ramblings"
# SITESUBTITLE = u"Writings of a guy on the internet"
SITEURL = 'http://scorpionresponse.com'

GITHUB_URL = 'https://github.com/ScorpionResponse/'
PDF_GENERATOR = False

TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

BYLINE = '&copy; 2012-2017 Paul Moss. All Rights Reserved.'

DEFAULT_PAGINATION = 7

GOOGLE_ANALYTICS = "UA-30458541-1"

# CLEAN_URLS = True

# FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),
#                 ('extra/favicon.ico', 'favicon.ico'),
#                 ('extra/CNAME', 'CNAME'),)

STATIC_PATHS = ['extra', 'images']

EXTRA_PATH_METADATA = {'extra/robots.txt': {'path': 'robots.txt'},
                       'extra/favicon.ico': {'path': 'favicon.ico'},
                       'extra/CNAME': {'path': 'CNAME'}
                       }

DISPLAY_PAGES_ON_MENU = True

ARTICLE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}.html'
