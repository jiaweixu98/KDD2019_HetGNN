# nohup S2conn.py > S2conn.log 2>&1 &
# 把PMID和S2ID联系起来，只要cancer里的
import jsonlines
from tqdm import tqdm
import pickle as pk

# Pcount_trans_PID = pk.load(open('Pcount_trans_PID.pkl','rb'))
# print(len(Pcount_trans_PID.values()))
# pk.dump(set(Pcount_trans_PID.values()),open('PID_set.pkl','wb'))
PID_set = pk.load(open('PID_set.pkl','rb'))
pid_s2id = {}
for i in tqdm(range(30)):
    with jsonlines.open('/home/dell/kd_paper_data/data/SemanticScholar-20220913/full(v20220913)/papers/paperP%d.jsonl'%i, mode='r') as reader:
        # item即为每一行的数据
        for item in reader:
            if item['externalids']['PubMed'] != None and item['externalids']['PubMed'] in PID_set:
                pid_s2id[item['externalids']['PubMed']] = item['corpusid']
                # print(item['corpusid'],item['externalids']['PubMed'],item['title'])
                # break
            break
        break
# pk.dump(pid_s2id,open('pid_s2id.pkl','wb'))