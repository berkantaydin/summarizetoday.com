import sys

import feedparser
import markdowner_aljazeera

list = ['http://www.aljazeera.com/xml/rss/all.xml', ]


def runner():
    for rss in list:
        feed = feedparser.parse(rss)
        for item in feed['entries']:
            print(item.link)
            markdowner_aljazeera.run(item.link)


if __name__ == '__main__':
    runner()
    sys.exit(0)