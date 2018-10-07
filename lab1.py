# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 10:14:16 2018

@author: AnnaPS
"""
#Exercise 1
'''
p = 'ABCDEFGHIJK'
print(p[3:7])
print(p[:4])
print(p[6:])
print(p[-5:-1])
print(p[-3:])
print(p[:-1])
print(p[8:4])
print(p[-2:2])
print(p[-3:0])
'''

#Exercise 2
'''
N = [[2,3], [1,5]]
print(N[0][0]) #prints 2, index from 0
'''

'''
To create dictionary: 
d = {1: 'Peter', 2: 'Mark'}
print(d[1])
print(1 in d)
'''

#Exercise 3
'''
x = 0
y = 0
print(x is y)
x = 'A'
y = 'A'
print(x is y)
x = True
y = True
print(x is y)
x = None
y = None
print(x is y) 
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
print(x is y) #false
print(x == y) #true
x = {1, 2, 3, 4}
y = {1, 2, 3, 4}
print(x is y) #false
print(x == y) #true
x = {1: 'A', 2: 'B', 3: 'C', 4: 'D'}
y = {1: 'A', 2: 'B', 3: 'C', 4: 'D'}
print(x is y) #false
print(x == y) #true

#So is kind of like == in java, checks equality
#for basic types, but contents for e.g. lists.

#However the == checks for content equality
'''

#Exercise 4
'''
a) iterating a list - ordering matters, iterating
 a set, the ordering does not matter (unordered).
b) yes you can iterate over the keys

d = {1: 'Peter', 2: 'Mark'}
for keys in d:
    print(keys)
'''

#Exercise 5
'''
import random

guess_msg = 'Please guess an integer between {} and {}'
range_start = 1
range_end = 100
answer = random.randint(range_start, range_end)
i = 0
while i < 5:
    #Notify the user of the guess range
    print(guess_msg.format(range_start, range_end))
    guess = int(input())
    
    if guess is answer:
        print('Congratulations! That is correct.')
        print('--------New Game----------')
        range_start = 1
        range_end = 100
        answer = random.randint(range_start, range_end)
        i = 0
        continue
    else:
        if guess < answer:
            range_start = guess + 1
        else:
            range_end = guess - 1
    
    #Print hint after 3 guesses
    if i is 3:
        is_even = (answer % 2) == 0
        if is_even:
            print('Hint: The number is even')
        else: 
            print('Hint: The number is odd')
    
    i += 1

print('Game over. The answer was: %s' % (answer))
'''

#Optional exercise
import random

exterior = 1

while exterior:
    guess_msg = 'Please guess an integer between {} and {}'
    range_start = 1
    range_end = 100
    bomb = random.randint(range_start, range_end)
    players_turn = True
    interior = 1
    while interior:
        #Notify the user of the guess range
        print(guess_msg.format(range_start, range_end))
        guess = random.randint(range_start, range_end)
        
        if players_turn:
            players_turn = False
            guess = input()
            if 'break' in guess:
                exterior = 0
                break
            guess = int(guess)
            if guess is bomb:
                print('****BOM****')
                print('Bom triggered, you lose')
                interior = 0
                continue
        else:
            print('The computers guess is: %s' % (guess))
            players_turn = True
            if guess is bomb:
                print('****BOM****')
                print('Bom triggered, the computer loses')
                interior = 0
                continue
        if guess < bomb:
            range_start = guess + 1
        else:
            range_end = guess - 1

print('Game Finished')
