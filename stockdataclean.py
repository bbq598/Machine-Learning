# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 22:21:31 2019
data clean 
@author: Xiaoqing Ding
"""

import os
import pandas as pd
import numpy as np

import csv

try:   
    #res = pd.concat([df1995mean, df1996mean], axis=1, join_axes=[df1995mean.index])

    file_name = os.path.join(r'C:\Users','bbq59','OneDrive','2019','2019 Fall','CS 767','project','^DJI.csv')
    df = pd.read_csv(file_name)
    #firs get the data for each year
    #df1995 = df[df.Year == 1995]
    #then get the data for each 123

    #df1995mean= df1995.groupby('Week_Number')['Return'].mean()
    # now get the one data from DJI from 1995. 
    #x = df1995mean.values.tolist()
    #after that doing the samething for each year and out put the list to the csv file. 
    
    #output_file = os.path.join('DJI_1995.csv')
    #df1995mean.to_csv(output_file, index=False)
    
    #to get the data per week for the stock DJI and append them to DJI dataframe 
    a = [i for i in range(1995,2019)]   
    for i in range(len(a)):

        a[i] = df[df.Year == a[i]]
        a[i] = a[i].groupby('Week_Number')['Return'].mean()
        
        if len(a[i]) > 52:
            a[i] = a[i].drop(a[i].index[52])
        if i == 0:
            DJI = a[0]
        else:
            DJI = DJI.append(a[i])
            
    #same get the data per week for GSPC 
    file_name = os.path.join(r'C:\Users','bbq59','OneDrive','2019','2019 Fall','CS 767','project','^GSPC.csv')
    df2 = pd.read_csv(file_name)
    
    b = [i for i in range(1995,2019)]   
    for i in range(len(b)):
        b[i] = df2[df.Year == b[i]]
        b[i] = b[i].groupby('Week_Number')['Return'].mean()   
        if len(b[i]) > 52:
            b[i] = b[i].drop(b[i].index[52])
        if i == 0:
            GSPC = b[0]
        else:
            GSPC = GSPC.append(b[i])  
                    
    #get the data per week for IXIC 
    file_name = os.path.join(r'C:\Users','bbq59','OneDrive','2019','2019 Fall','CS 767','project','^IXIC.csv')
    df3 = pd.read_csv(file_name)
    
    c = [i for i in range(1995,2019)]   
    for i in range(len(c)):
        c[i] = df3[df.Year == c[i]]
        c[i] = c[i].groupby('Week_Number')['Return'].mean()       
        if len(c[i]) > 52:
            c[i] = c[i].drop(c[i].index[52])
        if i == 0:
            IXIC = c[0]
        else:
            IXIC = IXIC.append(c[i])  
        
    #get the data per week for RUT 
    file_name = os.path.join(r'C:\Users','bbq59','OneDrive','2019','2019 Fall','CS 767','project','^RUT.csv')
    df4 = pd.read_csv(file_name)
    
    d = [i for i in range(1995,2019)]   
    for i in range(len(d)):
        d[i] = df4[df.Year == d[i]]
        d[i] = d[i].groupby('Week_Number')['Return'].mean() 
        if len(d[i]) > 52:
            d[i] = d[i].drop(d[i].index[52])
        if i == 0:
            RUT = d[0]
        else:
            RUT = RUT.append(d[i])         
        
 
        
        

    file_name = os.path.join(r'C:\Users','bbq59','OneDrive','2019','2019 Fall','CS 767','project','future_contract','Copper Futures Historical Data.csv')
    df5 = pd.read_csv(file_name)
    
    e = [i for i in range(1995,2019)]   
    for i in range(len(e)):
        e[i] = df5[df5.Year == e[i]]
        e[i] = e[i]['Change %']
        if len(e[i]) > 52:
            e[i] = e[i].drop(e[i].index[52])
        if i == 0:
            Copper = e[0]
        else:
            Copper = Copper.append(e[i])     
        

    file_name = os.path.join(r'C:\Users','bbq59','OneDrive','2019','2019 Fall','CS 767','project','future_contract','Crude Oil WTI Futures Historical Data.csv')
    df6 = pd.read_csv(file_name)
    
    f = [i for i in range(1995,2019)]   
    for i in range(len(f)):
        f[i] = df6[df6.Year == f[i]]
        f[i] = f[i]['Change %']
        if len(f[i]) > 52:
            f[i] = f[i].drop(f[i].index[52])
        if i == 0:
            CrudeOil = f[0]
        else:
            CrudeOil = CrudeOil.append(f[i])     
        
        

    file_name = os.path.join(r'C:\Users','bbq59','OneDrive','2019','2019 Fall','CS 767','project','future_contract','Gold Futures Historical Data.csv')
    df7 = pd.read_csv(file_name)
    
    g = [i for i in range(1995,2019)]   
    for i in range(len(g)):
        g[i] = df7[df7.Year == g[i]]
        g[i] = g[i]['Change %']
        if len(g[i]) > 52:
            g[i] = g[i].drop(g[i].index[52])
        if i == 0:
            Gold = g[0]
        else:
            Gold = Gold.append(g[i])       
            
                
    file_name = os.path.join(r'C:\Users','bbq59','OneDrive','2019','2019 Fall','CS 767','project','future_contract','Natural Gas Futures Historical Data.csv')
    df9 = pd.read_csv(file_name)
    
    j = [i for i in range(1995,2019)]   
    for i in range(len(j)):
        j[i] = df9[df9.Year == j[i]]
        j[i] = j[i]['Change %']
        if len(j[i]) > 52:
            j[i] = j[i].drop(j[i].index[52])
        if i == 0:
            Gas = j[0]
        else:
            Gas = Gas.append(j[i])           
        
    file_name = os.path.join(r'C:\Users','bbq59','OneDrive','2019','2019 Fall','CS 767','project','future_contract','Silver Futures Historical Data.csv')
    df10 = pd.read_csv(file_name)
    
    k = [i for i in range(1995,2019)]   
    for i in range(len(k)):
        k[i] = df10[df10.Year == k[i]]
        k[i] = k[i]['Change %']
        if len(k[i]) > 52:
            k[i] = k[i].drop(k[i].index[52])
        if i == 0:
            Silver = k[0]
        else:
            Silver = Silver.append(k[i])           
     
    file_name = os.path.join(r'C:\Users','bbq59','OneDrive','2019','2019 Fall','CS 767','project','future_contract','US Corn Futures Historical Data.csv')
    df11 = pd.read_csv(file_name)
    
    l = [i for i in range(1995,2019)]   
    for i in range(len(l)):
        l[i] = df11[df11.Year == l[i]]
        l[i] = l[i]['Change %']
        if len(l[i]) > 52:
            l[i] = l[i].drop(l[i].index[52])
        if i == 0:
            Corn = l[0]
        else:
            Corn = Corn.append(l[i])    

    file_name = os.path.join(r'C:\Users','bbq59','OneDrive','2019','2019 Fall','CS 767','project','future_contract','US Soybean Oil Futures Historical Data.csv')
    df12 = pd.read_csv(file_name)
    
    m = [i for i in range(1995,2019)]   
    for i in range(len(m)):
        m[i] = df12[df12.Year == m[i]]
        m[i] = m[i]['Change %']
        if len(m[i]) > 52:
            m[i] = m[i].drop(m[i].index[52])
        if i == 0:
            SoybeanOil = m[0]
        else:
            SoybeanOil = SoybeanOil.append(m[i])            
        

    #data = pd.concat([ DJI, GSPC,IXIC,RUT,Copper,CrudeOil,Gold,Gas,Silver,Corn,SoybeanOil], axis=1)
    # GSPC[i],IXIC[i],RUT[i],Copper[i],CrudeOil[i],Gold[i],Gas[i],Silver[i],Corn[i],SoybeanOil[i]

    # change all of them to list 
    DJI = DJI.values.tolist()
    GSPC = GSPC.values.tolist()
    IXIC = IXIC.values.tolist()
    RUT = RUT.values.tolist()
    Copper = Copper.values.tolist()
    CrudeOil = CrudeOil.values.tolist()
    Gold = Gold.values.tolist()
    Gas = Gas.values.tolist()
    Silver = Silver.values.tolist()
    Corn = Corn.values.tolist()
    SoybeanOil = SoybeanOil.values.tolist()
    

    # append them into one list 
    data = [[]for i in range(1248)]
    for i in range(len(data)):
        data[i].append(float(DJI[i]))
        data[i].append(float(GSPC[i]))
        data[i].append(float(IXIC[i]))
        data[i].append(RUT[i])
        data[i].append(Copper[i])
        data[i].append(CrudeOil[i])
        data[i].append(Gold[i])
        data[i].append(Gas[i])
        data[i].append(Silver[i])
        data[i].append(Corn[i]) 
        data[i].append(SoybeanOil[i])
    
    #rechange the list  to datafram and output to csv file    
    #name = ['DJI','GSPC','IXIC','RUT','Copper','CrudeOil','Gold','Gas','Silver','Corn','SoybeanOil']    
    #test=pd.DataFrame(columns=name,data=data)
    
    #input_dir = r'C:\Users\bbq59\OneDrive\2019\2019 Fall\CS 767\project'
    
    #output_file = os.path.join(input_dir,  'data.csv')        
    #test.to_csv(output_file, index=False)
        
        
except Exception as e:
    print(e)