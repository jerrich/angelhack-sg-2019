#extracting keywords from article using paralleldots API

import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=72fb4129711844f58401b72dae9df2dc')
response = requests.get(url)
##print(response.json())

import paralleldots
from newspaper import Article

#commented out attempt at article extraction
#url = "https://www.economist.com/united-states/2019/05/30/how-should-america-fight-the-next-downturn" #set url from user's current article
#article = Article(url, language="en")
#article.download()
#text = article.text #extract article text
#print(text)
text = "In a statement issued with France and UN chief António Guterres on Saturday, China committed to “update” its climate target “in a manner representing a progression beyond the current one”.  It also vowed to publish a long term decarbonisation strategy by next year."

# Setting your API key
paralleldots.set_api_key( "83JQ4TLL6boJsr6xzHu590WePYyKAWE4KrBTn3pDbGI" )

### Viewing your API key
##paralleldots.get_api_key()

# Get article text
response=paralleldots.keywords(text)
print(response)
for pair in response["keywords"]:
    print("keyword: " + pair["keyword"])
    print("confidence: " + str(pair["confidence_score"]))