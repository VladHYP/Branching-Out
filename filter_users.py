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


def filter_by_email(users, email_filter):
    return [
        user for user in users
        if email_filter.lower() in user["email"].lower()
    ]


with open("users.json", "r") as file:
    users = json.load(file)

name_filter = input("Enter name to search: ")
age_filter = int(input("Enter age to search: "))
email_filter = input("Enter email to search: ")

filtered_by_name = filter_by_name(users, name_filter)
filtered_by_age = filter_by_age(users, age_filter)
filtered_by_email = filter_by_email(users, email_filter)

print("Users filtered by name:")
for user in filtered_by_name:
    print(user)

print("Users filtered by age:")
for user in filtered_by_age:
    print(user)

print("Users filtered by email:")
for user in filtered_by_email:
    print(user)