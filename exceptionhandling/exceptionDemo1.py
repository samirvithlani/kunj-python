#error: compile time syntext....
#exception : logical,....
#Exception

#How to handle ex:
#using try except block.
#using raise keyword


try:
    no1 = int(input("enter no 1 :"))
    no2 = int(input("enter no 2 :"))
    ans = no1 / no2
    print(ans)
except ZeroDivisionError as e:
    print("can not divide by zero",e) 
except ValueError as e:
    print("check your inpurt..",e)       