# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 09:15:32 2018

@author: AnnaPS
"""
import numpy as np
import pandas as pd

csv_path = 'US_census.csv'
d = pd.read_csv(csv_path, na_values=["?"])
print(d.head())
print(d.shape)

#######################TASK 1######################################
"""
Delete the tuple if its attribute value in either workclass or occupation is 
missing
"""
d_w_o = d[['Workclass','Occupation']]
index_nan = np.where(pd.isna(d_w_o))[0] #gives indexes of all nan values in d_w_o
d.drop(index_nan, inplace=True)

"""
For the missing values in native country, fill with the major one (i.e. the 
country that appear most in the dataset) 
"""
country = d['Native country'].mode() #mode = most common value
print("\nMost common native country: %s" % country[0])
d['Native country'].fillna(country[0], inplace=True)

"""
For the missing values in working hours per week, fill with the average value 
(rounded to nearest integer) of this attribute. 
"""
work_h = round(d['Working hours per week'].mean())
print("\nThe average working hours per week is %s" % work_h)
d['Working hours per week'].fillna(work_h, inplace=True)
d.to_csv('task 1.csv')

#######################TASK 2######################################


rm_col = ['Final sampling weight', 'Years of education', 'Capital gain', 
          'Capital loss']
d.drop(rm_col, axis=1, inplace=True)
print("\nSize after removal of columns: %s" % str(d.shape))
d.to_csv('task 2.csv')

#######################TASK 3######################################
age_group = []

for age in d['Age']:
    group = ">=60"
    
    if age < 20:
        group = "<20"
    elif age < 29:
        group = "20-29"
    elif age < 39:
        group = "30-39"
    elif age < 49:
        group = "40-49"
    elif age < 59:
        group = "50-59"
        
    age_group.append(group)
    
d["Age group"] = np.asarray(age_group)

pred_inc = d["Predicted income"]
pred_inc.replace("<=50K", 1, inplace=True)
pred_inc.replace(">50K", 0, inplace=True)

d.to_csv('task 3.csv')
