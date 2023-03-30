# nohup python S2conn_embeddings.py > S2conn_embeddings.log 2>&1 &
# 找到cancer graph 中的local citation relationships
import jsonlines
from tqdm import tqdm
import pickle as pk
s2id_embeddings = pk.load(open('pca_embeddings.pkl','rb'))
# pk.dump(s2id_embeddings,open('s2id_embeddings.pkl','wb'))
for k,v in s2id_embeddings.items():
    print(k,v)
    print(k,len(v))
    break
print(len(s2id_embeddings))