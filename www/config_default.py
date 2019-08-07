#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations.
'''

__author__ = 'Michael Liao'

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': '20190807mysql',
        'db': 'p_blog'
    },
    'session': {
        'secret': 'p_blog20190807'
    }
}