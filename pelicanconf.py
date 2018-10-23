#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Michael Fryar'
SITENAME = 'Michael Fryar'
SITEDESCRIPTION = 'Learning to use new tools. Trying to be useful.'
SITESUBTITLE = 'Learning to use new tools. Trying to be useful.'
SITEURL = 'https://mefryar.github.io'

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
SOCIAL = (
    ('github', 'https://github.com/mefryar'),
    ('linkedin', 'https://linkedin.com/in/fryar')
)

THEME = 'theme'

SIDEBAR_DISPLAY = ['categories', 'tags', 'social']

STATIC_PATHS = ['images', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
