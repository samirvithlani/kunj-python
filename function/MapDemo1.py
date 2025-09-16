#map
users = ["ram","shyam","amit","sumit","kunal"]

#userUpper = [i.upper() for i in users]

upperUser = map(lambda x:x.upper(),users)
print(list(upperUser))


marks = [10,12,13,14,15]
marks2 = map(lambda x:x*2,marks)
print(tuple(marks2))


#filter


namelenfilt = filter(lambda x: len(x)>4,users)
print(list(namelenfilt))
namewiths = filter(lambda x:x.startswith("s"),users)
print(set(namewiths))