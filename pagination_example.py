from serpapi import GoogleSearch

parameter = {
  "q": "coca cola after:2009-10-05 before:2022-12-04",
  "tbm": "nws",
  "api_key": "API_KEY",
  "start": 0,
  "num": 100,# page size
  "end": 500, #  total number of pages

}

# as proof of concept
# urls collects
urls = []

search = GoogleSearch(parameter)
result = search.get_dict()

while True:
    if "news_results" in result:
        for news in result["news_results"]:
         #   print(news["title"])
            urls.append(news['link'])
        if "serpapi_pagination" in result:
            print('I am a new page', parameter['start'])
            if "next" in result["serpapi_pagination"]:
                parameter['start'] += parameter['num']
                search = GoogleSearch(parameter) #  this line was missing in your code
                result = search.get_dict()
            else:
                break
        else:
            break
    else:
        break


# note: the exact number if variable depending on the search engine backend
if len(urls) == (parameter['end'] - parameter['start']):
    print("all search results count match!")
if len(urls) == len(set(urls)):
    print("all search results are unique!")


print("Length of URLs", len(urls))
