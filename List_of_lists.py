# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 23:06:49 2016

@author: t0rqu3
"""

import csv
 
with open('way_to_file', 'rU') as infile:
   reader = csv.DictReader(infile)
   data = {}
   for row in reader:
     for header, value in row.items():
       try:
         data[header].append(value)
       except KeyError:
         data[header] = [value]
print data 
