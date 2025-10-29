#Creating a dictionary
dic = {"name" : "vijay", "age" : 24, "course" : "python"}
print("1. Printing dictionary values                   : ",dic)

new_dic = dict(zip([1,2,3],["vijay","deeksha","swathi"]))
print("2. Printing newly created dictionary            : ",new_dic)

#Adding new value
dic["location"] = "Chennai"
print("3. After adding new values                      : ",dic)

#Updating existing value
dic["location"] = "Nellai"
print("4. After updating an existing values            : ",dic)

dob = {"dob" : "13/11/2000"}
dic.update(dob)
print("5. Adding new values using udpate method        : ",dic)

#Pop used in dictionary
dic.pop("age")
print("6. After using pop function                     : ",dic)

#Popitem
value = dic.popitem()
print("7. After using popitem with deleted value       : ",value,dic)

#Update method
dic.update({"age" : 24})
print("8. Adding new values using update method        : ",dic)

#len method
print("9. Finding length of dictionary                 : ",len(dic))

#copy method
dic_copy = dic.copy()
print("10. Printing copied dictionary using copy()     : ",dic_copy)

#get method - if key not found in dictionary it will not throw an error instead it retuns none.
# print(dic.get("name"))
print("11. Printing value using get function           : ",dic.get("location"))

print("12. Printing value using indexing method        : ",dic["name"])
# print(dic["location"]) #but this way throw an error so mostly prefer get method to access key.

#Looping dictionary
print("13. Iterating over for loops using dic name     : ",end=" ")
for i in dic:
    print(i,end=" ")

print("\n14. Iterating over for loops using keys()       : ",end=" ")
for i in dic.keys():
    print(i,end=" ")

print("\n15. Iterating over for loops using values()     : ",end=" ")
for i in dic.values():
    print(i,end=" ")

print("\n16. Iterating over for loops using items()      : ",end=" ")
for key,value in dic.items():
    print(f"{key} : {value}",end=", ")

#Merge dictionaries
dic1 = {1:"Vijay",2:"Swathi"}
dic2 = {3:"Deeksha",4:"Laksh"}
dic1.update(dic2)
print("\n17. After merge two dictionaries using update   : ",dic1)