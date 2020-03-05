# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 00:03:51 2019

@author: Xiaoqing Ding
"""

import os
import pandas as pd

try:  
    
    file_name = os.path.join(r'C:\Users','bbq59','OneDrive','2019','2019 Fall','CS 767','project','^VIX.csv')
    df = pd.read_csv(file_name)    
    
    #using this to get the data for VIX
    a = [i for i in range(1995,2019)]   
    for i in range(len(a)):

        a[i] = df[df.Year == a[i]]
        a[i] = a[i].groupby('Week_Number')['Close'].mean()
        
        if len(a[i]) > 52:
            a[i] = a[i].drop(a[i].index[52])
        if i == 0:
            VIX = a[0]
        else:
            VIX = VIX.append(a[i])    
    
    #using this to decide the label 
    VIX = VIX.values.tolist()
    label = [[]for i in range(1248)]
    
    for i in range(len(VIX)):
        if VIX[i] > 40 or VIX[i] < 15:
            label[i].append('Red')
        else: 
            label[i].append('green')
    

    
    
    
    
    
except Exception as e:
    print(e)