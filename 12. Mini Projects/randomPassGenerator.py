#a program that genrates a strong random password of n length

#concept -- we are going to create a list of all the possible characters (which are valid in the password) -- A-Z, a-z, 0-9, Punctuators-(\,/,!,@,-,#,$,%,^,&,*,(,)) etc. From this list -- we can generate N random characters to create a random password which could be N length long

# import random
# import string #colletion of string constants

# val= random.choice(["a",69,"xyz",2,3])
# print(val)

# print(string.ascii_letters) #americal standard code for information interchange
# print(string.digits)
# print(string.punctuation)

# print(random.choice("Aditya Jain")) #-- will print any random character from the string

#-------------------------------------

import random
import string #colletion of string constants

charValues = string.ascii_letters + string.digits + string.punctuation

pass_len= int(input("Enter the digits of how long you want your password to be: "))
# pass_len=6

# password=""
# for i in range(pass_len):
#     password+=random.choice(charValues)

# print(f'Your random password is: {password}')

#----------------------------

#using list comprehention syntax: {funtion for i in range(n)}

# .join method when used with an empty string concatenates any number of strings //the string whose method is called is inserted in between each given string (as a joiner). The result is returned as a new string.

res = "".join([random.choice(charValues) for i in range(pass_len)])
print("Your random password is: ",res)
