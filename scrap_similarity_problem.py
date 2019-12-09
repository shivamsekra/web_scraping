# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 17:56:04 2019

@author: Shivam Sekra
"""

import bs4
from bs4 import BeautifulSoup
import requests
import nltk
import pandas as pd
import urllib
import re
from nltk.corpus import stopwords
nltk.download('stopwords')


df=pd.read_csv('scrap.csv')

my_list1 = df['blog_hyperlinks'][0].split(",")
my_list2 = df['blog_hyperlinks'][1].split(",")
my_list3 = df['blog_hyperlinks'][2].split(",")
my_list4 = df['blog_hyperlinks'][3].split(",")
my_list5 = df['blog_hyperlinks'][4].split(",")
my_list6 = df['blog_hyperlinks'][5].split(",")
my_list7 = df['blog_hyperlinks'][6].split(",")
my_list8 = df['blog_hyperlinks'][7].split(",")
my_list9 = df['blog_hyperlinks'][8].split(",")
my_list10 = df['blog_hyperlinks'][9].split(",")
my_list11 = df['blog_hyperlinks'][10].split(",")
my_list12 = df['blog_hyperlinks'][11].split(",")
my_list13 = df['blog_hyperlinks'][12].split(",")
my_list14 = df['blog_hyperlinks'][13].split(",")
my_list15 = df['blog_hyperlinks'][14].split(",")
my_list16 = df['blog_hyperlinks'][15].split(",")
my_list17 = df['blog_hyperlinks'][16].split(",")
my_list18 = df['blog_hyperlinks'][17].split(",")
my_list19 = df['blog_hyperlinks'][18].split(",")
my_list20 = df['blog_hyperlinks'][19].split(",")

common_words=""
percentage_similarity=""
records=[]
for i in range(len(my_list1)):
    parent_link=df['blog_link'][0]
    child_link=my_list1[i]
    records.append((parent_link,child_link,common_words,percentage_similarity))
df_new = pd.DataFrame(records, columns=['parent_link','child_link','common_words','percentage_similarity'])

common_words=""
percentage_similarity=""
records=[]
for i in range(len(my_list2)):
    parent_link=df['blog_link'][1]
    child_link=my_list2[i]
    records.append((parent_link,child_link,common_words,percentage_similarity))
df_new2 = pd.DataFrame(records, columns=['parent_link','child_link','common_words','percentage_similarity'])
df_new=df_new.append(df_new2)

common_words=""
percentage_similarity=""
records=[]
for i in range(len(my_list3)):
    parent_link=df['blog_link'][2]
    child_link=my_list3[i]
    records.append((parent_link,child_link,common_words,percentage_similarity))
df_new3 = pd.DataFrame(records, columns=['parent_link','child_link','common_words','percentage_similarity'])
df_new=df_new.append(df_new3)

common_words=""
percentage_similarity=""
records=[]
for i in range(len(my_list4)):
    parent_link=df['blog_link'][3]
    child_link=my_list4[i]
    records.append((parent_link,child_link,common_words,percentage_similarity))
df_new4 = pd.DataFrame(records, columns=['parent_link','child_link','common_words','percentage_similarity'])
df_new=df_new.append(df_new4)

common_words=""
percentage_similarity=""
records=[]
for i in range(len(my_list5)):
    parent_link=df['blog_link'][4]
    child_link=my_list5[i]
    records.append((parent_link,child_link,common_words,percentage_similarity))
df_new5= pd.DataFrame(records, columns=['parent_link','child_link','common_words','percentage_similarity'])
df_new=df_new.append(df_new5)

common_words=""
percentage_similarity=""
records=[]
for i in range(len(my_list6)):
    parent_link=df['blog_link'][5]
    child_link=my_list6[i]
    records.append((parent_link,child_link,common_words,percentage_similarity))
df_new6 = pd.DataFrame(records, columns=['parent_link','child_link','common_words','percentage_similarity'])
df_new=df_new.append(df_new6)

common_words=""
percentage_similarity=""
records=[]
for i in range(len(my_list7)):
    parent_link=df['blog_link'][6]
    child_link=my_list7[i]
    records.append((parent_link,child_link,common_words,percentage_similarity))
df_new7 = pd.DataFrame(records, columns=['parent_link','child_link','common_words','percentage_similarity'])
df_new=df_new.append(df_new7)

common_words=""
percentage_similarity=""
records=[]
for i in range(len(my_list8)):
    parent_link=df['blog_link'][7]
    child_link=my_list2[8]
    records.append((parent_link,child_link,common_words,percentage_similarity))
df_new8 = pd.DataFrame(records, columns=['parent_link','child_link','common_words','percentage_similarity'])
df_new=df_new.append(df_new8)

common_words=""
percentage_similarity=""
records=[]
for i in range(len(my_list9)):
    parent_link=df['blog_link'][8]
    child_link=my_list9[i]
    records.append((parent_link,child_link,common_words,percentage_similarity))
df_new9 = pd.DataFrame(records, columns=['parent_link','child_link','common_words','percentage_similarity'])
df_new=df_new.append(df_new9)

common_words=""
percentage_similarity=""
records=[]
for i in range(len(my_list10)):
    parent_link=df['blog_link'][9]
    child_link=my_list10[i]
    records.append((parent_link,child_link,common_words,percentage_similarity))
df_new10 = pd.DataFrame(records, columns=['parent_link','child_link','common_words','percentage_similarity'])
df_new=df_new.append(df_new10)

common_words=""
percentage_similarity=""
records=[]
for i in range(len(my_list11)):
    parent_link=df['blog_link'][10]
    child_link=my_list11[i]
    records.append((parent_link,child_link,common_words,percentage_similarity))
df_new11 = pd.DataFrame(records, columns=['parent_link','child_link','common_words','percentage_similarity'])
df_new=df_new.append(df_new11)

common_words=""
percentage_similarity=""
records=[]
for i in range(len(my_list12)):
    parent_link=df['blog_link'][11]
    child_link=my_list12[i]
    records.append((parent_link,child_link,common_words,percentage_similarity))
df_new12 = pd.DataFrame(records, columns=['parent_link','child_link','common_words','percentage_similarity'])
df_new=df_new.append(df_new12)

common_words=""
percentage_similarity=""
records=[]
for i in range(len(my_list13)):
    parent_link=df['blog_link'][12]
    child_link=my_list13[i]
    records.append((parent_link,child_link,common_words,percentage_similarity))
df_new13 = pd.DataFrame(records, columns=['parent_link','child_link','common_words','percentage_similarity'])
df_new=df_new.append(df_new13)

common_words=""
percentage_similarity=""
records=[]
for i in range(len(my_list14)):
    parent_link=df['blog_link'][13]
    child_link=my_list14[i]
    records.append((parent_link,child_link,common_words,percentage_similarity))
df_new14 = pd.DataFrame(records, columns=['parent_link','child_link','common_words','percentage_similarity'])
df_new=df_new.append(df_new14)


common_words=""
percentage_similarity=""
records=[]
for i in range(len(my_list15)):
    parent_link=df['blog_link'][14]
    child_link=my_list15[i]
    records.append((parent_link,child_link,common_words,percentage_similarity))
df_new15 = pd.DataFrame(records, columns=['parent_link','child_link','common_words','percentage_similarity'])
df_new=df_new.append(df_new15)

common_words=""
percentage_similarity=""
records=[]
for i in range(len(my_list16)):
    parent_link=df['blog_link'][15]
    child_link=my_list16[i]
    records.append((parent_link,child_link,common_words,percentage_similarity))
df_new16 = pd.DataFrame(records, columns=['parent_link','child_link','common_words','percentage_similarity'])
df_new=df_new.append(df_new16)

common_words=""
percentage_similarity=""
records=[]
for i in range(len(my_list17)):
    parent_link=df['blog_link'][16]
    child_link=my_list17[i]
    records.append((parent_link,child_link,common_words,percentage_similarity))
df_new17 = pd.DataFrame(records, columns=['parent_link','child_link','common_words','percentage_similarity'])
df_new=df_new.append(df_new17)

common_words=""
percentage_similarity=""
records=[]
for i in range(len(my_list18)):
    parent_link=df['blog_link'][17]
    child_link=my_list18[i]
    records.append((parent_link,child_link,common_words,percentage_similarity))
df_new18= pd.DataFrame(records, columns=['parent_link','child_link','common_words','percentage_similarity'])
df_new=df_new.append(df_new18)

common_words=""
percentage_similarity=""
records=[]
for i in range(len(my_list19)):
    parent_link=df['blog_link'][18]
    child_link=my_list19[i]
    records.append((parent_link,child_link,common_words,percentage_similarity))
df_new19 = pd.DataFrame(records, columns=['parent_link','child_link','common_words','percentage_similarity'])
df_new=df_new.append(df_new19)

common_words=""
percentage_similarity=""
records=[]
for i in range(len(my_list20)):
    parent_link=df['blog_link'][19]
    child_link=my_list20[i]
    records.append((parent_link,child_link,common_words,percentage_similarity))
df_new20 = pd.DataFrame(records, columns=['parent_link','child_link','common_words','percentage_similarity'])
df_new=df_new.append(df_new20)

df_new.reset_index(drop=True,inplace=True)
df_new


parent=df_new.parent_link[5]
child=df_new.child_link[5]

source1 = requests.get(parent)
source2 = requests.get(child)
soup1=BeautifulSoup(source1.content,'html.parser')
soup2=BeautifulSoup(source2.content,'html.parser')

first1=soup1.find(class_="main-content")
blog_content1=""
for paragraph in first1.find_all('p'):
        blog_content1 += paragraph.text

first2=soup2.find(class_="main-content")
blog_content2=""
for paragraph in first2.find_all('p'):
        blog_content2 += paragraph.text

import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
  
# X = input("Enter first string: ").lower() 
# Y = input("Enter second string: ").lower() 
X =blog_content1
Y =blog_content2
  
# tokenization 
X_list = word_tokenize(X)  
Y_list = word_tokenize(Y) 
  
# sw contains the list of stopwords 
sw = stopwords.words('english')  
l1 =[];l2 =[] 
  
# remove stop words from string 
X_set = {w for w in X_list if not w in sw}  
Y_set = {w for w in Y_list if not w in sw} 
  
# form a set containing keywords of both strings  
rvector = X_set.union(Y_set)  
for w in rvector: 
    if w in X_set: l1.append(1) # create a vector 
    else: l1.append(0) 
    if w in Y_set: l2.append(1) 
    else: l2.append(0) 
c = 0
  
# cosine formula  
for i in range(len(rvector)): 
        c+= l1[i]*l2[i] 
cosine = c / float((sum(l1)*sum(l2))**0.5) 

df_new.common_words[5]=rvector
df_new.percentage_similarity[5]=cosine















parent=df_new.parent_link[50]
child=df_new.child_link[50]

source1 = requests.get(parent)
source2 = requests.get(child)
soup1=BeautifulSoup(source1.content,'html.parser')
soup2=BeautifulSoup(source2.content,'html.parser')

first1=soup1.find(class_="main-content")
blog_content1=""
for paragraph in first1.find_all('p'):
        blog_content1 += paragraph.text

first2=soup2.find(class_="main-content")
blog_content2=""
for paragraph in first2.find_all('p'):
        blog_content2 += paragraph.text

import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
  
# X = input("Enter first string: ").lower() 
# Y = input("Enter second string: ").lower() 
X =blog_content1
Y =blog_content2
  
# tokenization 
X_list = word_tokenize(X)  
Y_list = word_tokenize(Y) 
  
# sw contains the list of stopwords 
sw = stopwords.words('english')  
l1 =[];l2 =[] 
  
# remove stop words from string 
X_set = {w for w in X_list if not w in sw}  
Y_set = {w for w in Y_list if not w in sw} 
  
# form a set containing keywords of both strings  
rvector = X_set.union(Y_set)  
for w in rvector: 
    if w in X_set: l1.append(1) # create a vector 
    else: l1.append(0) 
    if w in Y_set: l2.append(1) 
    else: l2.append(0) 
c = 0
  
# cosine formula  
for i in range(len(rvector)): 
        c+= l1[i]*l2[i] 
cosine = c / float((sum(l1)*sum(l2))**0.5) 

df_new.common_words[50]=rvector
df_new.percentage_similarity[50]=cosine



parent=df_new.parent_link[51]
child=df_new.child_link[51]

source1 = requests.get(parent)
source2 = requests.get(child)
soup1=BeautifulSoup(source1.content,'html.parser')
soup2=BeautifulSoup(source2.content,'html.parser')

first1=soup1.find(class_="main-content")
blog_content1=""
for paragraph in first1.find_all('p'):
        blog_content1 += paragraph.text

first2=soup2.find(class_="main-content")
blog_content2=""
for paragraph in first2.find_all('p'):
        blog_content2 += paragraph.text

import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
  
# X = input("Enter first string: ").lower() 
# Y = input("Enter second string: ").lower() 
X =blog_content1
Y =blog_content2
  
# tokenization 
X_list = word_tokenize(X)  
Y_list = word_tokenize(Y) 
  
# sw contains the list of stopwords 
sw = stopwords.words('english')  
l1 =[];l2 =[] 
  
# remove stop words from string 
X_set = {w for w in X_list if not w in sw}  
Y_set = {w for w in Y_list if not w in sw} 
  
# form a set containing keywords of both strings  
rvector = X_set.union(Y_set)  
for w in rvector: 
    if w in X_set: l1.append(1) # create a vector 
    else: l1.append(0) 
    if w in Y_set: l2.append(1) 
    else: l2.append(0) 
c = 0
  
# cosine formula  
for i in range(len(rvector)): 
        c+= l1[i]*l2[i] 
cosine = c / float((sum(l1)*sum(l2))**0.5) 

df_new.common_words[51]=rvector
df_new.percentage_similarity[51]=cosine






















parent=df_new.parent_link[85]
child=df_new.child_link[85]

source1 = requests.get(parent)
source2 = requests.get(child)
soup1=BeautifulSoup(source1.content,'html.parser')
soup2=BeautifulSoup(source2.content,'html.parser')

first1=soup1.find(class_="main-content")
blog_content1=""
for paragraph in first1.find_all('p'):
        blog_content1 += paragraph.text

first2=soup2.find(class_="main-content")
blog_content2=""
for paragraph in first2.find_all('p'):
        blog_content2 += paragraph.text

import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
  
# X = input("Enter first string: ").lower() 
# Y = input("Enter second string: ").lower() 
X =blog_content1
Y =blog_content2
  
# tokenization 
X_list = word_tokenize(X)  
Y_list = word_tokenize(Y) 
  
# sw contains the list of stopwords 
sw = stopwords.words('english')  
l1 =[];l2 =[] 
  
# remove stop words from string 
X_set = {w for w in X_list if not w in sw}  
Y_set = {w for w in Y_list if not w in sw} 
  
# form a set containing keywords of both strings  
rvector = X_set.union(Y_set)  
for w in rvector: 
    if w in X_set: l1.append(1) # create a vector 
    else: l1.append(0) 
    if w in Y_set: l2.append(1) 
    else: l2.append(0) 
c = 0
  
# cosine formula  
for i in range(len(rvector)): 
        c+= l1[i]*l2[i] 
cosine = c / float((sum(l1)*sum(l2))**0.5) 

df_new.common_words[85]=rvector
df_new.percentage_similarity[85]=cosine















parent=df_new.parent_link[149]
child=df_new.child_link[149]

source1 = requests.get(parent)
source2 = requests.get(child)
soup1=BeautifulSoup(source1.content,'html.parser')
soup2=BeautifulSoup(source2.content,'html.parser')

first1=soup1.find(class_="main-content")
blog_content1=""
for paragraph in first1.find_all('p'):
        blog_content1 += paragraph.text

first2=soup2.find(class_="main-content")
blog_content2=""
for paragraph in first2.find_all('p'):
        blog_content2 += paragraph.text

import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
  
# X = input("Enter first string: ").lower() 
# Y = input("Enter second string: ").lower() 
X =blog_content1
Y =blog_content2
  
# tokenization 
X_list = word_tokenize(X)  
Y_list = word_tokenize(Y) 
  
# sw contains the list of stopwords 
sw = stopwords.words('english')  
l1 =[];l2 =[] 
  
# remove stop words from string 
X_set = {w for w in X_list if not w in sw}  
Y_set = {w for w in Y_list if not w in sw} 
  
# form a set containing keywords of both strings  
rvector = X_set.union(Y_set)  
for w in rvector: 
    if w in X_set: l1.append(1) # create a vector 
    else: l1.append(0) 
    if w in Y_set: l2.append(1) 
    else: l2.append(0) 
c = 0
  
# cosine formula  
for i in range(len(rvector)): 
        c+= l1[i]*l2[i] 
cosine = c / float((sum(l1)*sum(l2))**0.5) 

df_new.common_words[149]=rvector
df_new.percentage_similarity[149]=cosine

fi = []
fi.append(df_new.iloc[5,:])
fi.append(df_new.iloc[50,:])
fi.append(df_new.iloc[51,:])
fi.append(df_new.iloc[85,:])
fi.append(df_new.iloc[149,:])
df_final=pd.DataFrame(fi, columns=['parent_link','child_link','common_words','percentage_similarity'])
df_final.reset_index(inplace=True,drop=True)
df_new.to_csv('parent_child.csv')
df_final.to_csv('similarity_with_parent_child.csv')

