#!/usr/bin/env python3
""" Web """

import requests
import redis
from Typing import Callable
from functools import wraps


def count_url_wrapper(method: Callable) -> Callable:
    """ Decorator counting how many times
    a Url is accessed """
    @wraps(method)
    def wrapper(url):
        hashed_url = f'hashed_url:{url}'
        hashed_counter = f'hashed_counter:{url}'

        response_html = method(url)

        store.incr(hashed_counter)
        store.set(hashed_url, response_html)
        store.expire(hashed_url, 10)
        return response_html if not store.get(hashed_url) else store.get(
            hashed_url)
    return wrapper


@count_url_wrapper
def get_page(url: str) -> str:
    """ Get page """
    return requests.get(url).text
