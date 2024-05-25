import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# CSVファイルからデータを読み込む
df = pd.read_csv('top_50_tracks_features.csv')

# コサイン類似度を計算するための特徴量を選択
features = df[['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']]

# ユーザーが選択した曲の特徴量（例えば、1行目を選択）
selected_features = features.iloc[0].values.reshape(1, -1)

# データセット内の各曲とのコサイン類似度を計算
similarities = cosine_similarity(selected_features, features)

# コサイン類似度が最も高い曲のインデックスを取得
most_similar_index = similarities.argsort()[0][-2]

# 推薦された曲を表示
recommended_track = df.iloc[most_similar_index]
print("Recommended Track:")
print(recommended_track)