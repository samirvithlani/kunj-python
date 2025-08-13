no = int(input("enter no :"))
temp = no
temp2=no
#1634 -- 4 -- 4 powe
#153 -- 3  -- cu...
#16587 5 -- 5 pow
digit=0
while temp>0:
    digit+=1
    temp= temp //10
print(digit) 
   
   #0
sum=0
while temp2>0:
    rem = temp2 %10
    sum = sum + rem**digit 
    temp2 = temp2 //10


if no == sum:
    print("armstrong...")    
else:
    print("armstrong not...")    
    


