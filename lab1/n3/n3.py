upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'

filename = input("filename : ")

with open(filename,"r", encoding = "utf-8") as file:
    data = file.read()
    for key in range(0,26):
        print("=== key:",26-key,"====")
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
                    
            print(i, end='')
        print("\n")
input("Press ENTER to exit...")
                

        

