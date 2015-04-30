#!/usr/bin/env python

from lxml import html
from xml.dom import minidom
from urllib import urlencode, quote
from urllib2 import urlopen, Request, HTTPError
import requests
import sys
import re, json, time
import codecs
import unicodedata

def find_synonyms(word):
    http_headers = {"User-Agent":"Mozilla/4.0 (compatible; MSIE5.5;WindowsNT)"}
    url = 'http://www.wordreference.com/sinonimos/' + quote(word.encode('utf-8'))
    page = Request(url, None, http_headers)
    response = urlopen(page).read()
    tree = html.fromstring(response)
    return [lel.split(' ,') for lel in tree.xpath('//div[@id="article"]/div/ul/li/text()')]


def synonym_tuple(word, output):
    output.write(word + u': ' )
    for i in find_synonyms(word):
        for j in i:
            output.write(j)
        output.write(u', ')
    output.write(u'\n')


"""
Main
"""
words = codecs.open('words.txt','r','utf8')
output = codecs.open('output.txt','w','utf8')

for word in words:
    word = word.strip()
    synonym_tuple(word,output)

words.close()
output.close()
