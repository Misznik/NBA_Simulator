# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 12:39:12 2018

@author: micha
"""

import pandas as pd
import random as rd
import matplotlib.pylab as plt
import numpy as np
import copy
from scipy import stats
import itertools
import operator
from statsmodels.graphics.gofplots import qqplot
import seaborn as sns; sns.set()
from funkcje_pomocnicze import *

dane_10_lat_df = pd.read_excel('team_v_team_10_makra.xlsm', sheetname='stosunki_simple')
wygrane_10_lat_df = pd.read_excel('team_v_team_10_makra.xlsm', sheetname='suma_bez_wag')
schedule_14_15_df = pd.read_excel('schedules.xlsx', sheetname='14-15')

dane_10_lat = dane_10_lat_df.values.tolist() #list of lists
schedule_14_15 = schedule_14_15_df.values.tolist() #zamiana dataframe na liste

gestosci = []
for i in range(len(dane_10_lat)):
    gestosci.append([])

dict_champs = {'ATL':0, #slownik ilosci wygranych mistrzostw
'BOS':0,
'CHA':0,
'CHI':0,
'CLE':0,
'DAL':0,
'DEN':0,
'DET':0,
'GSW':0,
'HOU':0,
'IND':0,
'LAC':0,
'LAL':0,
'MEM':0,
'MIA':0,
'MIL':0,
'MIN':0,
'NJN':0,
'NOH':0,
'NYK':0,
'ORL':0,
'PHI':0,
'PHO':0,
'POR':0,
'SAC':0,
'SAS':0,
'SEA':0,
'TOR':0,
'UTA':0,
'WAS':0}

prawdopodobienstwa = copy.deepcopy(dict_champs)
przejscia_1rnd = copy.deepcopy(dict_champs)
przejscia_2rnd = copy.deepcopy(dict_champs)
przejscia_3rnd = copy.deepcopy(dict_champs)
przejscia_final = copy.deepcopy(dict_champs)
finalowe4 = []

west_teams = ['DAL','DEN','GSW','HOU','LAC','LAL','MEM','MIN','NOH','PHO','POR','SAC','SAS','SEA','UTA']
east_teams = ['ATL','BOS','CHA','CHI','CLE','DET','IND','MIA','MIL','NJN','NYK','ORL','PHI','TOR','WAS']

N = 1000 #Ilosc symulacji

#############################  LOOPING
for n in range(1,N+1):
    wyniki = [['ATL',0],  #lista z wynikami, dopisujemy do niej kolejne zwyciestwa
    ['BOS',0],
    ['CHA',0],
    ['CHI',0],
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
    ['NJN',0],
    ['NOH',0],
    ['NYK',0],
    ['ORL',0],
    ['PHI',0],
    ['PHO',0],
    ['POR',0],
    ['SAC',0],
    ['SAS',0],
    ['SEA',0],
    ['TOR',0],
    ['UTA',0],
    ['WAS',0]]
    
    #  Symulacja sezonu zasadniczego
    for j in range(0,len(schedule_14_15[0])-1):  
        for i in range(j+1,len(schedule_14_15[0])): #rozpoczecie petli od drugiego elementu; pomiciecie nazwy
            for number in range(0,schedule_14_15[j][i]):
                prob = dane_10_lat[j][1]/(dane_10_lat[j][1]+dane_10_lat[i-1][1]) #wyznaczanie usrednionej szansy na zwyciestwo
                result = rd.random() #wyznaczania liczby losowej z przedzialu [0,1]
                if result <= prob:
                    wyniki[j][1]+=1
                else:
                    wyniki[i-1][1]+=1 #przez roznice w strukturze trzeba inaczej indeksowac
    
    east = []
    west = []
    
    for k in range(0,len(wyniki)):
        if wyniki[k][0] in east_teams:
            east.append(wyniki[k])
        else:
            west.append(wyniki[k])
     
    east.sort(key=lambda x: x[1], reverse = True) #sortowanie po drugim elemencie
    west.sort(key=lambda x: x[1], reverse = True)
            
    rnd1_east = east[:8]
    rnd1_west = west[:8]
    
    ##################################   EAST 1st ROUND
    rnd2_east = [[],[],[],[]]
    win = [0,0,0,0,0,0,0,0]
    while win[0] < 4 and win[7] < 4:  #NOWY POMYSL NA SYMULACJE PLAYOFFOW: WYNIKI Z TEGO SEZONU
        prob = rnd1_east[0][1]/(rnd1_east[0][1]+rnd1_east[7][1])
        result = rd.random()
        if result <= prob:
            win[0]+=1
        else:
            win[7]+=1
    if win[0] == 4:
        rnd2_east[0]=rnd1_east[0]
    else:
        rnd2_east[0]=rnd1_east[7]
        
    while win[3] < 4 and win[4] < 4:  #NOWY POMYSL NA SYMULACJE PLAYOFFOW: WYNIKI Z TEGO SEZONU
        prob = rnd1_east[3][1]/(rnd1_east[3][1]+rnd1_east[4][1])
        result = rd.random()
        if result <= prob:
            win[3]+=1
        else:
            win[4]+=1
    if win[3] == 4:
        rnd2_east[1]=rnd1_east[3]
    else:
        rnd2_east[1]=rnd1_east[4]
        
    while win[2] < 4 and win[5] < 4:  #NOWY POMYSL NA SYMULACJE PLAYOFFOW: WYNIKI Z TEGO SEZONU
        prob = rnd1_east[2][1]/(rnd1_east[2][1]+rnd1_east[5][1])
        result = rd.random()
        if result <= prob:
            win[2]+=1
        else:
            win[5]+=1
    if win[2] == 4:
        rnd2_east[2]=rnd1_east[2]
    else:
        rnd2_east[2]=rnd1_east[5]
        
    while win[1] < 4 and win[6] < 4:  #NOWY POMYSL NA SYMULACJE PLAYOFFOW: WYNIKI Z TEGO SEZONU
        prob = rnd1_east[1][1]/(rnd1_east[1][1]+rnd1_east[6][1])
        result = rd.random()
        if result <= prob:
            win[1]+=1
        else:
            win[6]+=1
    if win[1] == 4:
        rnd2_east[3]=rnd1_east[1]
    else:
        rnd2_east[3]=rnd1_east[6]
        
        
    ##########################################################   WEST 1st ROUND
    rnd2_west = [[],[],[],[]]
    win = [0,0,0,0,0,0,0,0]
    while win[0] < 4 and win[7] < 4:  #NOWY POMYSL NA SYMULACJE PLAYOFFOW: WYNIKI Z TEGO SEZONU
        prob = rnd1_west[0][1]/(rnd1_west[0][1]+rnd1_west[7][1])
        result = rd.random()
        if result <= prob:
            win[0]+=1
        else:
            win[7]+=1
    if win[0] == 4:
        rnd2_west[0]=rnd1_west[0]
    else:
        rnd2_west[0]=rnd1_west[7]
        
    while win[3] < 4 and win[4] < 4:  #NOWY POMYSL NA SYMULACJE PLAYOFFOW: WYNIKI Z TEGO SEZONU
        prob = rnd1_west[3][1]/(rnd1_west[3][1]+rnd1_west[4][1])
        result = rd.random()
        if result <= prob:
            win[3]+=1
        else:
            win[4]+=1
    if win[3] == 4:
        rnd2_west[1]=rnd1_west[3]
    else:
        rnd2_west[1]=rnd1_west[4]
        
    while win[2] < 4 and win[5] < 4:  #NOWY POMYSL NA SYMULACJE PLAYOFFOW: WYNIKI Z TEGO SEZONU
        prob = rnd1_west[2][1]/(rnd1_west[2][1]+rnd1_west[5][1])
        result = rd.random()
        if result <= prob:
            win[2]+=1
        else:
            win[5]+=1
    if win[2] == 4:
        rnd2_west[2]=rnd1_west[2]
    else:
        rnd2_west[2]=rnd1_west[5]
        
    while win[1] < 4 and win[6] < 4:  #NOWY POMYSL NA SYMULACJE PLAYOFFOW: WYNIKI Z TEGO SEZONU
        prob = rnd1_west[1][1]/(rnd1_west[1][1]+rnd1_west[6][1])
        result = rd.random()
        if result <= prob:
            win[1]+=1
        else:
            win[6]+=1
    if win[1] == 4:
        rnd2_west[3]=rnd1_west[1]
    else:
        rnd2_west[3]=rnd1_west[6]
    #############################################################   RND2 EAST     
    rnd3_east = [[],[]]
    win = [0,0,0,0]
    while win[0] < 4 and win[1] < 4: 
        prob = rnd2_east[0][1]/(rnd2_east[0][1]+rnd2_east[1][1])
        result = rd.random()
        if result <= prob:
            win[0]+=1
        else:
            win[1]+=1
    if win[0] == 4:
        rnd3_east[0]=rnd2_east[0]
    else:
        rnd3_east[0]=rnd2_east[1]    
     
    while win[2] < 4 and win[3] < 4: 
        prob = rnd2_east[2][1]/(rnd2_east[2][1]+rnd2_east[3][1])
        result = rd.random()
        if result <= prob:
            win[2]+=1
        else:
            win[3]+=1
    if win[2] == 4:
        rnd3_east[1]=rnd2_east[2]
    else:
        rnd3_east[1]=rnd2_east[3]  
    
    #############################################################   RND2 WEST     
    rnd3_west = [[],[]]
    win = [0,0,0,0]
    while win[0] < 4 and win[1] < 4: 
        prob = rnd2_west[0][1]/(rnd2_west[0][1]+rnd2_west[1][1])
        result = rd.random()
        if result <= prob:
            win[0]+=1
        else:
            win[1]+=1
    if win[0] == 4:
        rnd3_west[0]=rnd2_west[0]
    else:
        rnd3_west[0]=rnd2_west[1]    
     
    while win[2] < 4 and win[3] < 4: 
        prob = rnd2_west[2][1]/(rnd2_west[2][1]+rnd2_west[3][1])
        result = rd.random()
        if result <= prob:
            win[2]+=1
        else:
            win[3]+=1
    if win[2] == 4:
        rnd3_west[1]=rnd2_west[2]
    else:
        rnd3_west[1]=rnd2_west[3]  
    ########################################  CONFERENCE FINALS
    final=[[],[]]
    win = [0,0]
    while win[0] < 4 and win[1] < 4: 
        prob = rnd3_east[0][1]/(rnd3_east[0][1]+rnd3_east[1][1])
        result = rd.random()
        if result <= prob:
            win[0]+=1
        else:
            win[1]+=1
    if win[0] == 4:
        final[0]=rnd3_east[0]
    else:
        final[0]=rnd3_east[1]
        
    win = [0,0]
    while win[0] < 4 and win[1] < 4: 
        prob = rnd3_west[0][1]/(rnd3_west[0][1]+rnd3_west[1][1])
        result = rd.random()
        if result <= prob:
            win[0]+=1
        else:
            win[1]+=1
    if win[0] == 4:
        final[1]=rnd3_west[0]
    else:
        final[1]=rnd3_west[1]   
        
    ########################################  FINALS
    champion=[[]]
    win = [0,0]
    while win[0] < 4 and win[1] < 4: 
        prob = final[0][1]/(final[0][1]+final[1][1])
        result = rd.random()
        if result <= prob:
            win[0]+=1
        else:
            win[1]+=1
    if win[0] == 4:
        champion[0]=final[0]
    else:
        champion[0]=final[1]
        
    dict_champs[champion[0][0]]+=1
    przejscia(rnd1_east, przejscia_1rnd)
    przejscia(rnd1_west, przejscia_1rnd)
    przejscia(rnd2_east, przejscia_2rnd)
    przejscia(rnd2_west, przejscia_2rnd)
    przejscia(rnd3_east, przejscia_3rnd)
    przejscia(rnd3_west, przejscia_3rnd)
    przejscia(final, przejscia_final)
    
    for i in range(len(dane_10_lat)):
        gestosci[i].append(wyniki[i][1])
        
    czworka_sort = ([rnd3_east[0][0],rnd3_east[1][0],rnd3_west[0][0],rnd3_west[1][0]])
    finalowe4.append(sorted(czworka_sort))

print('Eastern conference:')
print(east)
print('Western conference:')
print(west)
print('PLAYOFFS 1st Round:')   
print('East:')
print(rnd1_east)
print('West:')
print(rnd1_west)
print('PLAYOFFS 2nd Round:')   
print('East:')
print(rnd2_east)
print('West:')
print(rnd2_west)
print('Conference finals:')   
print('East:')
print(rnd3_east)
print('West:')
print(rnd3_west)
print('Finals:')
print(final)
print('Champion:')
print(champion)

srednie = []
for i in range(len(gestosci)):
    srednie.append([dane_10_lat[i][0], np.mean(gestosci[i])])

east_density = []
west_density = []
for i in range(len(gestosci)): 
    if dane_10_lat[i][0] in east_teams:
        east_density.append(gestosci[i])
    elif dane_10_lat[i][0] in west_teams:
        west_density.append(gestosci[i])

#boxploty_konf(east_density, east_teams)  
#boxploty_konf(west_density, west_teams)   
#rysuj_wykres(dict_champs,'mistrzowie')
#rysuj_wykres(przejscia_1rnd,'przejscia do 1 rundy')
#rysuj_wykres(przejscia_2rnd,'przejscia do 2 rundy')
#rysuj_wykres(przejscia_3rnd,'przejscia do 3 rundy')
#rysuj_wykres(przejscia_final,'przejscia do finalow')
#rysuj_gestosc(gestosci,4)
#rysuj_histogram(1,10)
#testy_norm(gestosci)
print('najczestsze czworki ' ,most_common(finalowe4))

   
##################################################  PRZEJSCIA
#names2 = list(przejscia_1rnd.keys())             #przyklad rysowania wykresu
#values2 = list(przejscia_1rnd.values())
#plt.figure(2)
#plt.subplot(211)
#plt.title('do 1 rundy')
#plt.bar(range(len(przejscia_1rnd)),values2,tick_label=names2)
#plt.show()

#suma = 0
#for i in range(len(dane_10_lat)):
#    suma += dane_10_lat[i][1]
#for i in range(len(dane_10_lat)):
#    prawdopodobienstwa[dane_10_lat[i][0]] = dane_10_lat[i][1]/suma*N #- 25  #zblizony ksztalt
#names2=[]
#values2=[]
#for i in range(len(dane_10_lat)):
#    names2.append(dane_10_lat[i][0])
#    values2.append(dane_10_lat[i][1])
#plt.figure(4)
#plt.title('Stosunek ilosci wygranych do ilosci meczy wygranych do rozegranych w 10 lat')
#plt.bar(range(len(dane_10_lat)),values2,tick_label=names2)
#plt.show()
