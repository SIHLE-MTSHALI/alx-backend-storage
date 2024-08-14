#!/usr/bin/env python3
"""
Implements a simple caching system
"""

import redis
import requests
import functools


def get_page(url: str) -> str:
    """
    Returns the content of a URL after caching the request's response 
    with an expiration time of 10 seconds
    """
    redis_client = redis.Redis()
    count_key = f'count:{url}'
    content_key = f'content:{url}'

    # Increment the access count
    redis_client.incr(count_key)

    # Check if content is cached
    cached_content = redis_client.get(content_key)
    if cached_content:
        return cached_content.decode('utf-8')

    # If not cached, fetch the content
    response = requests.get(url)
    content = response.text

    # Cache the content with 10 seconds expiration
    redis_client.setex(content_key, 10, content)

    return content


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))
    print(get_page(url))
