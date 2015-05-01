import os
import summarize
import sys
import time

from bs4 import BeautifulSoup as bs
from slugify import slugify

CONTENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'content', 'posts'))


def run(url):
    data = summarize.summarize_page(url)

    title = data.title.split(' - Al Jazeera')[0]
    dt = time.strftime('%Y-%m-%d %H:%M')
    category = "news"
    tags = "bbc"
    url = data.url
    content = "\n\n".join(data.summaries)
    slug = slugify(title)

    print("Creating: %s" % slug)

    dr = time.strftime('%Y/%m/%d')
    full_things_of_file = os.path.join(CONTENT_DIR, dr, "%s.md" % slug)

    if os.path.exists(full_things_of_file):
        print('Report already exist.')
        return False

    if not os.path.exists(dr):
        print('Date DIRs created.')
        os.makedirs(dr)

    with open(full_things_of_file, "a") as fx:
        fx.write("Title: %s\n" % title)
        fx.write("Date: %s\n" % dt)
        fx.write("Category: %s\n" % category)
        fx.write("Tags: %s\n" % tags)
        fx.write("Slug: %s\n" % slug)
        fx.write("Src: %s\n" % url)
        fx.write("Author: %s\n" % "jarvis")
        fx.write("\n")
        fx.write("\n")
        fx.write("%s" % content)

    print('Created: %s' % slug)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        run(url=sys.argv[0])
        sys.exit(0)

    print('Usage %s.py <URL>' % __file__)
    sys.exit(1)