upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
keys = []
key_current = 0

codedname = input("filename : ")

clear = open("IN.txt","r", encoding = "utf-8")
coded = open(codedname,"r", encoding = "utf-8")

clearline = clear.read();
codedline = coded.read();

for i in range(0, len(clearline)):
    flag = False

    if upper.find(clearline[i])>=0 and upper.find(codedline[i])>=0:
        key_current = upper.find(codedline[i])-upper.find(clearline[i])
        flag = True
            
    elif lower.find(clearline[i])>=0 and lower.find(codedline[i])>=0:
        key_current = lower.find(codedline[i])-lower.find(clearline[i])
        flag = True

    if key_current < 0: key_current = key_current + 26
    keys.append(key_current)

print("Unique keys:",set(keys))

clear.close()
coded.close()        

input("\npress ENTER to exit.")

        
        
