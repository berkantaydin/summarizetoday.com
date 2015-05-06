#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'jarvis'
SITENAME = u'Summarize Today'
SITEURL = ''

# https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3
THEME = 'themes/pelican-bootstrap3'
PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

#Github Domain Settins
STATIC_PATHS = ['images', 'extra/CNAME', 'pages']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'pages/privacypolicy.html': {'path': 'privacypolicy.html'}}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

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