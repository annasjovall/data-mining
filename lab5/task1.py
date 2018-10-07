# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 15:36:56 2018

@author: AnnaPS
"""
from Orange.data import Table, Domain

data_tab = Table.from_file('mushroom.csv')

#########################TASK 1################################
feature_vars = data_tab.domain.attributes
class_label_var = data_tab.domain[0]
mushroom_domain = Domain(feature_vars, class_label_var)

data_tab = Table.from_table(domain=mushroom_domain, source=data_tab)

print("DOMAIN: %s \nVARIABLES: %s \nATTRIBUTES: %s \nCLASS_VAR: %s" 
      % (data_tab.domain, data_tab.domain.variables, data_tab.domain.attributes, 
         data_tab.domain.class_var))

#########################TASK 2################################