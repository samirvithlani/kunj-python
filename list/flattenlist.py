data = [1,[2,[3,[4,[5]]]]]
flatten =[]
copy = data

while copy: #[2,[3,[4,[5]]]] #
    elm = copy.pop(0) #elm =1 2
    print("removing...",elm)
    print("updated copy",copy) #[]
    
    if isinstance(elm,list):#[2, [3, [4, [5]]]]
        copy = elm + copy #append... [2, [3, [4, [5]]]] 
    else:
        flatten.append(elm)  #[1,2]  

print(flatten)        

#[2,4,3,5,7,8,9] k =8

#[2,5]
#[4,3]

#k=8
#[3,5]
