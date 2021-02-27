#!/usr/bin/python
#!/usr/bin/env python
import subprocess
import time
import random
import os
import sys

print ("---------------------------------------------------Welcome To MagicPass!!-----------------------------------------------")

chars = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm`¬!£$%^&*()_+{}@~<>?|\/.,;#{}1234567890'

length = input('Password Length? :')
length = int(length)

number = input('How many passwords? : ')
number = int(number)
print("")

for p in range (number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
    print("")
      
   
time.sleep(0.5)

print("Restarting...")
subprocess.call(sys.argv[0], shell=True)

