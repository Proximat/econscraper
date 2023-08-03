# otherfile.py
from categories import publishers

def is_publisher(url):
    return url in publishers

# testing
test_url = "https://www.sciencedirect.com"
print(is_publisher(test_url))  # prints True if test_url is in the list, False otherwise
