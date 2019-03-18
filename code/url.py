# This script shows how to modify a URL.

from typing import List, Tuple
import urllib
from urllib.parse import unquote, urlparse, urlunparse, parse_qsl, urlencode

url = 'https://en.wikipedia.org:8080/wiki/Internet?index=0&view=no#Terminology'
print(f"{url}\n")

# Break a URL into components, which are printed below.

url_components: urllib.parse.ParseResult = urlparse(url)

print("URL components:\n")
print(f"* Scheme:   {url_components.scheme}")
print(f"* Netloc:   {url_components.netloc}")
print(f"* Hostname: {url_components.hostname}")
print(f"* Port:     {url_components.port}")
print(f"* Path:     {url_components.path}")
print(f"* Params:   {url_components.params}")
print(f"* Fragment: {url_components.fragment}")
print(f"* Username: {url_components.username}")
print(f"* Password: {url_components.password}")
print(f"* Query:    {url_components.query}\n")

# Get the query parameters.

query_parameters: List[Tuple[str, str]] = parse_qsl(url_components.query)

print("Query parameters:\n")
for name, value in query_parameters:
    print(f'* {name}: {value}')
print('')

# Build a list of query parameters from the dictionary.
# The function urlencode() encodes a dict or sequence of two-element tuples
# into a URL query string.

params = {'p1':10, 'p2': 'this is a param'}
new_query_parameters = urlencode(params)

# Build a URL from its components.
# Note: url_components

new_url_components = list(url_components)
new_url_components[4] = new_query_parameters
new_url: str = urlunparse(tuple(new_url_components))

print(new_url)


