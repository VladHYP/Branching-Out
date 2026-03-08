import json


def load_users():
    with open("users.json", "r") as file:
        return json.load(file)


def filter_by_name(users, name_filter):
    return [user for user in users if name_filter.lower() in user["name"].lower()]


def filter_by_age(users, age_filter):
    return [user for user in users if user["age"] == age_filter]


def filter_by_email(users, email_filter):
    return [user for user in users if email_filter.lower() in user["email"].lower()]


def main():
    users = load_users()

    name_filter = input("Enter name to search: ")
    age_filter = int(input("Enter age to search: "))
    email_filter = input("Enter email to search: ")

    print("Users filtered by name:")
    for user in filter_by_name(users, name_filter):
        print(user)

    print("Users filtered by age:")
    for user in filter_by_age(users, age_filter):
        print(user)

    print("Users filtered by email:")
    for user in filter_by_email(users, email_filter):
        print(user)


if __name__ == "__main__":
    main()