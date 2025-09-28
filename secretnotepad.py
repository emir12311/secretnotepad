from os import system
from time import sleep
from hashlib import sha256
import base64
import json

def login():
    system('cls||clear')
    global username
    global t
    if username == "":
        username = input("Please enter your username: ")
    passw = t[username][0]
    for p in range(0, 2):    
        password = input("Password: ")
        encryptedpass = sha256(password.encode("utf-8")) 
        if encryptedpass.hexdigest() == passw:
            print("Access granted")
            access = "Granted"
            sleep(1)
            system('cls||clear')
            break
        else:
            print("Access denied, Try again.")

def newaccount():
    print("It seems like that username doesnt exist in our database")
    while q != "n":
        accountcreate = input("Would you like to create a new account? (y/n) ")
        if accountcreate == "y":
            newpass = input("Enter password for the new account: ") 
            newencryptpass = sha256(newpass.encode("utf-8"))
            t[username] = [newencryptpass.hexdigest(), ""]
            with open("keys.json", "w") as s:
                json.dump(t, s)
            print("Account successfully created, redirecting you to the login..")
            sleep(1)
            break
        else:
            quit()
try:
    with open("keys.json", "r") as b:
        t = json.load(b)
except:
    with open("keys.json", "a") as g:
        json.dump({"admin": ["akdgajdf", ""]}, g)

    with open("keys.json", "r") as b:
      t = json.load(b)
        

q = "."

access = ""

username = input("Please enter your username: ")

allusers = list(t.keys())

if username in allusers:
    login()
else:
    newaccount()
    username = ""
    login()
    
#67 mentioned!!!!!!!!!!(sndsf njsdhbcsbuawdfbsefupornoarfeueshusethusrdhfsye6rfh8ayw)

vs = t.get(username)
notes = vs[1]

if notes == "":
    wr = input("It seems like you dont have notes saved, would you like to write? (y/n) ")
    if wr.lower() == "y": 
        writenote = input(": ")
        t[username][1] = writenote
        with open("keys.json", "w") as y:
            json.dump(t, y)
else:
    print("Your saved notes are:")
    print(notes)
    editext = input("Write over, Add or Quit (w/a/q)? ")
    