#!/usr/bin/env python3
"""
Module for web
"""
import requests
import redis
from typing import Callable
from functools import wraps

def count_url_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a particular URL was accessed.
    """
    @wraps(method)
    def wrapper(url: str):
        """
        Wrapper function for decorator
        """
        _redis = redis.Redis()
        _redis.incr(f"count:{url}")
        return method(url)

    return wrapper

@count_url_calls
def get_page(url: str) -> str:
    """
    Get the HTML content of a particular URL and cache the result
    """
    _redis = redis.Redis()
    response = _redis.get(url)
    if response is None:
        response = requests.get(url).text
        _redis.setex(url, 10, response)
    return response
