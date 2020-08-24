
import sys

#Inputs
f_in = open(sys.argv[1],'r')
rows = 1792
columns = 2048
seed_buff = 1000

try:
    rows = int(sys.argv[2])
    columns = int(sys.argv[3])
    seed_buff = int(sys.argv[4])

except(IndexError):
    pass


seed_len = rows*columns
f_out = open('seed_seq.txt','w')

seq = f_in.read()

i = 0
while(i <= len(seq) - seed_len):
    f_out.write(seq[i:i+seed_len]+'\n')
    i += seed_len + seed_buff
    
f_in.close()
f_out.close()


f_in = open('seed_seq.txt','r')
f_out = open('seed.txt','w')

dat = list(map(lambda x: list(map(int,x[:-1])),f_in.readlines()))
seed = [0]*len(dat[0])

for i in range(len(dat[0])):
    for m in dat:
        seed[i] ^= m[i]

f_out.write(''.join(map(str,seed)))

f_in.close()
f_out.close()

f_in = open('seed.txt','r')
f_out = open('seed_matrix.txt','w')

seed = f_in.read()

for i in range(0,len(seed)-columns+1,columns):
    f_out.write(seed[i:i+columns]+'\n')

f_in.close()
f_out.close()
