# Dictionary adalah Object kalo di dart
# Array with key

user = {
    "name" : "Azri",
    "age" : 18,
    "is_admin" : True
}

user["username"] = "maybeazri"
user["name"] = "Muhammad Azri"

name = user.get('name')
temp = user.get('username', "agungsetiawan")

print (name)
print (temp)