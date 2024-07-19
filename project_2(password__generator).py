import random
import string
length = int(input("Enter required length of password : "))

chars = string.ascii_letters
chars += string.digits
chars += string.punctuation

password_1 = ""

for i in range(length):
    password_1 += random.choice(chars)
password_1 = ''.join([random.choice(chars) for i in range(length)])
if password_1 == '':
    print("password generation failed")
else:
    print("Generated password is : ", password_1)
    print("Password generation successful")