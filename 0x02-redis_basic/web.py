#!/usr/bin/env python3
"""Caching web pages with Redis"""

import redis
import requests
from functools import wraps
from typing import Callable
from urllib.parse import quote


def count_url_access(method: Callable) -> Callable:
    """Decorator to track URL access count."""

    @wraps(method)
    def wrapper(url):
        r = redis.Redis()
        encoded_url = quote(url, safe='')
        r.incr(f"count:{encoded_url}")
        return method(url)

    return wrapper


def cache_page_content(method: Callable) -> Callable:
    """Decorator to cache web page content for 10 seconds."""

    @wraps(method)
    def wrapper(url):
        r = redis.Redis()
        encoded_url = quote(url, safe='')
        cached_page = r.get(encoded_url)
        if cached_page:
            return cached_page.decode("utf-8")

        result = method(url)
        r.setex(encoded_url, 10, result)
        return result

    return wrapper


@count_url_access
@cache_page_content
def get_page(url: str) -> str:
    """Fetches a web page and returns its content."""
    response = requests.get(url)
    response.raise_for_status()
    return response.text
