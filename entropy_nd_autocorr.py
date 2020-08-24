from math import log,sqrt
from collections import Counter
import numpy as np

def calc_Shanon(probs):
    return sum(map(lambda x : -x*log(x,2),probs))

def calc_Collision(probs):
    return -log(sum([x**2 for x in probs]) ,2)

def calc_Min(probs):
#     return min(map(lambda x: -log(x,2), probs))
    return -log(max(probs),2)

def calc_Renyi_Half(probs):
    return 2*log(sum([sqrt(x) for x in probs]) ,2)




def calc_Acc_Min(counts, m_, entrpy_func):
    
    coll_val_up = entrpy_func(counts.values())
    entrpy_ = []
    
    for m in reversed(m_): 
        counts_ls = dict()
        
        for c in counts:
            a = c[:-4]+']'
            if a in counts_ls:
                continue
             
            
            counts_ls[a] = counts[c]
    
            if(c[-2] == '0'):
                c = c[:-2]+'1]'
            else:
                c = c[:-2]+'0]'
     
            if c in counts:
#         print(c)
                counts_ls[a] += counts[c]

        coll_val =   entrpy_func(counts_ls.values())
        entrpy_.append(coll_val_up - coll_val)
        coll_val_up = coll_val
        counts = counts_ls
        print('{0:.2f}% left'.format(((m)/len(m_))*100))
    
#     print(list(counts_ls.keys())[0], " ", counts_ls[list(counts_ls.keys())[0]])
    entrpy_.reverse()
    return entrpy_


