# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 11:34:56 2014

@author: Simon
"""
import csv
import datetime
import numpy as np
import matplotlib.pyplot as plt
dato = []
svovel = []

with open('vps_single_ship_data.csv', 'rb') as csvfile:
    ship = csv.reader(csvfile) #, delimiter=',') #, quotechar='"')
    for row in ship:
        try:
            svovel.append(float(row[8]))
            dato.append(row[0])
        except:
            pass
            # svovel.append(row[8])
                
        
del svovel[0]
del dato[0]
dato2 = []
for row in dato:
    # datetime.datetime.strptime('row[0]-row[1]-row[2]', '%y-%m-%d').date()
    c_dato = datetime.datetime.strptime(row, '%Y-%m-%d').date()
    
    dato2.append(c_dato)

list.sort(dato2)
plot(dato2, svovel)
tall = 0
noe = []
begrensning = 100
while tall < begrensning:
    tall = tall+1
    noe.append (tall)
tall = 0
summen = 0
while tall < begrensning:
    summen = summen + noe[tall]
    tall += 1

print summen