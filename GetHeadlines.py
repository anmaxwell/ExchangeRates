# Imports
from newsapi import NewsApiClient

# Initialise 
newsapi = NewsApiClient(api_key='')

# Get the top UK headlines for the day
top_uk_headlines = newsapi.get_top_headlines(category=('business' or 'technology'),
                                          language='en',
                                          country='gb')

for item in top_uk_headlines['articles']:
    print(item['title'])