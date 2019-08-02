import os
file = str(os.getcwd()) #to get the current directory of python file
details = {}            #converting the database values into a dictionary
with open(file + "\Database\Database.txt") as f:
    for line in f:
        (key, value) = line.split()
        details[key] = value

close = False

def option():
    option = input("What would you like master?:\n1.Signup\n2.Login\n3.Password change\n4.Close\n")
    #option = option.lower() #converting to lower to create uniformity
    if "1" in option:
        signup()
    elif "2" in option:
        ID = input("ID: ")
        password = input("Password: ")
        login(ID,password) #caling the login function with the ID and Password
    elif "3" in option:
        ID = input("ID: ")
        new_password = input("New password: ")
        passwordchange(ID, new_password) 
    elif "4" in option:
        global close
        close = True
    else:
        print("What do you want?") 
    
def signup():
    ID = input("ID: ")
    if ID in details:
        print("ID already exists.")
    else:
        fopen = open(file + "\Database\Database.txt" ,"a")
        password = input("Password: ")
        fopen.write(ID)
        fopen.write(" " + password + "\n")
        fopen.close()

def login(ID,password):
    if ID in details: #using the global variable stored values
        if details[ID] == password:
            print("Login Successful.") #calling to check password
        else:
            print("Wrong password.")
    else:
            print("No ID exists.")

def passwordchange(ID, new_password): #writing everything except our old ID instead of deleting
    details = {} #declaring a local variable, so not the same as the above one
    with open(file + "\Database\Database.txt", 'r') as f: #opening as read first to store the values
        for line in f:
            (key,value) = line.split()
            details[key] = value
    with open(file + "\Database\Database.txt", 'w') as f:
        if ID in details:
            for name in details:
                if ID != name: #writing everything except the ID
                    f.write(name)
                    f.write(" " + value + "\n")
            f.write(ID)
            f.write(" " + new_password + "\n")
        else:
            print("No such ID exists.")
        
run = True
while run:
    option()
    if close == True:
        run = False
        
