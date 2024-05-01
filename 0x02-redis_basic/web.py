#!/usr/bin/env python3
import requests
import time

def get_page(url: str) -> str:
    """
    Retrieves the HTML content of a given URL and caches it with an expiration time of 10 seconds.
    """
    # Check if the URL has been accessed before
    cache_key = f"count:{url}"
    cached_content = get_cached_content(cache_key)

    if cached_content:
        return cached_content

    # Fetch the page content using requests
    try:
        response = requests.get(url)
        page_content = response.text

        # Cache the content with an expiration time of 10 seconds
        cache_content(cache_key, page_content, expiration=10)
        return page_content
    except requests.RequestException:
        return "Error: Unable to retrieve page content."

def get_cached_content(key: str) -> str:
    """
    Retrieves cached content if available.
    """
    # Implement your caching logic here (e.g., using Redis, memcached, etc.)
    # For demonstration purposes, let's assume we have a dictionary as our cache.
    return cache.get(key, "")

def cache_content(key: str, content: str, expiration: int):
    """
    Caches the content with the specified expiration time.
    """
    # Implement your caching logic here (e.g., update the dictionary cache).
    # For demonstration purposes, we'll just update the dictionary.
    cache[key] = content
    time.sleep(expiration)  # Simulate expiration delay

# Example usage
if __name__ == "__main__":
    url_to_fetch = "http://slowwly.robertomurray.co.uk/delay/1000/url/https://www.example.com"
    page_content = get_page(url_to_fetch)
    print(page_content)
