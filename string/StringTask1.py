data = "hi this is india"
title = ""
for i in range(0,len(data)):
    if i==0:
        c = data[0].upper()
        print(c)
        title+=c
    else:
        if " " in data[i-1]:
            c = data[i].upper()
            print(c)
            title+=c
            #print(title)
        else:
           # print(data[i])
            title+=data[i]    

print(title)            
                
    