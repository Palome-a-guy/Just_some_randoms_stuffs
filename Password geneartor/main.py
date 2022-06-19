import random

try:
    password_length = int(input("Length of the password = "))
except:
    password_length = int(input("Enter a number : "))

characters = "abcdefghijklmnopqrstxyz0123456789é&€AZERTYUIOPQSDFGHJKLMWXCVBN"

password = ""   

for index in range(password_length):
    password = password + random.choice(characters)

print("Password generated:")
print(password)