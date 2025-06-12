from math import *

encount = dict()
keys = 0
finsize = 0
enthropy = float(0)

filename = str(input("filename.txt: "))

with open (filename,"r+") as file:
    for line in file:
        for i in line:
            
            if i == '\n':
                continue
            if encount.get(i,0) == 0:
                encount.update({i:1})
                keys = keys + 1
            else:
                encount[i] = encount.get(i)+1
            finsize = finsize + 1

print("file has",keys,"unique symbols, total of",finsize,"entries")

for i in encount:
    px = float(encount.get(i))/finsize
    print(i,"is",format(px*100,'.2f'),"% of all text")
    enthropy = enthropy + (px * log2(px))

print("enthropy: ",abs(enthropy),"\n")
input("press ENTER to exit...")
