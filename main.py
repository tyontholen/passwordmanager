master_pwd = input ("Please enter master password: ")

def view():
    #r mode, reads only
    with open('passwords.txt', 'r') as file:
        for line in file.readlines():
            #seperate the username and password for viewing
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "- Password:", passw)

def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    

    #with open for file management
    #w mode, write, overwrites files
    #append mode, create a new file if doesn't exist, otherwise add to the end of existing file
    with open('passwords.txt', 'a') as file:
        #writes to the file combining account name and password to a new line
        file.write(name + "|" + pwd + "\n")
    

while True:
    mode = input("Add new password or view existing (view, add) ? Press q to quit. ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue