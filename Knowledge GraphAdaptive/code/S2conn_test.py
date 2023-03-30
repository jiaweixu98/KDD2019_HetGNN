# nohup python S2conn_embeddings.py > S2conn_embeddings.log 2>&1 &
import jsonlines
from tqdm import tqdm
import pickle as pk
# only 234k have refs in this graph
s2id_citing_cited = pk.load(open('s2id_citing_cited.pkl','rb'))
# print(len(s2id_citing_cited))
# for k,v in s2id_citing_cited.items():
#     print(type(k),type(v))
#     break
s2id_pcount = {}
pid_s2id = pk.load(open('pid_s2id.pkl','rb'))
pid_pcount = pk.load(open('PID_trans_Pcount.pkl','rb'))

for k,v in pid_s2id.items():
    s2id_pcount[str(v)] = pid_pcount[k]
print('s2p finished')

paper_c2citation_c = {}
for k,v in s2id_citing_cited.items():
    # k sid; V sid；下面转化为数字符号
    paper_c2citation_c[s2id_pcount[k]] = list(map(lambda x: s2id_pcount[x],v))


p_p_citation_list = open("../data/academic/p_p_citation_list.txt", "w")
import operator
sorted_paper_c2citation_c = sorted(paper_c2citation_c.items(),key=operator.itemgetter(0))
for k, v in  dict(sorted_paper_c2citation_c).items():
    p_p_citation_list.write(str(k) + ":")
    for tt in range(len(v)-1):
        p_p_citation_list.write(str(v[tt]) + ",")
    p_p_citation_list.write(str(v[-1]))
    p_p_citation_list.write("\n")
p_p_citation_list.close()