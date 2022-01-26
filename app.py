## PYTHON :- READING AND WRITING IN JSON

# JSON 
import json

#reading the Json data

# f = open("data.json")

# #converting into json

# data = json.load(f)

# for i in data['emp_details']:
#     print(i)

# f.close()    


#Writing Json data

dictionary = {
    "name": "John",
    "email": "john123@gmail.com",
    "bloodGroup": "B+ve"
}

dictionary["name"] = input("enter name")
dictionary["email"] = input("enter email")
dictionary["bloodGroup"] = input("enter bloodGroup")


#serializing json
json_object = json.dumps(dictionary, indent = 4)

#writing the json
with open("data.json", "w") as outfile:
    outfile.write(json_object)

