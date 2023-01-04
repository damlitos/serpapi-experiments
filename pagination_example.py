from serpapi import GoogleSearch

parameter = {
  "q": "coca cola after:2009-10-05 before:2022-12-04",
  "tbm": "nws",
  "api_key": "XXXXXX",
  "start": 0,
  "num": 80, # page size
  "end": 240, #  total number of results

}

# as proof of concept
# urls collects
urls = []

search = GoogleSearch(parameter)
result = search.get_dict()

while True:
    if "news_results" in result:

        print('I am a new page', parameter['start'])
        counter = 0
        for news in result["news_results"]:
         #   print(news["title"])
            counter += 1
            urls.append(news['link'])

        print(counter)
        if "serpapi_pagination" in result:

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
