
import sys
#Input
filename = sys.argv[1]

f_in = open(filename,'r')
f_out = open(filename[:-4]+'_von.txt','w')

seq = f_in.read()

for i in range(0,len(seq)-1,2):
    if(seq[i] == seq[i+1]):
        continue
    elif(seq[i] == '1'):
        f_out.write('1')
    else:
        f_out.write('0')

f_in.close()
f_out.close()



