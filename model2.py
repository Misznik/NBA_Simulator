# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 17:25:03 2018

@author: micha
"""
import pandas as pd
import random as rd
import matplotlib.pylab as plt

dane_10_lat_df = pd.read_excel('team_v_team_10_makra.xlsm', sheetname='stosunki')
schedule_14_15_df = pd.read_excel('schedules.xlsx', sheetname='14-15')

dane_10_lat = dane_10_lat_df.values.tolist() #list of lists
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
    ['WAS',0]]

def find_indeks(indeks_fd):
    for indeks_i in range(1,len(dane_10_lat)+1):
        for indeks_j in range(len(dane_10_lat)):  #wyszukanie indeksu dla rozbudowanego mdoelu
            if dane_10_lat[indeks_j][0] == schedule_14_15[indeks_fd][0]: #dla bostonu
                indeks = indeks_j
                return indeks
                
#for indeks_i in range(1,len(dane_10_lat)+1):
#    for indeks_j in range(len(dane_10_lat)):  #wyszukanie indeksu dla rozbudowanego mdoelu
#        if dane_10_lat[indeks_j][0] == schedule_14_15[1][0]: #dla bostonu
#            indeks = indeks_j
#            print(dane_10_lat[indeks][indeks_i], indeks_i, indeks_j)

for j in range(0,len(schedule_14_15[0])-1):  
        for i in range(j+1,len(schedule_14_15[0])): #rozpoczecie petli od drugiego elementu; pomiciecie nazwy
            for number in range(0,schedule_14_15[j][i]):
                indeks = find_indeks(i)
                prob = dane_10_lat[j][indeks] #wyznaczanie usrednionej szansy na zwyciestwo
                result = rd.random() #wyznaczania liczby losowej z przedzialu [0,1]
                print(j,i,schedule_14_15[j][i],prob,result,schedule_14_15[i-1][0])
                if result <= prob:
                    wyniki[j][1]+=1
                else:
                    wyniki[i-1][1]+=1

           
#for j in range(0,len(schedule_14_15[0])-1):     #bckp
#        for i in range(j+1,len(schedule_14_15[0])):
#            for indeks_i in range(len(dane_10_lat)):  #wyszukanie indeksu dla rozbudowanego mdoelu
#                for indeks_j in range(len(dane_10_lat)): 
#                    if dane_10_lat[indeks_j][0] == schedule_14_15[i-1][0]:
#                        indeks = indeks_j
#            prob = dane_10_lat[indeks][indeks_i]                        
#            for number in range(0,schedule_14_15[j][i]):
#                result = rd.random()
#                if result <= prob:
#                    wyniki[j][1]+=1
#                else:
#                    wyniki[i-1][1]+=1
# 

#ilosc = 0
#for it in range(len(wyniki)):
#    ilosc += wyniki[it][1]                  
print(wyniki)
#print(ilosc)
# TU JUZ BEZ SREDNIEJ WAZONEJ