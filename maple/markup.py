#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: markup.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2018-11-06 11:29:39 (CST)
# Last Update: Tuesday 2018-11-20 10:59:46 (CST)
#          By:
# Description:
# ********************************************************************************
from flask import Markup
from bleach import clean
from orgpython import org_to_html
from markdown import markdown

from six.moves import html_entities
from six.moves.html_parser import HTMLParser
import six
import re


class _HTMLWordTruncator(HTMLParser):

    _word_regex = re.compile(r"\w[\w'-]*", re.U)
    _word_prefix_regex = re.compile(r'\w', re.U)
    _singlets = ('br', 'col', 'link', 'base', 'img', 'param', 'area', 'hr',
                 'input')

    class TruncationCompleted(Exception):
        def __init__(self, truncate_at):
            super(_HTMLWordTruncator.TruncationCompleted,
                  self).__init__(truncate_at)
            self.truncate_at = truncate_at

    def __init__(self, max_words):
        # In Python 2, HTMLParser is not a new-style class,
        # hence super() cannot be used.
        try:
            HTMLParser.__init__(self, convert_charrefs=False)
        except TypeError:
            # pre Python 3.3
            HTMLParser.__init__(self)

        self.max_words = max_words
        self.words_found = 0
        self.open_tags = []
        self.last_word_end = None
        self.truncate_at = None

    def feed(self, *args, **kwargs):
        try:
            # With Python 2, super() cannot be used.
            # See the comment for __init__().
            HTMLParser.feed(self, *args, **kwargs)
        except self.TruncationCompleted as exc:
            self.truncate_at = exc.truncate_at
        else:
            self.truncate_at = None

    def getoffset(self):
        line_start = 0
        lineno, line_offset = self.getpos()
        for i in range(lineno - 1):
            line_start = self.rawdata.index('\n', line_start) + 1
        return line_start + line_offset

    def add_word(self, word_end):
        self.words_found += 1
        self.last_word_end = None
        if self.words_found == self.max_words:
            raise self.TruncationCompleted(word_end)

    def add_last_word(self):
        if self.last_word_end is not None:
            self.add_word(self.last_word_end)

    def handle_starttag(self, tag, attrs):
        self.add_last_word()
        if tag not in self._singlets:
            self.open_tags.insert(0, tag)

    def handle_endtag(self, tag):
        self.add_last_word()
        try:
            i = self.open_tags.index(tag)
        except ValueError:
            pass
        else:
            # SGML: An end tag closes, back to the matching start tag,
            # all unclosed intervening start tags with omitted end tags
            del self.open_tags[:i + 1]

    def handle_data(self, data):
        word_end = 0
        offset = self.getoffset()

        while self.words_found < self.max_words:
            match = self._word_regex.search(data, word_end)
            if not match:
                break

            if match.start(0) > 0:
                self.add_last_word()

            word_end = match.end(0)
            self.last_word_end = offset + word_end

        if word_end < len(data):
            self.add_last_word()

    def handle_ref(self, char):
        offset = self.getoffset()
        ref_end = self.rawdata.index(';', offset) + 1

        if self.last_word_end is None:
            if self._word_prefix_regex.match(char):
                self.last_word_end = ref_end
        else:
            if self._word_regex.match(char):
                self.last_word_end = ref_end
            else:
                self.add_last_word()

    def handle_entityref(self, name):
        try:
            codepoint = html_entities.name2codepoint[name]
        except KeyError:
            self.handle_ref('')
        else:
            self.handle_ref(six.unichr(codepoint))

    def handle_charref(self, name):
        if name.startswith('x'):
            codepoint = int(name[1:], 16)
        else:
            codepoint = int(name)
        self.handle_ref(six.unichr(codepoint))


def truncate_html_words(s, num, end_text='…'):
    """Truncates HTML to a certain number of words.

    (not counting tags and comments). Closes opened tags if they were correctly
    closed in the given html. Takes an optional argument of what should be used
    to notify that the string has been truncated, defaulting to ellipsis (…).

    Newlines in the HTML are preserved. (From the django framework).
    """
    length = int(num)
    if length <= 0:
        return ''
    truncator = _HTMLWordTruncator(length)
    truncator.feed(s)
    if truncator.truncate_at is None:
        return s
    out = s[:truncator.truncate_at]
    if end_text:
        out += ' ' + end_text
    # Close any tags still open
    for tag in truncator.open_tags:
        out += '</%s>' % tag
    # Return string
    return out


def markup_clean(text):
    tags = [
        'b', 'i', 'font', 'br', 'div', 'h2', 'blockquote', 'ul', 'li', 'a',
        'p', 'strong', 'span', 'h1', 'pre', 'code', 'img', 'h3', 'h4', 'em',
        'hr', 'ol', 'h5', 'table', 'colgroup', 'col', 'th', 'td', 'tr',
        'tbody', 'thead'
    ]
    attrs = {
        '*': ['style', 'id', 'class'],
        'font': ['color'],
        'a': ['href'],
        'img': ['src', 'alt']
    }
    styles = ['color']
    return clean(text, tags=tags, attributes=attrs, styles=styles)


def markdown_to_html(text, length=None):
    # text = markdown(text, extensions=['codehilite', 'fenced_code'])
    text = markdown(text)
    if length is None:
        return Markup(text)
    return Markup(truncate_html_words(text, length))


def orgmode_to_html(text, length=None):
    text = org_to_html(text)
    if length is None:
        return Markup(text)
    return Markup(truncate_html_words(text, length))
