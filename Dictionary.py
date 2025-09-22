my_dict = {
    "key1":"value1",
    "key2":"value2",
    "key3":"value3",
    "key4":"value4"
}
print(my_dict)

# Creating dictionary:
# normal dictionary:
BioData = {
    "name" : "Prasad",
    "rollno": 4,
    "branch": "cse cs",
    "place": "zaheerabad"
}
print(BioData) 

# Dictionary using constructor:
BioData1 = dict( Name="prasad",roll_no=4,branch="cse cs")
print(BioData1)

# SQUARE BRACKETS:
print(BioData["name"])
print(BioData["rollno"])
print(BioData["branch"])
print(BioData["place"])

# using get() method:
print(BioData.get("name"))
print(BioData.get("rollno"))
print(BioData.get("branch"))
print(BioData.get("place"))

# adding and updating dictionary:
BioData = {
    "name" : "Prasad",
    "rollno": 4,
    "branch": "cse cs",
    "place": "zaheerabad"
}

# update:
BioData["role"] = "abp" 
BioData["Place"] = "nkd"
print(BioData)

# add:
BioData[" hydra"] = "rr" 
print(BioData)

# removing in dictionary:
BioData = {
    "name" : "Prasad",
    "rollno": 4,
    "blood group":"o",
    "branch": "cse cs",
    "place": "zaheerabad",
    "role":"SDE"
}
print(BioData)

# loops for dictionary:
BioData = {
    "name" : "Chary",
    "rollno": 28,
    "blood group":"o",
    "branch": "cse cs",
    "place": "zhb",
    "role":"SDE"
}
for i in BioData.keys():
    print(i)
for i in BioData.values():
    print(i)
for i in BioData.items():
    print(i)    


    