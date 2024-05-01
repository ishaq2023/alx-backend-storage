#!/usr/bin/env python3

import requests
import time

# Dictionary to store cached pages and their access counts
cache = {}

def cache_page(func):
    def wrapper(url):
        # Check if the URL is in the cache
        if url in cache:
            # Check if the cached entry is still valid (within 10 seconds)
            if time.time() - cache[url]['timestamp'] < 10:
                cache[url]['count'] += 1  # Increment access count
                return cache[url]['content']

        # If not in cache or expired, call the original function
        content = func(url)

        # Update cache with new content and access count
        cache[url] = {
            'content': content,
            'timestamp': time.time(),
            'count': 1
        }
        return content
    return wrapper

@cache_page
def get_page(url: str) -> str:
    return requests.get(url).text

# Test the function
url = "http://slowwly.robertomurray.co.uk/delay/1000/url/http://www.example.com"
print(get_page(url))
print(get_page(url))
