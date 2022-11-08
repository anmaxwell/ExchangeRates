# Imports
import json
import requests

import os
from datetime import datetime

url = 'https://api.apilayer.com/exchangerates_data/latest?base=GBP&symbols=USD'

payload = {}
headers= {
  'apikey': 'iVhclvMkTD98sD5kpwCGrD75B5sxuAjK'
}

response = requests.request('GET', url, headers=headers, data = payload)

status_code = response.status_code
result = json.loads(response.text)

# Check if the directory is there to write the output file else create it
path = 'rates'
filename = 'rates_'+str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))
dirpath = os.path.join(path, filename + '.json')

if not os.path.exists(path):
    os.makedirs(path) 
  
with open(dirpath, 'w') as outfile:
    json.dump(result, outfile)