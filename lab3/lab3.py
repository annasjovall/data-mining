# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 09:54:00 2018

@author: AnnaPS
"""
import numpy as np
import pandas as pd

#Exercise 1
"""
with open('test1.txt') as f:
    print('Is f closed? {}'.format(f.closed))
    for line in f.readlines():
        print(line.rstrip())
        
print('Is f closed? {}'.format(f.closed))

data = ['The is output line 1\r\n', 'The is output line 2\r\n',
'The is output line 3\r\n', 'The is output line 4\r\n']

with open('test2.txt', 'w') as f:
    f.writelines(data)
"""

#Exercise 2
"""
arr1 = np.array([1, 2.2, 7, 19])
print(arr1) #[ 1.   2.2  7.  19. ]

arr2 = np.array([[19, 22, 65], [4, 18]])
print(arr2) #[list([19, 22, 65]) list([4, 18])]
"""

#Exercise 3
"""
arr1 = np.array([[2.1, 3., 4.5], [0.8, 5.1, 2.4]])
print(arr1) #[[2.1 3.  4.5] [0.8 5.1 2.4]]

arr2 = np.array(((2.1, 3., 4.5), (0.8, 5.1, 2.4)))
print(arr2) #[[2.1 3.  4.5] [0.8 5.1 2.4]]
"""

#Exercise 4
"""
arr = np.array([[11, 16, 21, 33, 44], [4, 17, 20, 14, 57], [5, 24, 34, 42, 38]])
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)
"""

#Exercise 5
"""
arr = np.array([[11, 16, 21, 33, 44], [4, 17, 20, 14, 57], [5, 24, 34, 42, 38],
[7, 11, 25, 49, 61]])
print(arr[:, ::-1])
"""

#Exercise 6
"""
arr = np.zeros((4, 3))
arr1 = np.insert(arr, 2, [1, 1, 1, 1])
print(arr1)
#[0. 0. 1. 1. 1. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
"""

#Exercise 7
"""
arr = np.random.rand(6,5)
print(arr)
print()
#delete row 5
arr1 = np.delete(arr, 4, axis=0)
print(arr1)
print()
#delete col 2
arr2 = np.delete(arr, 1, axis=1)
print(arr2)
"""

#Exercise 8
"""
arr = np.array([2, 3, 4, 5])
s = pd.Series(arr)
print(s) #dtype: int32
"""

#Exercise 9
"""
dic =	{
  "apple": 11,
  "banana": 22,
  "cherry": 33
}
s = pd.Series(dic)
print(s) #dtype: int64
ss = pd.Series(dic, index=[6, 7, 8])
print(ss) #dtype: float64
"""

#Exercise 10

dic = {
  'dict1' : {"anna": 1, "panna": 2, "banana": 3},
  'dict2' : {"b": "c"},
  'dict3' : {45: "anna"}
}
print(dic)
d = pd.DataFrame(dic)
print(d) #It works but does not look great


#Exercise 11
"""
d = pd.DataFrame([['California', 'Sacramento', 39536653],
                ['Utah', 'Salt Lake City', 3101833],
                ['Texas', 'Austin', 28304596],
                ['Florida', 'Tallahassee', 20984400],
                ['Minnesota', 'Saint Paul', 5576606]],
                index=['Cal', 'Uta', 'Tex', 'Flo', 'Min'],
                columns=['State', 'Capital', 'Population'])
print(type(d['Population']))
print(type(d.iloc[3]))
print(d[['Population', 'State']])
print(d.iloc[:, 0:3:2])
"""

#Exercise 12
"""Using the given CSV file “tut3.csv”, calculate the total mark (= assignment marks +
exam marks) for every student and put it to the appended column “Total mark”, and then export
modified dataframe to another CSV file."""
csv_path = 'tut3.csv'
d = pd.read_csv(csv_path, index_col = "Student Id")
print(d)
print(d.shape)

total_marks = []
for i in d.index:
    row = d.loc[i]
    mark = row['Assignment marks'] + row['Exam marks']
    total_marks.append(mark)
    
d_tot = pd.DataFrame(total_marks, index = d.index, columns=['Total mark'])

d_mod = d.join(d_tot)
d_mod.to_csv('inc_tot_mark.csv')