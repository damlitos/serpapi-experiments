
import os
from serpapi import GoogleSearch

start = 0
end = 500
page_size = 100

# basic search parameters
parameter = {
    #"q": "kudo insurance after:2022-10-05 before:2022-12-04",
    "q": "coca cola after:2009-10-05 before:2022-12-05",
    "tbm": "nws",
    "api_key": "API_KEY",
    # optional pagination parameter
    #  the pagination method can take argument directly
    "start": start,
    "end": end,
    "num": page_size
}

# as proof of concept
# urls collects
urls = []

# initialize a search
search = GoogleSearch(parameter)

# create a python generator using parameter
pages = search.pagination()
# or set custom parameter
pages = search.pagination(start, end, page_size)

# fetch one search result per iteration
# using a basic python for loop
# which invokes python iterator under the hood.
for page in pages:
    print(f"Current page: {page['serpapi_pagination']['current']}")
    for news_result in page["news_results"]:
        #print(f"Title: {news_result['title']}\nLink: {news_result['link']}\n")
        urls.append(news_result['link'])

# check if the total number pages is as expected
# note: the exact number if variable depending on the search engine backend
if len(urls) == (end - start):
    print("all search results count match!")
if len(urls) == len(set(urls)):
    print("all search results are unique!")

print(len(urls))
