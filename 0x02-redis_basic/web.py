#!/usr/bin/env python3
"""
Web cache and tracker module.
"""
import redis
import requests
from typing import Callable

redis_instance = redis.Redis()

def get_page(url: str) -> str:
    """Fetch a page and cache the result in Redis."""
    count_key = f"count:{url}"
    redis_instance.incr(count_key)

    cached_page = redis_instance.get(url)
    if cached_page:
        return cached_page.decode('utf-8')

    response = requests.get(url)
    redis_instance.setex(url, 10, response.text)

    return response.text
