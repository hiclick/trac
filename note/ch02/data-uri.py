# -*- coding:utf-8 -*-
__author__ = 'Christen'


data_uri = open("google.png", "rb").read().encode("base64").replace("\n", "")
img_tag = '<img alt="google" src="data:image/png;base64,{0}">'.format(data_uri)

print img_tag