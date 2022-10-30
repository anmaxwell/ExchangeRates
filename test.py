# Imports
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

import json
import os
from datetime import datetime

# Check if the directory is there to write the output file else create it
path = 'headlines'
filename = 'test_'+str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))
dirpath = os.path.join(path, filename + '.json')

headline_vectors = ['test1', 'test2']

if not os.path.exists(path):
    os.makedirs(path) 
  
with open(dirpath, 'w') as outfile:
    json.dump(headline_vectors, outfile)