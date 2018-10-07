# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 09:49:58 2018

@author: AnnaPS
"""

#Exercise 1
"""
def say_hello():
    return "hello", "good-bye"

print(say_hello())
hi, bye = say_hello()
print(hi)
print(bye)
"""

#Exercise 2
"""
def demo_opt_params(param1, param2 = 'optional parameter 1', 
                    param3 = 'optional parameter 2'):
    print('Parameter 1: ' + str(param1))
    print('Parameter 2: ' + str(param2))
    print('Parameter 3: ' + str(param3))
    print('---------')

#prints same thing
demo_opt_params('string 1', 'string 2', 'string 3')
demo_opt_params(param1 = 'string 1', param2 = 'string 2', param3 = 'string 3')
#prints different (string 3 will be parameter 2 in the first case, not the second)
demo_opt_params('string 1', 'string 3')
demo_opt_params(param1 = 'string 1', param3 = 'string 3')
"""

#Exercise 3

def is_pallindrome(p):
    pallindrome = str(p).lower()
    length = len(pallindrome)
    
    for i in range(length//2):
        last = pallindrome[length-1-i]
        first = pallindrome[i]
        if(first != last):
            return False
    return True

print(is_pallindrome("anna"))
print(is_pallindrome(1991))
print(is_pallindrome(2133412))

#Optional exercise
"""
the generated password must consists of:
1. at least one uppercase character
2. at least one lowercase character
3. at least two digits
4. at least one punctuation character @#$%&
"""
import re, string, random

def check_password(password):
     # searching for digits
    digit = re.search(r"\d", password)

    # searching for uppercase
    uppercase = re.search(r"[A-Z]", password)

    # searching for lowercase
    lowercase = re.search(r"[a-z]", password)

    # searching for symbols
    symbol = re.search(r"\W", password)

    # overall result
    ok =  digit and uppercase and lowercase and symbol
    return ok is not None
    
def generate_password(pass_length = 8):
    if pass_length < 8:
        pass_length = 8
    ok = False
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ""
    while not ok:
        password = ''.join(random.choice(chars) for i in range(pass_length))
        print(password)
        if check_password(password):
            ok = True
    return password

print("generated password: " + generate_password(10))
