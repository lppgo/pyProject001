#!/usr/bin/env python
# coding: utf-8
import logging


logging.basicConfig(level=logging.INFO)


def cal(m, n):
    if n == 0:
        # raise ValueError('Illegal value: %d' % n)
        logging.info('Illegal value: %d' % n)
    return m * n


try:
    r = cal(6, 0)
    print(r)
except Exception as e:
    print(e)
