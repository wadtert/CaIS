import enchant
d = enchant.Dict("en_US")

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
newdata = ''

filename = input("filename : ")

with open(filename,"r", encoding = "utf-8") as file:
    data = file.read()
    for key in range(0,26):
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

            newdata=newdata+i
            
        words = newdata.split()
        for word in words:
            if d.check(word):
                print("=== key :",26-key,"===")
                print(newdata);
            break
        newdata=''

input("\npress ENTER to exit.")
                
                

        

