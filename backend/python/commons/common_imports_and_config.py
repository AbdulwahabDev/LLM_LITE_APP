import os 
import sys
import numpy as np
import json
import pandas as pd 
import json  
from tqdm import tqdm 
from pathlib import Path
 
from commons.Enums.DeviceEnum import *

current_file_path = Path(__file__)
base_path = str(current_file_path.parent.parent) 

QdrantClient_URL = os.environ.get('QdrantClient_URL')
NeuralSearcher_model_path = os.environ.get('NeuralSearcher_model_path')
collection_name=os.environ.get('collection_name')
