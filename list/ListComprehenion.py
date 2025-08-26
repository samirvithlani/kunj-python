# data =[]

# for i in range(1,6):
#     data.append(i)

# print(data)    

data =[i for i in range(1,6)]
print(data)

users = ["ram","shyam","amit","sumut","ajay"]

upperUser = [i.upper() for i in users]
print(upperUser)


#10
sales = [100,200,300,400,500]
salesprofit = [i+(i*0.2) for i in sales]
print(salesprofit)


#if
users = ["ram","shyam","amit","sumit","ajay"]

userwithlen = [i for i in users if len(i)>3]
print(userwithlen)


numbers = [1,2,3,4,5,6,7,8,9,109,191,191,1923,3,44,3]

evenno = [i for i in numbers if  i%2==0]
print(evenno)


names = ["raj","bob","parth","madam","naman","jaya"]

palindromes = [i for i in names if i == i[::-1]]
print(palindromes)


#names = ["raj","bob","parth","madam","naman","jaya"]

palindromeslabels = ["Yes" if i == i[::-1] else "NO" for i in names]
print(palindromeslabels)

numbers = [1,2,3,4,5,6,7,8,9,109,191,191,1923,3,44,3]
numberslabel = ["even" if i%2==0 else "odd" for i in numbers]
print(numberslabel)

numbers = [1,2,3,4,5,6,7,8,9,109,0,191,191,1923,-3,44,3]
#posneg = ["POS" if i >0 else "NEG" for i in numbers]
posneg = ["POS" if i >0 else ("zero" if i ==0 else "NEG") for i in numbers]
print(posneg)

