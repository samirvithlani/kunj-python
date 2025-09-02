#{1:1,2:2,3:3,4:4,5:5}

#data= {i:i for i in range(1,6)}
data= {i:i**2 for i in range(1,6)}
print(data)

users = ["ram","shyam","amit","sumit","ajay","raj"]

#userdict ={i:i for i in users}
#userdict ={i:len(i) for i in users}
userdict ={i[0]:i for i in users}
print(userdict)

users = ["ram","shyam","amit","sumit","ajay","raj"]
userdict2 = {i:len(i) for i in users if len(i)>3}
print(userdict2)

users = ["bob","ram","madam","shyam","amit","naman"]
userlabel = {i:"Palindrom" if i == i[::-1] else "Not palindrome" for i in users}
print(userlabel)



