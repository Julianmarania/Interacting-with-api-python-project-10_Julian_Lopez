import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy as sp

# load the .env file variables
load_dotenv()

# Leer las variables CLIENT_ID y CLIENT_SECRET desde el archivo .env
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

