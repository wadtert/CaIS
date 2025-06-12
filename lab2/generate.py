from random import *

line = ''
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

otype = int(input("0 - mono\n1 - binary\n2 - digits\n3 - letters\n-->"))
filename = str(input("filename: "))

file = open(filename,"w+")

if otype == 0:
    for lines in range(0,100):
        for digits in range (0,100):
            digit = 7
            line = line + str(digit)
        file.write(line+'\n')
        line = ''

if otype == 1:
    for lines in range(0,100):
        for digits in range (0,100):
            digit = randint(0,1)
            line = line + str(digit)
        file.write(line+'\n')
        line = ''

if otype == 2:
    for lines in range(0,100):
        for digits in range (0,100):
            digit = randint(0,9)
            line = line + str(digit)
        file.write(line+'\n')
        line = ''

if otype == 3:
    for lines in range(0,100):
        for words in range (0,100):
            word = choice(alphabet)
            line = line + str(word)
        file.write(line+'\n')
        line = ''
    
file.close()
input("Done.\nPress ENTER to exit.")
