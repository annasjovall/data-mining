# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 09:28:24 2018

@author: Anna Palmqvist Sjövall


Assignment One 
CSE5DMI Data Mining
Part I
"""

#The string S that is used in all parts of Q1
s = "This is a string"

"""
 A for loop that prints the 
 ASCII code of each character in a string 
 named S. 
 
 1.a)
"""
for char in s: print("%s : %d" % (char, ord(char)))

"""
 A loop that computes the sum of the ASCII 
 codes of all characters in a string.
 
 1.b)
"""
print("\nThe sum of the ASCII codes is: %d" % sum(map(ord, s)))

"""
 A loop that returns a new list that contained the ASCII code of each character
 in the string
  
 1.c)
"""
print("\nThe list of each characters ASCII value:")
print(*[ord(c) for c in s])