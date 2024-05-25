# 必要なライブラリをインポート
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Spotify APIの認証情報を設定
client_id = '7f10c6e741ea4f25b46fb86e20a8ca16'
client_secret = '0eae52d162fd4ef4a00a2a93564ca17f'

# Spotipyオブジェクトを作成
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# JAPAN週間ランキングの上位50曲のプレイリストID
playlist_id = '37i9dQZEVXbKXQ4mDTEBXq'

# プレイリスト内の曲情報を取得
playlist_tracks = sp.playlist_tracks(playlist_id)

# 上位50曲の特徴量を取得
top_50_features = []
for track in playlist_tracks['items']:
    # 曲情報を取得
    track_id = track['track']['id']
    track_name = track['track']['name']
    artist_name = track['track']['artists'][0]['name']
    
    # 曲の特徴量を取得
    features = sp.audio_features(track_id)
    
    # 特徴量が取得できた場合はリストに追加
    if features:
        features[0]['track_name'] = track_name
        features[0]['artist_name'] = artist_name
        top_50_features.append(features[0])

# 取得した特徴量を保存（例えばCSVファイルに保存する）
df = pd.DataFrame(top_50_features)
df.to_csv('top_50_tracks_features.csv', index=False)
