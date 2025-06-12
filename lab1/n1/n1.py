upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'

key = int(input("\n==============key:"))

outname = 'o'+str(key)+'.txt'
out = open(outname,"w+",encoding="utf-8")

with open("IN.txt","r",encoding = "utf-8") as file:
    data = file.read()
    for i in data:
        
        if upper.find(i)>=0:
            if upper.index(i)+key > 25:
                i = upper[upper.index(i)+key-26]
            else:
                i = upper[upper.index(i)+key]
        if lower.find(i)>=0:
            if lower.index(i)+key > 25:
                i = lower[lower.index(i)+key-26]
            else:
                i = lower[lower.index(i)+key]
                
        out.write(i)
        
out.close()
print(outname,"created")
input("\npress ENTER to exit")
