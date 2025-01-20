#importing the encryption module
from cryptography.fernet import Fernet

#load and read the saved key, read binary
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


#master_pwd = input ("Please enter master password: ")
#encoding masterpass to match with bytes
key = load_key() # + master_pwd.encode()
fer = Fernet(key)

"""
def write_key():
    key = Fernet.generate_key()
    #write mode, binary mode
    #creates a key, call it once in your project
    with open("key.key", "wb") as key_file:
        key_file.write(key)
""" 

#write_key()        






def view():
    #r mode, reads only
    with open('passwords.txt', 'r') as file:
        for line in file.readlines():
            #seperate the username and password for viewing
            data = line.rstrip()
            user, passw = data.split("|")
            #decode to remove the byte'' when viewing
            print("User:", user, "- Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    

    #with open for file management
    #w mode, write, overwrites files
    #append mode, create a new file if doesn't exist, otherwise add to the end of existing file
    with open('passwords.txt', 'a') as file:
        #writes to the file combining account name and password to a new line
        file.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
    

while True:
    mode = input("Add new password or view existing (view, add). Press q to quit. ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue