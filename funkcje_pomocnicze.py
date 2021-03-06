# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 19:27:55 2018

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
from statsmodels.stats.diagnostic import lilliefors
import pylab

dane_10_lat_df = pd.read_excel('team_v_team_5_dla18.xlsm', sheetname='stosunki_wagi')
schedule_14_15_df = pd.read_excel('schedules.xlsx', sheetname='18-19')

dane_10_lat = dane_10_lat_df.values.tolist() #list of lists
schedule_14_15 = schedule_14_15_df.values.tolist()
west_teams = ['DAL','DEN','GSW','HOU','LAC','LAL','MEM','MIN','NOP','PHO','POR','SAC','SAS','OKC','UTA']
east_teams = ['ATL','BOS','CHO','CHI','CLE','DET','IND','MIA','MIL','BRK','NYK','ORL','PHI','TOR','WAS']
gestosci = []
wyniki_east_14_15 = {'ATL':60, 
    'BOS':40,
    'CHO':33,
    'CHI':50,
    'CLE':53,
    'DET':32,
    'IND':38,
    'MIA':37,
    'MIL':41,
    'BRK':38,
    'NYK':17,
    'ORL':25,
    'PHI':18,
    'TOR':49,
    'WAS':46} 
wyniki_west_14_15 = {'DAL':50,
    'DEN':30,
    'GSW':67,
    'HOU':56,
    'LAC':56,
    'LAL':21,
    'MEM':55,
    'MIN':16,
    'NOP':45,
    'PHO':39,
    'POR':51,
    'SAC':29,
    'SAS':55,
    'OKC':45,
    'UTA':38} 

wyniki_14_15 = {'ATL':60, 
    'BOS':40,
    'CHO':33,
    'CHI':50,
    'CLE':53,
    'DET':32,
    'IND':38,
    'MIA':37,
    'MIL':41,
    'BRK':38,
    'NYK':17,
    'ORL':25,
    'PHI':18,
    'TOR':49,
    'WAS':46,
    'DAL':50,
    'DEN':30,
    'GSW':67,
    'HOU':56,
    'LAC':56,
    'LAL':21,
    'MEM':55,
    'MIN':16,
    'NOP':45,
    'PHO':39,
    'POR':51,
    'SAC':29,
    'SAS':55,
    'OKC':45,
    'UTA':38} 

wyniki_east_17_18 = {'ATL':24, 
    'BOS':55,
    'CHO':36,
    'CHI':27,
    'CLE':50,
    'DET':39,
    'IND':48,
    'MIA':44,
    'MIL':44,
    'BRK':28,
    'NYK':29,
    'ORL':25,
    'PHI':52,
    'TOR':59,
    'WAS':43} 
wyniki_west_17_18 = {'DAL':24,
    'DEN':46,
    'GSW':58,
    'HOU':65,
    'LAC':42,
    'LAL':35,
    'MEM':22,
    'MIN':47,
    'NOP':48,
    'PHO':21,
    'POR':49,
    'SAC':27,
    'SAS':47,
    'OKC':48,
    'UTA':48}

wyniki_17_18 = {'ATL':24, 
    'BOS':55,
    'CHO':36,
    'CHI':27,
    'CLE':50,
    'DAL':24,
    'DEN':46,
    'DET':39,
    'GSW':58,
    'HOU':65,
    'IND':48,
    'LAC':42,
    'LAL':35,
    'MEM':22,
    'MIA':44,
    'MIL':44,
    'MIN':47,
    'BRK':28,
    'NOP':48,
    'NYK':29,
    'ORL':25,
    'PHI':52,
    'PHO':21,
    'POR':49,
    'SAC':27,
    'SAS':47,
    'OKC':48,
    'TOR':59,
    'UTA':48,
    'WAS':43}

def find_indeks(indeks_fd):
    for indeks_i in range(1,len(dane_10_lat)+1):
        for indeks_j in range(len(dane_10_lat)):  #wyszukanie indeksu dla rozbudowanego mdoelu
            if dane_10_lat[indeks_j][0] == schedule_14_15[indeks_fd][0]: #dla bostonu
                indeks = indeks_j
                return indeks
            
def przejscia(lista, slownik):
    for key in lista:
        slownik[key[0]] += 1
            
def rysuj_wykres(slownik, tytul, osx, osy):
    names = list(slownik.keys())
    values = list(slownik.values())
    plt.bar(range(len(slownik)),values,tick_label=names)
    plt.title(tytul)
    plt.xlabel(osx)    
    plt.ylabel(osy)
    plt.show() 

def rysuj_histogram(numer, mody):
    nazwa = "Histogram zwyciestw "+ dane_10_lat[numer][0]
    plt.title(nazwa)
    plt.hist(gestosci[numer], bins = mody)

def rysuj_gestosc(lista, numer):
    pd.DataFrame(lista[numer]).plot(kind='density')

def most_common(L):   #kod z internetu, to nie plagiat?
  # get an iterable of (item, iterable) pairs
  SL = sorted((x, i) for i, x in enumerate(L))
  # print 'SL:', SL
  groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item
  def _auxfun(g):
    item, iterable = g
    count = 0
    min_index = len(L)
    for _, where in iterable:
      count += 1
      min_index = min(min_index, where)
    # print 'item %r, count %r, minind %r' % (item, count, min_index)
    return count, -min_index
  # pick the highest-count/earliest item
  return max(groups, key=_auxfun)[0]

def testy_norm(lista_gestosci, indeks):
    print('Shapiro-Wilk') # shapiro-wilk, nie sa normalne
    print(dane_10_lat[indeks][0], stats.shapiro(lista_gestosci[indeks]))
    print('Lilliefors') # shapiro-wilk, nie sa normalne
    print(dane_10_lat[indeks][0], lilliefors(lista_gestosci[indeks]))
    print('D’Agostino’s K^2 Test')
    # D’Agostino’s K^2 Test, Sample looks Gaussian (fail to reject H0)
    print(dane_10_lat[indeks][0], stats.normaltest(lista_gestosci[indeks]))
    print('Anderson-Darling test')
    print(dane_10_lat[indeks][0], stats.anderson(lista_gestosci[indeks]), 'norm')    

def boxploty_konf(lista_gest, lista_nazw, wyniki_dict, tytul, etykieta):        
    fig, ax = plt.subplots()
    ax.boxplot(lista_gest)
    plt.xticks([i for i in range(1,16)], lista_nazw)
    names = list(wyniki_dict.keys())
    values = list(wyniki_dict.values())
    plt.scatter(range(1,len(wyniki_dict)+1), values, label=etykieta, color='k')
    ax.set_title(tytul)
    ax.set_xlabel('Drużyna')
    ax.set_ylabel('Liczba zwycięstw')
    leg = plt.legend()
    plt.show()
    
def boxploty_konf_2018(lista_gest, lista_nazw, tytul):        
    fig, ax = plt.subplots()
    ax.boxplot(lista_gest)
    plt.xticks([i for i in range(1,16)], lista_nazw)
    ax.set_title(tytul)
    ax.set_xlabel('Drużyna')
    ax.set_ylabel('Liczba zwycięstw')
    plt.show()
    
def rysuj_qqplot(lista, numer):    
    stats.probplot(lista[numer], dist="norm", plot=pylab)
    pylab.show()
      
#a = [x+1 for x in a]
def predykcja():
    rnd1_east = list(x for x in przejscia_1rnd.items() if x[0] in east_teams)
    rnd1_east.sort(key=lambda x: x[1], reverse=True)
    rnd1_east=rnd1_east[0:8]
#    print('PLAYOFFS 1st Round:')   
#    print('East:')
    print(rnd1_east)
    
    rnd1_west = list(x for x in przejscia_1rnd.items() if x[0] in west_teams)
    rnd1_west.sort(key=lambda x: x[1], reverse=True)
    rnd1_west=rnd1_west[0:8]
#    print('PLAYOFFS 1st Round:')   
#    print('west:')
    print(rnd1_west)

    rnd2_east = list(x for x in przejscia_2rnd.items() if x[0] in east_teams)
    rnd2_east.sort(key=lambda x: x[1], reverse=True)
    rnd2_east=rnd2_east[0:4]
#    print('PLAYOFFS 2nd Round:')   
#    print('East:')
    print(rnd2_east)
    
    rnd2_west = list(x for x in przejscia_2rnd.items() if x[0] in west_teams)
    rnd2_west.sort(key=lambda x: x[1], reverse=True)
    rnd2_west=rnd2_west[0:4]
#    print('PLAYOFFS 2nd Round:')   
#    print('west:')
    print(rnd2_west)   
    
    rnd3_east = list(x for x in przejscia_3rnd.items() if x[0] in east_teams)
    rnd3_east.sort(key=lambda x: x[1], reverse=True)
    rnd3_east=rnd3_east[0:2]
#    print('PLAYOFFS 3rd Round:')   
#    print('East:')
    print(rnd3_east)
    
    rnd3_west = list(x for x in przejscia_3rnd.items() if x[0] in west_teams)
    rnd3_west.sort(key=lambda x: x[1], reverse=True)
    rnd3_west=rnd3_west[0:2]
#    print('PLAYOFFS 3rd Round:')   
#    print('west:')
    print(rnd3_west)
    
    final_pred_east = list(x for x in przejscia_final.items() if x[0] in east_teams)
    final_pred_east.sort(key=lambda x: x[1], reverse=True)
    final_pred=final_pred_east[0:1]
    final_pred_west = list(x for x in przejscia_final.items() if x[0] in west_teams)
    final_pred_west.sort(key=lambda x: x[1], reverse=True)
    final_pred.append(final_pred_west[0:1])
#    print('PLAYOFFS Finals:')
    print(final_pred) 

    champs_pred = list(dict_champs.items())
    champs_pred.sort(key=lambda x: x[1], reverse=True)
    champs_pred=champs_pred[0]
#    print('Champions:')
    print(champs_pred)       
 ##################################################################3   
  


