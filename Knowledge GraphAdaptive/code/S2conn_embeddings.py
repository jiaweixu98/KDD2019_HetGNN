# nohup python S2conn_embeddings.py > S2conn_embeddings.log 2>&1 &
# 找到cancer graph 中的local citation relationships
import jsonlines
from tqdm import tqdm
import pickle as pk
# local pmid set
# PID_set = pk.load(open('PID_set.pkl','rb'))
# pmid-S2ID, 有近1000个没有匹配上，所以去掉，我们更新一下。
# pid_s2id = pk.load(open('pid_s2id.pkl','rb'))
# matched_s2id_set = set()
# for k,v in pid_s2id.items():
#     # print(type(k),type(v))
#     matched_s2id_set.add(str(v))
#     # break
# pk.dump(matched_s2id_set,open('matched_s2id_set.pkl','wb'))
matched_s2id_set = pk.load(open('matched_s2id_set.pkl','rb'))
matched_s2id_list = []
for i in matched_s2id_set:
    matched_s2id_list.append(int(i))

matched_s2id_list = set(matched_s2id_list)
print(len(matched_s2id_list))
# print(len(matched_s2id_set))
# matched_PID_set = pk.load(open('matched_PID_set.pkl','rb'))
# matched_PID_set = pk.load(open('matched_PID_set.pkl','rb'))
# pk.dump(set(pid_s2id.keys()),open('matched_PID_set.pkl','wb'))
# matched_PID_set = pk.load(open('matched_PID_set.pkl','rb'))
# print(len(matched_PID_set))
# print(type(matched_s2id_set.pop()))
# print(len(PID_set))
# print(len(pid_s2id))
# pid_s2id
s2id_embeddings = {}
for i in tqdm(range(30)):
    with jsonlines.open('/home/dell/kd_paper_data/data/SemanticScholar-20220913/full(v20220913)/embeddings/%d.jsonl'%i, mode='r') as reader:
        # item即为每一行的数据
        for item in reader:
            if item['corpusid'] in matched_s2id_list:
                s2id_embeddings[item['corpusid']] = eval(item['vector'])
# print(s2id_citing_cited)
# print(s2id_embeddings)
pk.dump(s2id_embeddings,open('s2id_embeddings.pkl','wb'))