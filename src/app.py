import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy as sp

# load the .env file variables
load_dotenv()

from spotipy.oauth2 import SpotifyOAuth  # Este es el método recomendado para conectarse a la API de Spotify utilizando autenticación OAuth

# Leer las variables CLIENT_ID y CLIENT_SECRET desde el archivo .env
my_client_id = os.environ.get("CLIENT_ID")
my_client_secret = os.environ.get("CLIENT_SECRET")
my_redirect_URI = "http://localhost:8000"  # Aqui pongo la localhost que agregué en el panel de desarrolladores de Spotify y que he tenido que poner a funcionar desde mi servidor.

# Crear una instancia de SpotifyOAuth para la autenticación
sp = sp.Spotify(auth_manager=SpotifyOAuth(client_id = my_client_id,
                                               client_secret = my_client_secret,
                                               redirect_uri = my_redirect_URI,
                                               scope=["user-library-read"]))

user_info = sp.current_user()  # Verificar que se conecta y me decuelve mi info
print(user_info)