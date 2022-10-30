# Imports
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

import json
import os
from datetime import datetime
from newsapi import NewsApiClient

# Initialise 
newsapi = NewsApiClient(api_key='5a1d2319cf6b4e06bd29beb4651f66f9')

# Get the top UK headlines for the day
top_uk_headlines = newsapi.get_top_headlines(category=('business' or 'technology'),
                                          language='en',
                                          country='gb')

#Loading pretrained model
module_url = 'https://tfhub.dev/google/universal-sentence-encoder/4'
model = hub.load(module_url)

#function to create embedding vectors
def embed(input):
    return model(input)

# Create a list of the latest headlines converted to vectors
headlines = []
for item in top_uk_headlines['articles']:
    headline_txt = item['title']

    #create vectors from questions
    vector_USE = embed(headline_txt)
    print('vector', vector_USE)

    headlines.append(vector_USE)

# Check if the directory is there to write the output file else create it
path = 'ukheadlines'
filename = 'ukheadlines_'+str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))
dirpath = os.path.join(path, filename + '.json')

if not os.path.exists(path):
    os.makedirs(path) 
  
print('created: ',filename)
with open(dirpath, 'w') as outfile:
    json.dump(headlines, outfile)