#!/usr/bin/env python
# fileencoding=utf-8

import json
from HTMLParser import HTMLParser

from bson.objectid import ObjectId

import tornado.escape


type_encoders = [
    (ObjectId, str),
]


def objectid_encoder(obj):
    for encoder in type_encoders:
        if isinstance(obj, encoder[0]):
            return encoder[1](obj)
    raise TypeError("Unknown value '%s' of type %s" % (
        obj, type(obj)))


def json_encode(value, ensure_ascii=False, indent=None):
    # adapted from tornado.escape.json_encode
    return json.dumps(
        value, default=objectid_encoder,
        ensure_ascii=ensure_ascii,
        indent=indent).replace("</", "<\\/")


json_decode = tornado.escape.json_decode


# http://stackoverflow.com/questions/753052/strip-html-from-strings-in-python

class _MLStripper(HTMLParser):

    def __init__(self):
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_html_tags(html):
    s = _MLStripper()
    s.feed(html)
    return s.get_data()
