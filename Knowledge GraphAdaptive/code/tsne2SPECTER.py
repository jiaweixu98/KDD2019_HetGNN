# nohup python tsne2SPECTER.py > tsne2SPECTER.log 2>&1 &
# 这tsne的复杂度太高了，所以我们用PCA，希望可以奏效。
from tqdm import tqdm
import numpy as np
from sklearn.decomposition import PCA
import subprocess
import pickle as pk
import pandas as pd
from sklearn import preprocessing
s2id_embeddings = pk.load(open('s2id_embeddings.pkl','rb'))
# pk.dump(s2id_embeddings,open('s2id_embeddings.pkl','wb'))
# print(len(s2id_embeddings))
# s2id_embeddings = {1:[1,2,0],
# 2:[0,1,2],3:[1,2,1],4:[1,2,1],5:[1,2,1],6:[1,2,1],7:[1,2,1],8:[1,2,1],9:[1,2,1],10:[1,2,1]
# }
# print(s2id_embeddings)
X_train = []
X_train_names = []
for x in s2id_embeddings:
        X_train.append(s2id_embeddings[x])
        X_train_names.append(x)

X_train = np.asarray(X_train)
pca_embeddings = {}
# embedding_file = open('pca_embedding_SPECTER.txt', 'w')

# PCA with 150 dimensions.
pca =  PCA(n_components = 128)
X_train = X_train - np.mean(X_train)
X_fit = pca.fit_transform(X_train)
# U1 = pca.components_
# print(X_fit)
for i, x in enumerate(X_train_names):
        pca_embeddings[x] = list(X_fit[i])
        # embedding_file.write("%s\t" % x)
        # for t in pca_embeddings[x]:
        #         embedding_file.write("%f\t" % t)        
        # embedding_file.write("\n")
# print(pca_embeddings)






# all_list = []
# for k,v in s2id_embeddings.items():
#     all_list.append(v)
# all_list_np = np.array(all_list)
# x_tsne = TSNE(n_components=128, random_state=1, method='exact').fit_transform(all_list_np)
# new_s2id_embeddings = {}
# countN = 0
# for k,v in s2id_embeddings.items():
#     new_s2id_embeddings[k] = list(x_tsne[countN])
#     countN += 1
# # print(new_s2id_embeddings)
pk.dump(pca_embeddings,open('pca_embeddings.pkl','wb'))