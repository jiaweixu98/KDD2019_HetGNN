import pickle as pk
from tqdm import tqdm
print('hello world')
Pcount_trans_PID = pk.load(open('Pcount_trans_PID.pkl','rb'))
Acount_trans_AID = pk.load(open('Acount_trans_AID.pkl','rb'))
Bcount_trans_BID = pk.load(open('Bcount_trans_BID.pkl','rb'))
f = open("../data/academic/48_node_embedding_re.txt", "r")
fa = open("../data/academic/0320author_48_node_embedding.txt", "w")
fp = open("../data/academic/0320paper_48_node_embedding.txt", "w")
fb = open("../data/academic/0320entity_48_node_embedding.txt", "w")
for line in tqdm(f):
    line = line.strip().split(' ')
    if line[0][0] == 'a':
        fa.write(Acount_trans_AID[int(line[0][1:])])
        for i in line[1:]:
            fa.write(' '+i)
        fa.write('\n')
        continue
    if line[0][0] == 'v':
        fb.write(Bcount_trans_BID[int(line[0][1:])])
        for i in line[1:]:
            fb.write(' '+i)
        fb.write('\n')
        continue
    if line[0][0] == 'p':
        fp.write(Pcount_trans_PID[int(line[0][1:])])
        for i in line[1:]:
            fp.write(' '+i)
        fp.write('\n')
f.close()
fa.close()
fp.close()
fb.close()