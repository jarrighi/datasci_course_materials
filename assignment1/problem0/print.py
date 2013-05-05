import urllib
import json

n = 1
for page in range(10):
  response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft&page=%s" % (page + 1))
  #print type(json.load(response)
  response_results = json.load(response)

  for i in range(15):
    print n,
    print ": ",
    print response_results["results"][i]["text"]
    n = n + 1