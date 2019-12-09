# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:13:16 2019

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

source_main1 = requests.get('https://www.hackerearth.com/blog/machine-learning/')
soup=BeautifulSoup(source_main1.content,'html.parser')
first=soup.find(class_="row blog-content-block")
links = first.find_all('a',attrs={'title':['Object detection for self-driving cars','Introduction to Object Detection','Data Visualization for Beginners-Part 3','Composing Jazz Music with Deep Learning','Data visualization for beginners – Part 2','Data visualization for beginners – Part 1','11 open source frameworks for AI and machine learning models','Leverage machine learning to amplify your social impact','Artificial  Intelligence 101: How to get started']})
records = []
for i in range(0,9):
    final = links[i].get('href')
      
    source = requests.get(final)
    soup=BeautifulSoup(source.content,'html.parser')
    blog=soup.find(class_="entry-content")
    blog_tit=blog.find(class_="entry-title")
    blog_title=blog_tit.text
    blog_content=""
    for paragraph in blog.find_all('p'):
        blog_content += paragraph.text
    comments=soup.find(id="thread__container")
    blog_questions=''
    blog_subheading=""
    for paragraph in blog.find_all('h2'):
        blog_subheading = blog_subheading+paragraph.text+','
        
    hyplinks=blog.find_all('a')    
    blog_hyperlinks=""
    for hyplink in hyplinks:
        blog_hyperlinks = blog_hyperlinks+hyplink.get('href')+','
    
    blog_link=final
    
    records.append((blog_title,blog_link,blog_content,blog_questions,blog_subheading,blog_hyperlinks))
df = pd.DataFrame(records, columns=['blog_title','blog_link','blog_content','blog_questions','blog_subheading','blog_hyperlinks'])

source_main2 = requests.get('https://intellipaat.com/blog/tutorial/machine-learning-tutorial/')
soup2=BeautifulSoup(source_main2.content,'html.parser')
first2=soup2.find(class_="blog-left")
links2=first2.find_all('a')
records2 = []
for i in range(0,11):
    final2 = links2[i].get('href')
   
     
    source2 = requests.get(final2)
    soup2=BeautifulSoup(source2.content,'html.parser')
    blog2=soup2.find(class_="blog-content-box clearfix")
   
    blog_tit=blog2.find('h2')
    blog_title=blog_tit.text
   
    blog_content=""
    for paragraph in blog2.find_all('p'):
        blog_content += paragraph.text
       
    comments2=soup2.find(class_="faq_tutorial_inner")
    blog_questions = ""
    '''for paragraph in comments2.find_all('h3'):
        blog_questions = blog_questions+paragraph.text+','
    '''
    
    

   
   
    blog_subheading= ""
    for paragraph in blog2.find_all('h2'):
        blog_subheading = blog_subheading+paragraph.text+','
       
    hyplinks=blog2.find_all('a')    
    blog_hyperlinks=""
    for hyplink in hyplinks:
        blog_hyperlinks = blog_hyperlinks+hyplink.get('href')+','
   
    blog_link=final
   
    records2.append((blog_title,blog_link,blog_content,blog_questions,blog_subheading,blog_hyperlinks))
df2 = pd.DataFrame(records2, columns=['blog_title','blog_link','blog_content','blog_questions','blog_subheading','blog_hyperlinks'])

df=df.append(df2)
df.reset_index(drop=True,inplace=True)
df.to_csv('scrap.csv')