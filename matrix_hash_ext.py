import sys

#Inputs
try:
    file_name = sys.argv[1]
except(IndexError):
    print('Please enter the path of the file containing raw bits')
    exit()

try:
    matrix_file = sys.argv[2]
except(IndexError):
    print('Please enter the path of the file containing the seed matrix')
    exit()

f_rand = open(file_name,'r')
f_matrix = open(matrix_file,'r')
f_out = open(file_name[:-4]+'_matrix.txt','w')
rand_dat = f_rand.read()
ext_matrix = [list(map(int,r[:-1])) for r in f_matrix.readlines()]
f_rand.close()
f_matrix.close()

col = len(ext_matrix[0])
for i in range(0,len(rand_dat)-col+1,col):
    for row in ext_matrix:
        ext_bit = 0
        for m in range(i,i+col):
            ext_bit ^= (int(rand_dat[m])&row[m-i])
        f_out.write(str(ext_bit))
        
f_out.close()
