# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:14:05 2019

@author: Xiaoqing
"""
import os
import pandas as pd
from sklearn import tree
from sklearn import metrics
from sklearn.metrics import confusion_matrix 
from stockdataclean import data 
from labelbyweeks import label
from sklearn.model_selection import train_test_split 
import numpy as np
from sklearn . naive_bayes import GaussianNB
from sklearn . ensemble import RandomForestClassifier


#use this function to print the result for classifier
try: 
    def getcf(prediction,y_test):
        
        error_rate = np.mean(prediction != y_test)
        cf = confusion_matrix(prediction,y_test)
    
        accuracy = (cf[0][0] + cf[1][1])/(cf[0][0]+cf[0][1]+cf[1][0]+cf[1][1])
        precision = cf[0][0]/(cf[0][0]+cf[1][0])
        recall = cf[0][0]/(cf[0][0]+cf[1][1])
        f1score = '{0:.2f}'.format(2 * precision * recall /(precision + recall))
        print('the result are:\n')
        print(cf)
        print('\nerror rate are:   ' + str('{0:.2f}'.format(error_rate))
              + '\naccuracy are:   ' + str('{0:.2f}'.format(accuracy)) + '\nprecision are:   ' + str('{0:.2f}'.format(precision)) +'\nrecall are:   ' 
              + str('{0:.2f}'.format(recall)) +'\nf1score are:   ' + str(f1score)+'\n')
        
        
        
    
    
except Exception as e:
    print(e)


try: 
    
    x = data
    
    y = label
    #apply split 
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size =0.1,random_state = 0 )
    #apply decision tree classifier
    tree_classifier = tree.DecisionTreeClassifier(criterion ='entropy', splitter = 'random')
    tree_classifier = tree_classifier.fit(x,y)
    prediction = tree_classifier.predict(x_test)
    print('Using decision tree classifier')
    getcf(prediction,y_test)
    
    #apply naive bayes
    NB_classifier = GaussianNB (). fit ( x_train , y_train )
    prediction2 = NB_classifier . predict ( x_test )
    
    print('\nUsing naive bayes classifier')
    getcf(prediction2,y_test)

    
    #apply random forest
    model = RandomForestClassifier ( n_estimators =100, max_depth =20,criterion ='entropy')
    model . fit ( x_train , y_train )
    prediction3 = model . predict ( x_test )
    print('Using Random Forest Classifier.')
    getcf(prediction3,y_test)
    
    
    
    
except Exception as e:
    print(e)