import hashlib
import csv
import string
from typing import OrderedDict
import collections

def hash_password_hack(input_file_name, output_file_name):
    a = OrderedDict()
    b = OrderedDict()
    l =[]
    with open('input_file_name.csv','r') as fin:
        reader =csv.reader(fin)
        for row in reader:
            name = row[0]
            l.append(name)
            a[name]=row[1]
        for i in range (1000,10000):
            s =str(i)
            result=hashlib.sha256(s.encode())
            b[result.hexdigest()]= s
        for j in range(len(l)):
             if b[a[l[j]]] != {}:
                 a[l[j]]=b[a[l[j]]]
        with open('output_file_name.csv','w') as fout:                                      
         writer = csv.writer(fout,delimiter=",", lineterminator='\n')
         for i in  range (len(l)):
             writer.writerow([l[i],a[l[i]]]) 
hash_password_hack('a','b')