#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 14:12:19 2020

@author: Jake
"""

import pandas as pd
import numpy as np

all_df = pd.concat([pl_df, spain_df, france_df, italy_df], axis = 0, ignore_index = True)



#%% preliminary cleaning

for each in all_df.columns:
    if 'over' in each.lower():
        all_df.drop([each], inplace = True, axis = 1)
    elif 'under' in each.lower():
        all_df.drop([each], inplace = True, axis = 1)
    elif 'prediction' in each.lower():
        all_df.drop([each], inplace = True, axis = 1)
    elif 'suspended' in each.lower():
        all_df.drop([each], inplace = True, axis = 1)


all_df['season'] = all_df['season'].apply(lambda x: x.replace('/', '-'))



 


#%%

all_df = all_df.drop(['team_name'], axis = 1)
all_df.rename(columns = {'common_name':'team'}, inplace = True)

# get rid of incomplete seasons due to Covid-19
bad_df = all_df.loc[all_df['matches_played']<38]
all_df = all_df.loc[all_df['matches_played']==38]

cols2keep = ['team', 'season', 'country', 'wins', 'draws', 'losses', 'points_per_game', 'goals_scored', 'goals_conceded', 'goal_difference',\
                    'clean_sheets', 'fts_count', 'leading_at_half_time', 'average_possession', 'cards_total', 'losing_at_half_time_home'\
                        ]
all_df = all_df[cols2keep]

#changing country column to league
dict = {'England': 'EPL', 'Italy': 'Serie A', 'France': 'Ligue 1', 'Spain': 'La Liga', 'Wales': 'EPL', 'Monaco': 'Ligue 1'}
for i, j in dict.items():
    all_df['country'].replace(i, j, inplace=True)
all_df.rename(columns = {'country': 'league'}, inplace=True)

all_df['start_year'] = all_df['season'].apply(lambda x: x.split('-')[0]).astype('int64')
all_df['points'] = (all_df['wins']*3)+all_df['draws']

#new col, total points the following season
all_df.sort_values(by=['start_year', 'league', 'points'], ascending = [True, True, False], inplace =True)

all_df['ns_points']=0

all_df.reset_index(drop = True, inplace=True)

#%%

ns_points =  []
for index, row in all_df.iterrows():
    team = row['team']
    df = all_df[all_df['team']==team] # creating a df of all instances with that team
    year = row['start_year'] # identifying what season the team is in
    for idx, rw in df.iterrows():
        if rw['start_year'] == year + 1:
            all_df['ns_points'].iloc[index] = rw['points']
            break
        elif rw['start_year'] == year + 2:
            all_df['ns_points'].iloc[index] = rw['points']
            break
        elif rw['start_year'] == year + 3:
            all_df['ns_points'].iloc[index] = rw['points']
            break
        elif rw['start_year'] == year + 4:
            all_df['ns_points'].iloc[index] = rw['points']
            break
        elif rw['start_year'] == year + 5:
            all_df['ns_points'].iloc[index] = rw['points']
            break
        elif rw['start_year'] == year + 6:
            all_df['ns_points'].iloc[index] = rw['points']
            break
        elif rw['start_year'] == year + 7:
            all_df['ns_points'].iloc[index] = rw['points']
            break
        elif rw['start_year'] == year + 8:
            all_df['ns_points'].iloc[index] = rw['points']
            break
        elif rw['start_year'] == year + 9:
            all_df['ns_points'].iloc[index] = rw['points']
            break
        elif rw['start_year'] == year + 10:
            all_df['ns_points'].iloc[index] = rw['points']
            break
        elif rw['start_year'] == year + 11:
            all_df['ns_points'].iloc[index] = rw['points']
            break
        elif rw['start_year'] == year + 12:
            all_df['ns_points'].iloc[index] = rw['points']
            break
        else:
            all_df['ns_points'].iloc[index] = 'NaN'
            
        
            

# redo with all footystats seasons data and possibly kaggle's 06-07 data appended
# load up other leagues with 20 teams: serie A and la liga, to provide extra data to train

# clean data to make matching
#engineer useful fetaures - next season points total
#drop irrelevant values

# features from kaggle: 'saves', 'total_pass', 'penalty_conceded', 'touches'
# features from footystats: 

