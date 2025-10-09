#Creating a dictionary
dic = {"name" : "vijay", "age" : 24, "course" : "python"}
print(dic)

new_dic = dict(zip([1,2,3],["vijay","deeksha","swathi"]))
print(new_dic)

#Adding new value
dic["location"] = "Chennai"
print(dic)

#Updating existing value
dic["location"] = "Nellai"
print(dic)

dob = {"dob" : "13/11/2000"}
dic.update(dob)
print(dic)

#Pop used in dictionary
dic.pop("age")
print(dic)

#Popitem
value = dic.popitem()
print(dic)

#Update method
dic.update({"age" : 24})
print(dic)

#len method
print(len(dic))

#copy method
dic_copy = dic.copy()
print(dic_copy)

#get method - if key not found in dictionary it will not throw an error instead it retuns none.
print(dic.get("name"))
print(dic.get("location"))

print(dic["name"])
# print(dic["location"]) #but this way throw an error so mostly prefer get method to access key.

#Looping dictionary
for i in dic:
    print(i,end=" ")

print("")
for i in dic.keys():
    print(i,end=" ")

print("")
for i in dic.values():
    print(i,end=" ")

print("")
for key,value in dic.items():
    print(f"{key} : {value}")

#Merge dictionaries
dic1 = {1:"Vijay",2:"Swathi"}
dic2 = {3:"Deeksha",4:"Laksh"}
dic1.update(dic2)
print(dic1)