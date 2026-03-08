import json


def filter_by_name(users, name_filter):
    return [
        user for user in users
        if name_filter.lower() in user["name"].lower()
    ]


def filter_by_age(users, age_filter):
    return [
        user for user in users
        if user["age"] == age_filter
    ]


with open("users.json", "r") as file:
    users = json.load(file)

name_filter = input("Enter name to search: ")
age_filter = int(input("Enter age to search: "))

filtered_by_name = filter_by_name(users, name_filter)
filtered_by_age = filter_by_age(users, age_filter)

print("Users filtered by name:")
for user in filtered_by_name:
    print(user)

print("Users filtered by age:")
for user in filtered_by_age:
    print(user)