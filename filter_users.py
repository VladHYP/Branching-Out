import json


def load_users():
    """Load users from the JSON file and return them as a list."""
    with open("users.json", "r", encoding="utf-8") as file:
        return json.load(file)


def filter_by_name(users, name_filter):
    """Return users whose names contain the given search text."""
    return [user for user in users if name_filter.lower() in user["name"].lower()]


def filter_by_age(users, age_filter):
    """Return users whose age matches the given age."""
    return [user for user in users if user["age"] == age_filter]


def filter_by_email(users, email_filter):
    """Return users whose email contains the given search text."""
    return [user for user in users if email_filter.lower() in user["email"].lower()]


def main():
    """Ask the user which filter to apply and print matching users."""
    users = load_users()

    print("Choose a filter:")
    print("1. Name")
    print("2. Age")
    print("3. Email")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        name_filter = input("Enter name to search: ")
        filtered_users = filter_by_name(users, name_filter)
        print("Users filtered by name:")
    elif choice == "2":
        age_filter = int(input("Enter age to search: "))
        filtered_users = filter_by_age(users, age_filter)
        print("Users filtered by age:")
    elif choice == "3":
        email_filter = input("Enter email to search: ")
        filtered_users = filter_by_email(users, email_filter)
        print("Users filtered by email:")
    else:
        print("Invalid choice.")
        return

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    main()