"Source: https://geekflare.com/password-generator-python-code/"
import string 
import random 

#characters used in password generatoe 
characters = list(string.ascii_letters + string.digits + "!@#$%^&()")

def generate_random_password():
    ##unit length of password from user 
    length = int(input("Enter password length"))
    
    #character shuffle
    random.shuffle(characters)
    
    ## picking random characters from the list 
    password = []
    for i in range(length):
        password.append(random.choice(characters))
        
    ## shuffling the password
    random.shuffle(password)
    
    ## convert list to string
    #print list 
    print("".join(password))
    
