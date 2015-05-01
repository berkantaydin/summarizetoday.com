import summarize
import sys
import time

from bs4 import BeautifulSoup as bs
from slugify import slugify


url = sys.argv[1]

data = summarize.summarize_page(url)

title = data.title.split(' - BBC News')[0]
dt = time.strftime('%Y-%m-%d %H:%M')
category = "bbc news"
tags = "bbc news"
url = data.url
content = "\n\n".join(data.summaries)
slug = slugify(title)

print(slug)

with open("/tmp/%s" % slug, "a") as fx:
    fx.write("Title: %s\n" % title)
    fx.write("Date: %s\n" % dt)
    fx.write("Category: %s\n" % category)
    fx.write("Tags: %s\n" % tags)
    fx.write("Slug: %s\n" % slug)
    fx.write("Author: %s\n" % "jarvis")
    fx.write("\n")
    fx.write("\n")
    fx.write("%s" % content)

