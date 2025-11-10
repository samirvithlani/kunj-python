no = int(input("enter no :"))

try:
    if no<18:
        raise ValueError("number must >18 ")

except ValueError as e:
    print(e)
        