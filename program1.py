# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 12:39:12 2018

@author: micha
"""

import pandas as pd
import random as rd
import math

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

west_teams = ['DAL','DEN','GSW','HOU','LAC','MEM','MIN','NOH','SEA','PHO','POR','SAC','SAS','UTA']
east_teams = ['BOS','NJN','CHI','CHA','CLE','DET','IND','MIA','MIL','NYK','ORL','PHI','TOR','WAS']

#prob = dane_10_lat[0][1]/(dane_10_lat[0][1]+dane_10_lat[1][1])
#print(rd.random() >= prob)

#for i in range(1,len(dane_10_lat),1):
    #print(dane_10_lat[i-1][0])
    #print(wyniki[i-1][0])  #taka sama strunktura, moze slownik?
    #print(dane_10_lat[i-1][0])
ilosc_gier=0
N=100

#for n in range(0,N):
for j in range(0,len(schedule_14_15[0])-1):  
    for i in range(j+1,len(schedule_14_15[0])): #rozpoczecie petli od drugiego elementu, pomiciecie nazwy
        #ilosc_gier+=schedule_14_15[j][i]
        for number in range(0,schedule_14_15[j][i]):
            prob = dane_10_lat[j][1]/(dane_10_lat[j][1]+dane_10_lat[i-1][1])
            result = rd.random()
            if result <= prob:
                wyniki[j][1]+=1
            else:
                wyniki[i-1][1]+=1 #przez roznice w struktureze trzeba inaczej indeksowac

#for n in range(0,len(wyniki)):
#    wyniki[n][1]=round(wyniki[n][1]/N)
#    ilosc_gier+=wyniki[n][1]

#posortowane = wyniki
#for n in range(0,len(posortowane)):
#    posortowane[n].reverse() 
#posortowane = sorted(posortowane, reverse = True)
#print(wyniki)
#print(ilosc_gier)

east = []
west = []

for k in range(0,len(wyniki)):
    if wyniki[k][0] in east_teams:
        east.append(wyniki[k])
    else:
        west.append(wyniki[k])
 
east.sort(key=lambda x: x[1], reverse = True) #sortowanie po drugim elemencie
west.sort(key=lambda x: x[1], reverse = True)
print(east)
print(west)

print('PLAYOFFS:')   #SCHEMAT
rnd1_east = east[:8]
rnd1_west = west[:8]
print(rnd1_east)
print(rnd1_west)

#rnd2_east = [[],[],[],[]]
#rnd2_west = [[],[],[],[]]
#win = [0,0,0,0,0,0,0,0]
#while win[0] < 4 and win[7] < 4:  #NOWY POMYSL NA SYMULACJE PLAYOFFOW: WYNIKI Z TEGO SEZONU
#    prob = rnd1_east[0][1]/(rnd1_east[0][1]+rnd1_east[7][1])
#    result = rd.random()
#    if result <= prob:
#        win[0]+=1
#    else:
#        win[7]+=1
#if win[0] == 4:
#    rnd2_east[0]=rnd1_east[0]
#else:
#    rnd2_east[0]=rnd1_east[7]
#    
#rnd3_east = [[],[]]
#rnd3_west = [[],[]]
#win = [0,0,0,0]
#while win[0] < 4 and win[1] < 4: 
#    prob = rnd2_east[0][1]/(rnd2_east[0][1]+rnd2_east[1][1])
#    result = rd.random()
#    if result <= prob:
#        win[0]+=1
#    else:
#        win[1]+=1
#if win[0] == 4:
#    rnd3_east[0]=rnd2_east[0]
#else:
#    rnd2_east[0]=rnd1_east[1]    
#    
#final=[[],[]]
#win = [0,0]
