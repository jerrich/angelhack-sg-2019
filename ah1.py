#example using "Apple" and "Jobs" as keywords from articles since July 5th

import requests
import operator

#generate list of articles sorted by popularity
urlPop = ('https://newsapi.org/v2/everything?'
          'q=Apple;Jobs&'
   	      'from=2019-07-05&'
	      'sortBy=popularity&'
          'apiKey=72fb4129711844f58401b72dae9df2dc')
responsePop = requests.get(urlPop)
responsePop = responsePop.json()

#generate list of articles sorted by relevancy of keywords
urlRel = ('https://newsapi.org/v2/everything?'
          'q=Apple;Jobs&'
   	      'from=2019-07-05&'
	      'sortBy=relevancy&'
          'apiKey=72fb4129711844f58401b72dae9df2dc')
responseRel = requests.get(urlRel)
responseRel = responseRel.json()

#generate list of scores assigning relevancy twice the weight of popularity
scores = {}
for article in range(0, len(responseRel["articles"])):
	scores[responseRel["articles"][article]["url"]] = 2 * (len(responseRel["articles"]) - article)
for article in range(0, len(responsePop["articles"])):
	if responsePop["articles"][article]["url"] in scores:
		scores[responsePop["articles"][article]["url"]] += (len(responseRel["articles"]) - article)

#pick top 10 scores to send off
sorted_scores = sorted(scores.items(), key=lambda kv: kv[1])
top10 = sorted_scores[(len(sorted_scores) - 10):]
final = dict((url,score) for url,score in top10)

#test by printing
print(final)