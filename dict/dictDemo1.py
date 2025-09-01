# data = {}
# print(data)

data = {"Gujarat":"Gandhinagar","Maharashtra":"Mumbai","Rajasthan":"Jaipur","Up":"Lucknow",
        "Gujarat":"Ahmdabad"}
print(data)
k = data.keys()
print(list(k))

v = data.values()
print(v)

kv = data.items()
print(kv)

for i,j in data.items():
    print(i,j)
    
    
#single value access
print(data.get("Gujarat"))    
print(data["Gujarat"])


#add..
data["Punjab"] ="Chandigadh"
data["Maharashtra"] = "Pune"

#add 2nd way
data.update({"Goa":"Panji","Jammu":"Shrinagar"})
print(data)



#remove...
removedValue = data.pop("Goa") #it will remove goa and panji check wigth in operator..
print(f"removing... {removedValue}")
print(data)

removedData = data.popitem() #it will remove last key value pair
print(f"removedData {removedData}")
print(data)
