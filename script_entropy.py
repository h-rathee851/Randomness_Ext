
# coding: utf-8


from entropy_nd_autocorr import *
from collections import Counter
import matplotlib.pyplot as plt
from os import mkdir,path
from datetime import datetime
import sys


# Inputs
filename = sys.argv[1]
entrpy_type = sys.argv[2]

if 'acc_min' in entrpy_type:
    try:
        seq_len = int(sys.argv[3])
    except(IndexError):
        print('Please enter the sequence length')
        quit()


# Get seq from file
seq = []
with open(filename,'r') as f:
    print('Reading File: ' + filename)
    seq = f.read()
    seq = list(map(int,seq))


if 'bit' in entrpy_type:
    # get bits prob dist
    dat = plt.hist(seq)
    probs = [int(dat[0][i])/len(seq) for i in (0,-1)]
    print('Calculating bit entropy')
    
    if('shanon' in entrpy_type):
        print('Shanon \t\t' + str(calc_Shanon(probs)) + '\n')

    elif('collision' in entrpy_type):    
        print('Collision \t\t' + str(calc_Collision(probs)) + '\n')

    elif('minimum' in entrpy_type):
        print('Min \t\t' + str(calc_Min(probs)) +'\n')

    elif('renyi_half' in entrpy_type):
        print('Renyi 1/2 \t\t' + str(calc_Renyi_Half(probs)) +'\n')

    else:
        print('Invalid Entropy Type')
    
    print('Done')



elif 'acc_min' in entrpy_type:
    #gen seq array
    seq_arr = []
    for i in range(0,len(seq)-(seq_len-1),seq_len):
        seq_arr.append(str(seq[i:i+seq_len]))

    if('shanon' in entrpy_type):
        entrpy_func = calc_Shanon

    elif('collision' in entrpy_type):
        entrpy_func = calc_Collision

    elif('minimum' in entrpy_type):
        entrpy_func = calc_Min
    
    elif('renyi_half' in entrpy_type):
        entrpy_func = calc_Renyi_Half

    else:
         print('Invalid Entropy Type')
         exit()

    counts = Counter(seq_arr)
    for key in counts.keys():
        counts[key] = counts[key]/len(seq_arr)


    f_out = open(filename[:-4]+'_acc_min_entrpy.txt','w')
    f_out.write(entrpy_type + '\n\n')
    f_out.write('S_m \t\t Value\n\n')

    print('Calculating Accurate Min Entropy')
    m_ = range(seq_len)
    sm_ = calc_Acc_Min(counts,range(seq_len),entrpy_func)
    for m,s in zip(m_,sm_):
        f_out.write(str(m) +'\t\t' + str(s) + '\n')

    f_out.close()
    print('Done')


else:
    print('Invalid Entropy Type')





