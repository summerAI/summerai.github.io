#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import yaml
from slugify import slugify
import os
import sys
from amazonproduct import API

api = API(locale='us')


def make_asin(str_or_int):
    result = str(str_or_int)
    return "0" * (9 - len(result)) + result


def scrape(items):
    result_set = {}

    result = api.item_lookup(*items)
    for item in result.Items.Item:
        if ":" in item.ItemAttributes.Title.text:
            title, tagline = item.ItemAttributes.Title.text.split(":", 1)
        else:
            title, tagline = item.ItemAttributes.Title.text, ""
        result_set[item.ASIN.text] = {
            b'url': item.DetailPageURL.text,
            b'slug': slug(title),
            b'title': title.strip().encode('utf-8'),
            b'tagline': tagline.strip().encode('utf-8'),
            b'author': item.ItemAttributes.Author.text,
        }

    # Get Images
    result = api.item_lookup(*items, ResponseGroup="Images")
    for item in result.Items.Item:
        if hasattr(item, 'MediumImage'):
            result_set[item.ASIN.text][b'cover'] = str(item.MediumImage.URL)
            result_set[item.ASIN.text][b'aspect_ratio'] = 100. * item.MediumImage.Height / item.MediumImage.Width

    return result_set


def slug(title):
    return slugify(title.split(":", 1)[0]).encode('utf-8')

if __name__ == "__main__":
    force = sys.argv[-1] == "--force"
    with open("bookshelf.yaml") as f:
        shelves = yaml.load(f)
        for shelf in shelves:
            print("Generating shelf '{}'".format(shelf))
            asins = map(make_asin, shelves[shelf].keys())
            for asin, item in scrape(asins).items():
                item[b'shelf'] = shelf
                path = "pages/books/{}.md".format(item['slug'])
                if force or not os.path.exists(path):
                    print("Adding '{}.md'".format(item['slug']))
                    with open(path, 'w') as f:
                        yaml.dump(item, f, default_flow_style=False, encoding='utf-8', allow_unicode=True)
