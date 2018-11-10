#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 19:50:58 2018

@author: zhangyufei
"""

import os
import csv

path = os.path.join('election_data.csv')
total_vote = 0
election = {}
with open(path,newline = '', encoding = 'utf-8') as file:
    reader = csv.reader(file, delimiter = ',')
    header = next(reader)
    for row in reader:
        if row[2] in election.keys():
            election[row[2]] += 1
        else:
            election[row[2]] = 1
        total_vote += 1
with open(os.path.join('output.csv'),'w') as file:
    file.write(f'Election Results \n-------------------------\nTotal Votes: {total_vote}')
    print('Election Results \n-------------------------')
    print(f'Total Votes: {total_vote}')
    
    
    winner = ''
    max_vote = 0
    for key in election.keys():
        print(f'{key}: {"{:.3%}".format(election[key]/total_vote)} ({election[key]})')
        file.write(f'{key}: {"{:.3%}".format(election[key]/total_vote)} ({election[key]})\n')
        if election[key] > max_vote:
            max_vote = election[key]
            winner = key
    
    print(f'-------------------------\nWinner: {winner}')
    file.write(f'-------------------------\nWinner: {winner}')

        