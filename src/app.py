import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy as sp
import matplotlib.pyplot as plt

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

user_info = sp.current_user()  # Comprobar pidiendo mi información de usuari de la API si estoy bien conectado a ella.
print(user_info)

info_bad_bunny = sp.artist_top_tracks( '4q3ewBCX7sLwd24euuV69X' , country = 'US' ) # Función para solicitar a la API el top 10 tracks por artista.

top_tracks = info_bad_bunny['tracks'] # Filtro los tracks
track_names = []
track_duration_ms = []
track_popularity = []

for track in top_tracks[:3]: # Bucle que recorra los tresprimeros tracks y me devuelva nombre, etc...
    track_names.append(track['name'])
    track_duration_ms.append(track['duration_ms'])
    track_popularity.append(track['popularity'])

# Convertir la duración de ms a minutos y redondearla a dos decimales.
track_duration_min = [round(duration / 60000, 2) for duration in track_duration_ms]

# Pasar todo a un dataframe
data_frame = pd.DataFrame({ 
    'Names': track_names,
'Duration(min)': track_duration_min,
'Popularity': track_popularity
}, index = ['Nº 1', 'Nº 2', 'Nº 3'])
print(data_frame)


# A partir de aqui creo otro Dataframe pero con el top 10 de las canciones, para que a la hora de analizar la relación estadistica, con su correspondiente scatter plot, la conclusion sea más real.
info_bad_bunny = sp.artist_top_tracks( '4q3ewBCX7sLwd24euuV69X' , country = 'US' )

top_tracks = info_bad_bunny['tracks']
track_names = []
track_duration_ms = []
track_popularity = []

for track in top_tracks:
    track_names.append(track['name'])
    track_duration_ms.append(track['duration_ms'])
    track_popularity.append(track['popularity'])

# Convertir la duración de ms a minutos y redondearla a dos decimales. 
track_duration_min = [round(duration / 60000, 2) for duration in track_duration_ms]

data_frame = pd.DataFrame({
    'Names': track_names,
'Duration(min)': track_duration_min,
'Popularity': track_popularity
})
print(data_frame)


plt.scatter(data_frame['Duration(min)'], data_frame['Popularity'])
plt.xlabel('Duration(min)')
plt.ylabel('Popularity')
plt.title('Popularity vs Duration of Tracks')

# Mostrar los nombres de las canciones en los puntos del gráfico
for i, name in enumerate(data_frame['Names']):
    plt.text(data_frame['Duration(min)'][i], data_frame['Popularity'][i], name, fontsize=8)

plt.show()

print(f'''Al analizar la relación estadística entre la popularidad y la duración de las canciones (He hecho el analisis de las 10 mejores para que 
el resultado sea mas amplio y real) podemos obserbar que el timepo de duracion de una cancion no es relwevante a la hora de obtener o no 
mayor popularidad en la industria musical. Para ello tambien podriamos realizar un hypothesis testing con una cantidad mayor de muestras
y de ahi sacar conclusiones. ''')