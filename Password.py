from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb")as key_file:
        key_file.write(key)
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pw = input("What is your master password? : ")
key = load_key() 
fer = Fernet(key)



def view():
    with open("passwords.txt", "r")as f:
        for line in r.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("user: ",user, "\t","Password: ",fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account name : ")
    pw = input("Password: ")

    with open("passwords.txt", "a")as f:
        f.write(name + "|" + fer.encrypt(pw.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing one?(view,add),press q to quit : ").lower
    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode")
        continue