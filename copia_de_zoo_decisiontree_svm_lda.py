# -*- coding: utf-8 -*-
"""Copia de Zoo_DecisionTree_SVM_LDA

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jCJyYQpKVvP_-ZCHsM2i3EeO9dACOp7r
"""

#En este Projecto se utiliza una base de datos  https://archive.ics.uci.edu/ml/datasets/zoo
 # Con Informacion de 7 clases distintas de animales, sin valores faltantes, 101 Instances, 14 atributos.

 #El objetivo de este proyecto es utilizar clasificadores para identificar los animales dentro de la base de datos.

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from sklearn.metrics import confusion_matrix,accuracy_score, classification_report, roc_curve



#Subimos base de datos 
df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/zoo/zoo.data',header=None)
#df=pd.read_csv('zoo.data',header=None)
df.head(5) # Muestra

head_df = ['animal','hair',  'feathers' , 'eggs' , 'milk',  'airborne' , 'aquatic',  'predator' ,'toothed','backbone', 'breathes'	, 'venomous', 'fins',	'legs','tail' ,'domestic'	,'catsize', 'Type']

for col in df.columns: 
   df.rename({col: head_df[col] }, axis=1, inplace=True)

df.head()

X1=df.iloc[:,1:-1]
Y1=df.iloc[:,-1]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X1, Y1, test_size=0.7,random_state= 27)

from sklearn.tree import DecisionTreeClassifier

Tree = DecisionTreeClassifier()
Tree.fit(x_train, y_train)

predic = Tree.predict(x_test)

print('accuracy  =', accuracy_score(y_test, predic))
print(classification_report(y_test, predic))
pd.crosstab(y_test, predic, rownames=['True'], colnames=['Predicted'], margins=True)

### SVM

from sklearn.svm import SVC

SVM = SVC(degree=1 , kernel="poly",probability=True)
SVM.fit(x_train,y_train)
predic = SVM.predict(x_test)

print('accuracy  =', accuracy_score(y_test, predic))
print(classification_report(y_test, predic))
pd.crosstab(y_test, predic, rownames=['True'], colnames=['Predicted'], margins=True)

## LDA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

lda = LinearDiscriminantAnalysis(n_components=2)
lda.fit(x_train, y_train)

predic = lda.predict(x_test)

print('accuracy  =', accuracy_score(y_test, predic))
print(classification_report(y_test, predic))
pd.crosstab(y_test, predic, rownames=['True'], colnames=['Predicted'], margins=True)