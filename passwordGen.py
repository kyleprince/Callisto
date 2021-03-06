import random
import string
import datetime
import array

# PasswordGen function
def passwordGen():
    # Open file and set datetime
    file = open('./password.txt', 'a')
    d = datetime.datetime.now()

    # Create variable buckets
    letters = "abcdefghjkmnpqrstuvwxyz"
    caps = "ABCDEFGHJKLMNPQRSTUVWXYZ"
    digits = "23456789"
    special = "!@#$%&?+"

    # Create prefix and month
    prefix = random.choice(caps) + random.choice(caps) + random.choice(caps)
    month = d.strftime("%B")
    
    # Build the password
    password = prefix + month
    password += random.choice(digits)
    password += random.choice(digits)
    password += random.choice(digits)
    password += random.choice(digits)
    password += random.choice(special)
    file.write("\n")
    print(password)
    file.write(password)
    file.close()

# Main
passwordGen()
