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

dane_10_lat_df = pd.read_excel('team_v_team_10_makra.xlsm', sheetname='stosunki_wagi')
schedule_14_15_df = pd.read_excel('schedules.xlsx', sheetname='14-15')
dane_10_lat = dane_10_lat_df.values.tolist() #list of lists
schedule_14_15 = schedule_14_15_df.values.tolist()
west_teams = ['DAL','DEN','GSW','HOU','LAC','LAL','MEM','MIN','NOH','PHO','POR','SAC','SAS','SEA','UTA']
east_teams = ['ATL','BOS','CHA','CHI','CLE','DET','IND','MIA','MIL','NJN','NYK','ORL','PHI','TOR','WAS']
gestosci = []

def find_indeks(indeks_fd):
    for indeks_i in range(1,len(dane_10_lat)+1):
        for indeks_j in range(len(dane_10_lat)):  #wyszukanie indeksu dla rozbudowanego mdoelu
            if dane_10_lat[indeks_j][0] == schedule_14_15[indeks_fd][0]: #dla bostonu
                indeks = indeks_j
                return indeks
            
def przejscia(lista, slownik):
    for key in lista:
        slownik[key[0]] += 1
            
def rysuj_wykres(slownik, tytul):
    names = list(slownik.keys())
    values = list(slownik.values())
    plt.bar(range(len(slownik)),values,tick_label=names)
    plt.title(tytul)
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

def testy_norm(lista_gestosci):
    print('Shapiro-Wilk')
    for i in range(len(lista_gestosci)):  # shapiro-wilk, nie sa normalne
        print(dane_10_lat[i][0], stats.shapiro(lista_gestosci[i]))
    print('D’Agostino’s K^2 Test')
    for i in range(len(lista_gestosci)):  # D’Agostino’s K^2 Test, Sample looks Gaussian (fail to reject H0)
        print(dane_10_lat[i][0], stats.normaltest(lista_gestosci[i]))
    print('Anderson-Darling test')
    for i in range(len(lista_gestosci)):  # 
        print(dane_10_lat[i][0], stats.anderson(lista_gestosci[i]), 'norm')    

def boxploty_konf(lista_gest, lista_nazw):        
    fig, ax = plt.subplots()
    ax.boxplot(lista_gest)
    plt.xticks([i for i in range(1,16)], lista_nazw)
    plt.show()
        