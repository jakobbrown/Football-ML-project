#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 20:07:39 2020

@author: Jake
"""

import glob
import pandas as pd
import numpy as np

#read data and concatenate dataframes - Spain



#read data and concatenate dataframes - teams
teams_files = glob.glob('/Users/Jake/Documents/uni/project:datasets/football stats/footystats/Premier League/england-premier-league-teams*.csv')


teamslist = []


for filename in teams_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    teamslist.append(df)

pl_df = pd.concat(teamslist, axis=0, ignore_index=True)


teams_files = glob.glob('/Users/Jake/Documents/uni/project:datasets/football stats/footystats/La Liga/spain-la-liga-teams*.csv')


teamslist = []


for filename in teams_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    teamslist.append(df)

spain_df = pd.concat(teamslist, axis=0, ignore_index=True)


teams_files = glob.glob('/Users/Jake/Documents/uni/project:datasets/football stats/footystats/Serie A/italy-serie-a-teams*.csv')


teamslist = []


for filename in teams_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    teamslist.append(df)

italy_df = pd.concat(teamslist, axis=0, ignore_index=True)

teams_files = glob.glob('/Users/Jake/Documents/uni/project:datasets/football stats/footystats/Ligue 1/france-ligue-1-teams*.csv')


teamslist = []


for filename in teams_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    teamslist.append(df)

france_df = pd.concat(teamslist, axis=0, ignore_index=True)



#%%