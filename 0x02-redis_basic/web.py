#!/usr/bin/env python3
"""
Implements an expiring web cache and tracker
"""

import redis
import requests
from functools import wraps
from typing import Callable


r = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """Decorator to count how many times a request has been made"""
    @wraps(method)
    def wrapper(url):
        """Wrapper function"""
        r.incr(f"count:{url}")
        cached_html = r.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        r.setex(f"cached:{url}", 10, html)
        return html
    return wrapper


@count_requests
def get_page(url: str) -> str:
    """
    Uses the requests module to obtain the HTML
    content of a particular URL and returns it.
    """
    resp = requests.get(url)
    return resp.text


if __name__ == "__main__":
    url = 'http://slowwly.robertomurray.co.uk'
    print(get_page(url))
    print(get_page(url))
    print(get_page(url))
    print(r.get(f"count:{url}"))
