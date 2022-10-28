# Imports
import os
from datetime import datetime
from newsapi import NewsApiClient

# Initialise 
newsapi = NewsApiClient(api_key='5a1d2319cf6b4e06bd29beb4651f66f9')

# Get the top UK headlines for the day
top_uk_headlines = newsapi.get_top_headlines(category=('business' or 'technology'),
                                          language='en',
                                          country='gb')

# Create a list of the latest headlines to convert to vectors
headlines = []
for item in top_uk_headlines['articles']:
    headlines.append(item['title'])

# Convert headlines to vectors

# Check if the directory is there to write the output file else create it
path = '/ukheadlines'
curr_timestamp = int(datetime.timestamp(datetime.now()))

def createheadlinefile():
    with open('ukheadlines/ukheadlines_{curr_timestamp}.json', 'w') as outfile:
        json.dump(headlines, outfile)

if os.path.exists(path):
    with open('ukheadlines/ukheadlines_{curr_timestamp}.json', 'w') as outfile:
        json.dump(headlines, outfile)

else:
    os.makedirs(path) 
    with open('ukheadlines/ukheadlines_{curr_timestamp}.json', 'w') as outfile:
        json.dump(headlines, outfile)
    print('oh dear')