import json

with open("users.json", "r") as file:
    users = json.load(file)

name_filter = input("Enter name to search: ")

filtered_users = [
    user for user in users
    if name_filter.lower() in user["name"].lower()
]

for user in filtered_users:
    print(user)