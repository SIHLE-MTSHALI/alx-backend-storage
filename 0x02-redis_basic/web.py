#!/usr/bin/env python3
"""
Web cache and tracker module
"""
import redis
import requests
import time
from functools import wraps
from typing import Callable


redis_client = redis.Redis()


def url_access_count(method: Callable) -> Callable:
    """
    Decorator to track the number of times a URL is accessed
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """Wrapper function"""
        redis_client.incr(f"count:{url}")
        cached_response = redis_client.get(f"cached:{url}")
        if cached_response:
            return cached_response.decode('utf-8')
        response = method(url)
        redis_client.setex(f"cached:{url}", 10, response)
        return response
    return wrapper


@url_access_count
def get_page(url: str) -> str:
    """
    Get the HTML content of a URL and cache the result
    """
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    url = ("http://slowwly.robertomurray.co.uk"
           "/delay/1000/url/http://www.example.com")
    page_content = get_page(url)
    print(page_content)
    print(f"Count: {redis_client.get(f'count:{url}').decode('utf-8')}")

    # Wait for cache to expire
    time.sleep(11)

    page_content = get_page(url)
    print(page_content)
    print(f"Count: {redis_client.get(f'count:{url}').decode('utf-8')}")
