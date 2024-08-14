#!/usr/bin/env python3
"""Caching web pages with Redis"""

import redis
import requests
from functools import wraps
from typing import Callable


def count_url_access(method: Callable) -> Callable:
    """Decorator to track URL access count"""

    @wraps(method)
    def wrapper(url):
        """Wrapper function to increment access count"""
        r = redis.Redis()
        r.incr(f"count:{url}")
        return method(url)

    return wrapper


def cache_page_content(method: Callable) -> Callable:
    """Decorator to cache web page content for 10 seconds"""

    @wraps(method)
    def wrapper(url):
        """Wrapper function to check/store cache"""
        r = redis.Redis()
        cached_page = r.get(url)
        if cached_page:
            return cached_page.decode('utf-8')

        result = method(url)
        r.setex(url, 10, result)
        return result

    return wrapper


@count_url_access
@cache_page_content
def get_page(url: str) -> str:
    """Fetches a web page and returns its content"""
    response = requests.get(url)
    response.raise_for_status()
    return response.text
