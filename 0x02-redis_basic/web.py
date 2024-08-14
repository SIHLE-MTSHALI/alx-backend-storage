#!/usr/bin/env python3
"""
Implements a simple caching system with tracking
"""

import redis
import requests
from typing import Callable


def get_page(url: str) -> str:
    """
    Get the HTML content of a particular URL and cache the results
    with an expiration time of 10 seconds. Track the number of times
    a particular URL was accessed.
    """
    cache = redis.Redis()
    count_key = f"count:{url}"
    content_key = f"content:{url}"

    # Increment the access count
    cache.incr(count_key)

    # Try to get the cached content
    cached_content = cache.get(content_key)
    if cached_content:
        return cached_content.decode('utf-8')

    # If not in cache, fetch the content
    print(f"Fetching {url}")  # For debugging
    response = requests.get(url)
    content = response.text

    # Cache the content with 10 seconds expiration
    cache.setex(content_key, 10, content)

    return content


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/1000/url/http://example.com/"
    print(get_page(url))
    print(get_page(url))
    print(f"Times {url} was accessed: {redis.Redis().get(f'count:{url}').decode('utf-8')}")
