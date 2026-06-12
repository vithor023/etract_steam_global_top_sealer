# %%
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
# %%
df = pd.read_csv('../data/raw/preprocessed/date_preprocessed.csv')
df.head()
# %%

k = 10
scores = []
for i in range(2,k):
    score_total = {}
    kmeans = KMeans(n_clusters=i,random_state=42)
    kmeans.fit(df)
    score_total['k'] = i
    score_total['inertia'] = kmeans.inertia_
    score_total['silhoutte'] = silhouette_score(df, kmeans.predict(df))
    scores.append(score_total)

# %%
df_score_cluster = pd.DataFrame(scores)
df_score_cluster

# %%
plt.figure(figsize=(10,6))
plt.plot(df_score_cluster['k'],df_score_cluster['inertia'],marker='o')
plt.title('Grafico do cutuvelo para indicar mellhor "k" ')
plt.xlabel('numero de clusters (k)')
plt.ylabel('Inertia')
plt.grid(True)
plt.show()

print('Inertia é uma metrica que indica a somatoria da distancia euclidiana de cada ponto com relação ao seu centroide.')
print('Um Bom k esta onde ha um subito descrecimo da inertia, seguido por uma descida suave(o cotovelo)')
print('De acordo com o grafico e o dataframe, o melhor k é o 5')
# %%
df