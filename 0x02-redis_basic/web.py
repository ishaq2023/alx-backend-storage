#!/usr/bin/env python3
"""
Module for web
"""
import requests
import redis

def get_page(url: str) -> str:
    """
    Retrieve the HTML content of a URL and cache the result with an expiration time of 10 seconds.

    Args:
        url (str): The URL of the page to retrieve.

    Returns:
        str: The HTML content of the page.
    """
    # Initialize Redis client
    redis_client = redis.Redis()

    # Increment the count for the URL
    count_key = f"count:{url}"
    redis_client.incr(count_key)

    # Retrieve cached page content if available
    cached_content = redis_client.get(url)
    if cached_content:
        return cached_content.decode('utf-8')

    # Fetch the page content
    response = requests.get(url)
    page_content = response.text

    # Cache the page content with an expiration time of 10 seconds
    redis_client.setex(url, 10, page_content)

    return page_content

if __name__ == "__main__":
    # Example usage
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.google.com"
    print(get_page(url))  # This might take some time to retrieve due to the delay
