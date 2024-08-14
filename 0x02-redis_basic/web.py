#!/usr/bin/env python3
"""
Implements an expiring web cache and tracker
"""

import redis
import requests
from functools import wraps
from typing import Callable


def create_redis_client():
    """Create and return a Redis client"""
    return redis.Redis()


def cache_and_track(func: Callable) -> Callable:
    """
    Decorator to cache the result of get_page with expiration
    and track the number of calls
    """
    @wraps(func)
    def wrapper(url: str) -> str:
        redis_client = create_redis_client()
        redis_client.incr(f"count:{url}")
        
        result = redis_client.get(f"cached:{url}")
        if result:
            return result.decode('utf-8')
        
        result = func(url)
        redis_client.setex(f"cached:{url}", 10, result)
        return result
    
    return wrapper


@cache_and_track
def get_page(url: str) -> str:
    """
    Get the HTML content of a particular URL and return it
    """
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    page_content = get_page(url)
    print(page_content)
    print(get_page(url))
    print(get_page(url))
