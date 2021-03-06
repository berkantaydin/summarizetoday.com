#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'jarvis'
SITENAME = u'Summarize Today'
SITEURL = ''

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3
THEME = 'themes/pelican-bootstrap3'
PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

#Github Domain Settings
STATIC_PATHS = ['images', 'extra/CNAME', 'pages']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = False
CATEGORY_FEED_ATOM = False
TRANSLATION_FEED_ATOM = False
AUTHOR_FEED_ATOM = False
AUTHOR_FEED_RSS = False
TAG_CLOUD_MAX_ITEMS = 20

# Blogroll
LINKS = (('BA', 'http://berkantaydin.com.tr'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/wwwsrc'),
          ('linkedin', 'https://www.linkedin.com/in/berkantaydin'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme Options
GOOGLE_ANALYTICS_UNIVERSAL = 'UA-62525705-1'
GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY = 'auto'
DISQUS_SITENAME = 'summarizetoday'
