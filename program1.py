# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 12:39:12 2018

@author: micha
"""

import pandas as pd
import random as rd

dane_10_lat_df = pd.read_excel('team_v_team_10_makra.xlsm', sheetname='stosunki_simple')
schedule_14_15_df = pd.read_excel('schedules.xlsx', sheetname='14-15')

dane_10_lat = dane_10_lat_df.values.tolist() #list of lists
#dane_10_lat[ATL][1]
schedule_14_15 = schedule_14_15_df.values.tolist()

wyniki = [['ATL',0],
['BOS',0],
['NJN',0],
['CHI',0],
['CHA',0],
['CLE',0],
['DAL',0],
['DEN',0],
['DET',0],
['GSW',0],
['HOU',0],
['IND',0],
['LAC',0],
['LAL',0],
['MEM',0],
['MIA',0],
['MIL',0],
['MIN',0],
['NOH',0],
['NYK',0],
['SEA',0],
['ORL',0],
['PHI',0],
['PHO',0],
['POR',0],
['SAC',0],
['SAS',0],
['TOR',0],
['UTA',0],
['WAS',0],
]

#prob = dane_10_lat[0][1]/(dane_10_lat[0][1]+dane_10_lat[1][1])
#print(rd.random() >= prob)

#for i in range(1,len(dane_10_lat),1):
    #print(dane_10_lat[i-1][0])
    #print(wyniki[i-1][0])  #taka sama strunktura, moze slownik?
    #print(dane_10_lat[i-1][0])
     
for i in range(1,len(schedule_14_15[0])): #rozpoczecie petli od drugiego elementu, pomiciecie nazwy
    for number in range(0,schedule_14_15[0][i]):
        prob = dane_10_lat[0][1]/(dane_10_lat[0][1]+dane_10_lat[i-1][1])
        result = rd.random()
        if result <= prob:
            wyniki[0][1]+=1
        else:
            wyniki[i-1][1]+=1 #przez roznice w struktureze trzeba inaczej indeksowac
    
