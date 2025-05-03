## Log-in screen -- user is asked to provide a username and password.

users_list = {
    "annasmith12" : "welcome2022",
    "angeloramos3" : "welcome2025",
    "lawrenceford09" : "welcome2015",
    "ericfredd55" : "welcome2020"
}

username_input = ""

while username_input == "":
    username_input = input("Please input your username: ")
    if username_input in users_list.keys():
        print("Username found.")
    else:
        print("Username does not exist.")
        username_input = ""
        print("## ----- ## \n")

print("## ----- ## \n")
print(f"Welcome {username_input}!")


password_input = ""
login_attempt = 3

while password_input == "":
    password_input = input("Please input your password: ")
    if password_input == users_list[username_input]:
        print("Login successful!")
    else:
        print("Wrong password entered.")
        password_input = ""
        login_attempt -= 1
        if login_attempt <= 0:
            print("You have entered the wrong password many times.")
            print("You are prohibited from logging in.")
            print("## ---- ## \n")
            break
        else:
            print("Please input your password again.")
            print(f"You have {login_attempt} attemp(s) left.")
            print("## ---- ## \n")
            
        

