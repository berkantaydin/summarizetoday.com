# -*- coding: utf-8 -*-

import lxml.html
import os
import requests
import sys
import time

from datetime import date, timedelta
from slugify import slugify


CONTENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'content', 'posts'))


def run():
    yesterday = (date.today() - timedelta(1)).strftime('%Y-%m-%d')
    page = requests.get("http://www.livescores.com/soccer/%s/" % yesterday)
    if not page:
        return False

    doctree = lxml.html.fromstring(page.text)

    homes = doctree.xpath("/html/body/div/div[5]/div/div[2]/text()")
    aways = doctree.xpath("/html/body/div/div[5]/div/div[4]/text()")
    scores = doctree.xpath("/html/body/div/div[5]/div/div[3]")

    i = 0
    yesterday_for_title = (date.today() - timedelta(1)).strftime('%Y/%m/%d')
    while True:
        try:
            homes[i] = homes[i].strip()
            aways[i] = aways[i].strip()

            try:
                if len(scores[i].text.strip()) > 3:
                    i += 1
                    continue

                scores[i] = scores[i].xpath('a/text()')[0].strip()
            except:
                i += 1
                continue
                pass

            title = "%s vs. %s, %s" % (homes[i], aways[i], yesterday_for_title)
            dt = time.strftime('%Y-%m-%d %H:%M')
            category = "sports"
            tags = "football, football scores, %s, %s" % (homes[i], aways[i])
            content = "%s %s %s" % (homes[i], scores[i], aways[i])
            slug = slugify(title)

            print("Creating: %s" % slug)

            dr = os.path.join(CONTENT_DIR, time.strftime('%Y/%m/%d'))
            full_things_of_file = os.path.join(dr, "%s.md" % slug)

            if os.path.exists(full_things_of_file):
                print('Report already exist.')
                continue

            if not os.path.exists(dr):
                print('Date DIRs created.')
                os.makedirs(dr)

            with open(full_things_of_file, "a") as fx:
                fx.write("Title: %s\n" % title)
                fx.write("Date: %s\n" % dt)
                fx.write("Category: %s\n" % category)
                fx.write("Tags: %s\n" % tags)
                fx.write("Slug: %s\n" % slug)
                fx.write("Author: %s\n" % "carbonero")
                fx.write("\n")
                fx.write("\n")
                fx.write("%s" % content)

            print('Created: %s' % slug)

            i += 1
        except IndexError:
            break
            pass


if __name__ == '__main__':
    run()
    sys.exit(0)
