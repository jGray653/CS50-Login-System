import random
import string
import csv
import sys

def main():
    try:
        print("1: Log In")
        print("2: Create a Login")

        choice = int(input("Please Choose: "))
        print(descision(choice))

    except ValueError:
        sys.exit("Invalid Input, Please Try Again")



def descision(c):
    try:
        if c == 1:
            u = input("Username: ")
            p = input("Password: ")
            return login(u, p)
        elif c == 2:
            n = input("What is your Name? ")
            return create(n)
        else:
            return "Invalid Selection, Please Try Again\n"
    except ValueError:
        sys.exit("A Value Error Was Raised.")

def login(u, p):
    users = []

    with open("information.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append({"name": row["name"], "username": row["username"], "password": row["password"]})

        for user in users:
            if user["username"] == f"{u}":
                if user["password"] == f"{p}":
                    return f"Hello, {user["name"]}"
                else:
                    return "Incorrect Password"

        return "User Doesn't Exist, Please Create An Account\n"

def create(n):
    try:
        users = []

        if "," in n:
            last, first = n.split(",")
            password = gen_pass()
            username = gen_user(first)
        else:
            first, last = n.split(" ")
            password = gen_pass()
            username = gen_user(first)

        with open("information.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                users.append({"name": row["name"], "username": row["username"], "password": row["password"]})

            for user in users:
                if user["name"] == f"{first} {last}":
                    return "User Already Exists, Please Try Again"

        with open("information.csv", "a") as file:
            file.write(f"{first} {last},{username},{password}\n")
            print(f"Username: {username}\nPassword: {password}")
            return "User Created! Please Sign In!"
    except ValueError:
        sys.exit("Please Input a Valid First and Last Name")


def gen_pass():
    alph = None
    for _ in range(3):
        alph = f"{alph}{random.choice(string.ascii_lowercase)}"
    numb = random.randint(1000, 9999)
    alph = alph.removeprefix("None")

    return f"{alph}{numb}"

def gen_user(n):
    for i in range(3):
        if i == 0:
            n = f"{n}_{random.randint(0, 9)}"
        else:
            n = f"{n}{random.randint(0, 9)}"
    return n

if __name__ == "__main__":
    main()
