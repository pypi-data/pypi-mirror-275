import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify APIの認証情報
client_id = '7f10c6e741ea4f25b46fb86e20a8ca16'
client_secret = '0eae52d162fd4ef4a00a2a93564ca17f'

# 認証
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))

# CSVファイルを読み込む
df = pd.read_csv('data/top_50_tracks_features.csv')

# 曲名とアーティスト名を取得して追加
track_names = []
artist_names = []

for track_id in df['id']:
    track = sp.track(track_id)
    track_names.append(track['name'])
    artist_names.append(track['artists'][0]['name'])

df['track_name'] = track_names
df['artist_name'] = artist_names

# CSVファイルに保存
df.to_csv('data/top_50_tracks_features2.csv', index=False)
