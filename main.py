# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 13:46:21 2023

@author: HSN
"""

import pandas as pd

names = ['HSN','Rey','Zahra']

def read_csv(path):
    df = pd.read_csv(path)
    return df

df = read_csv('bahman.csv')

def get_rows_by_name(name):
    return df.loc[df['Name'] == name]

def get_total_spent_by_name(name):
    rows = get_rows_by_name(name)
    return rows['Spent'].sum()

def get_total_spent():
    return df['Spent'].sum()

def get_total_for_house():
    rows = df.loc[(df['HSN'] == 1) & (df['Rey'] == 1) & (df['Zahra'] == 1)]
    return rows['Spent'].sum()

def get_dong_for_house():
    return get_total_for_house()/3

def get_total_for_us():
    rows = df.loc[(df['HSN'] == 1) & (df['Rey'] == 1) & (df['Zahra'] == 0)]
    return rows['Spent'].sum()

def get_dong_for_us():
    return get_total_for_us()/2

def get_dong_for_one_from_who(a,b,names):
    rows = df.loc[(df[b] == 1)]
    qry_str = ''
    for name in names:
        if (name != b):
            qry_str += str(name) + "=0 and"
    
    qry_str = qry_str[:-3]
    
    rows =rows.query(qry_str)




print()

















