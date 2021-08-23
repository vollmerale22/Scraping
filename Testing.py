# -*- coding: utf-8 -*-
# Main code
"""

@author: AV
"""
import scrapy
from bs4 import BeautifulSoup
from urllib.parse import unquote
from selenium import webdriver
import requests
from requests import get
import urllib.request
import pandas as pd 
import numpy as np
from time import sleep
import time
from random import randint

   
# Document for first 100 UIDs
uids = pd.read_excel(r'C:\Users\vollm\Desktop\Random Test.xlsx', index_col=None)
contents = []

for urls in range(len(uids)):
        # Variable to store website link    
        url = 'https://www.uid.admin.ch/Detail.aspx?uid_id='+uids.loc[urls][0]
        
        # Driver executing web-search
        driver = webdriver.Chrome(executable_path=r'S:\3_Hiwi\Vollmer\Data scraping\chromedriver.exe')
        driver.get(url)
        time.sleep(10)
        page= requests.get(url)
        content = driver.page_source.encode('utf-8').strip()
        
        # Call BeautifulSoup for parsing
        soup = BeautifulSoup(page.text) #content,'html.parser')
        
        
        uid = (soup.select('#cphContent_ctl14+ .col-sm-4 div'))[0].text.strip()
        status = (soup.select('#cphContent_ctl15+ .col-sm-4 div'))[0].text.strip()
        extension = (soup.select('#cphContent_ctl16+ .col-sm-4 div'))[0].text.strip()
        name = (soup.select('#cphContent_ctl17+ .col-sm-10 div'))[0].text.strip()
        additional_name = (soup.select('#cphContent_ctl19+ .col-sm-10 div'))[0].text.strip()
        translation = (soup.select('#cphContent_ctl20+ .col-sm-10 div'))[0].text.strip()
        c_o= (soup.select('#cphContent_ctl21+ .col-sm-10 div'))[0].text.strip()
        street = (soup.select('#cphContent_ctl25+ .col-sm-10 div'))[0].text.strip()
        complement= (soup.select('#cphContent_ctl26+ .col-sm-10 div'))[0].text.strip()
        zip_town = (soup.select('#cphContent_ctl30+ .col-sm-10 div'))[0].text.strip()
        canton = (soup.select('#cphContent_ctl31+ .col-sm-4 div'))[0].text.strip()
        country = (soup.select('#cphContent_ctl32+ .col-sm-4 div'))[0].text.strip()
        municipality= (soup.select('#cphContent_ctl33+ .col-sm-4 div'))[0].text.strip()
        municipality_no= (soup.select('#cphContent_ctl34+ .col-sm-4 div'))[0].text.strip()
        egid= (soup.select('#cphContent_ctl35+ .col-sm-3 div'))[0].text.strip()
        last_validation = (soup.select('#cphContent_ctl37_datLastValidationDate div'))[0].text.strip()
        po_box= (soup.select('#cphContent_ctl38+ .col-sm-4 div'))[0].text.strip()
        zip_po = (soup.select('#cphContent_ctl42+ .col-sm-10 div'))[0].text.strip()
        legal= (soup.select('#cphContent_ctl43+ .col-sm-4 div'))[0].text.strip()
        rc_status =(soup.select('#cphContent_ctl44+ .col-sm-4 div'))[0].text.strip()
        uid_head =( soup.select('#cphContent_ctl45+ .col-sm-4 div'))[0].text.strip()
        reference=( soup.select('#cphContent_ctl47+ .col-sm-3 div'))[0].text.strip()
        vat_status = (soup.select('#cphContent_ctl48+ .col-sm-4 div'))[0].text.strip()
        vat_number= (soup.select('#cphContent_ctl49+ .col-sm-4 div'))[0].text.strip()
        start_obl =( soup.select('#cphContent_ctl50_datVATBegin div'))[0].text.strip()
        end_obl = (soup.select('#cphContent_ctl51_datVATEnd div'))[0].text.strip()
        vat_group =(soup.select('#cphContent_ctl52+ .col-sm-4 div'))[0].text.strip()
        try: 
            lei= (soup.select('#cphContent_ctl55+ .col-sm-4 div'))[0].text.strip()
            reg_status = (soup.select('#cphContent_ctl56+ .col-sm-4 div'))[0].text.strip()
            reg_date=( soup.select('#cphContent_ctl57+ .col-sm-4 div'))[0].text.strip()
            valid_until= (soup.select('#cphContent_ctl58+ .col-sm-4 div'))[0].text.strip()
        except IndexError:
            lei = ""
            reg_status = ""
            
            valid_until = ""
        
        
        
        contents.append([uid, status, extension, name, additional_name, translation, c_o, street, complement, zip_town,
                        canton, country, municipality, municipality_no, egid, last_validation,po_box,
                        zip_po,legal,rc_status,uid_head,reference,vat_status,vat_number,start_obl,end_obl,
                        lei,reg_status,reg_date,valid_until])
        
        driver.quit()
        

df = pd.DataFrame(contents)
        
       
        
        
df.to_csv(r'C:\Users\vollm\Desktop\Random Results.csv')




























#Lists
firstclass=[] #List to store the first class
secondclass=[] #List to store the second class
thirdclass=[] #List to store the third class

df = pd.DataFrame()



# Method by classes

for urls in range(len(uids)):
   
        url = 'https://www.uid.admin.ch/Detail.aspx?uid_id=CHE-100.159.411'#+uids.loc[urls][0]
        driver = webdriver.Chrome(executable_path=r'C:\Users\vollm\Downloads\chromedriver.exe')
        driver.get(url)
        time.sleep(10)
        page= requests.get(url)
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(page.text,'html.parser') #content,'html.parser')
        text = soup.get_text()
                
         
        first_class= soup.find_all("div",{"class": "col-sm-4"})
        firstdivs = []
        for div in first_class:
            firstdivs.append(div.text)
       
        #First class includes UID, status,HR status, Country , Municipality, 
        #Municipality no,Last validation, RC status, VAT status, VAT number, VAT group member, Legal form, PO box number, UID headquarter
        
        second_class= soup.find_all("div", {"class": "col-sm-10"})
       # Second class includes Name,old names, additional name, translation,c/o, Street/No., Complement, ZIP/Town, ZIP/Town of PO box,
        seconddivs=[]
        for div in second_class:
            seconddivs.append(div.text)
         
        third_class= soup.find_all("div", {"class": "col-sm-3"})
        thirddivs = []
        # Third class includes EGID, link, Commerce reference number
        for div in third_class:
           thirddivs.append(div.text)    
        
        dataframe_a= pd.DataFrame({'a': pd.Series(firstdivs)})
        dataframe_a = dataframe_a.transpose()

        dataframe_b= pd.DataFrame({'a': pd.Series(seconddivs)})
        dataframe_b = dataframe_b.transpose()

        dataframe_c= pd.DataFrame({'a': pd.Series(thirddivs)})
        dataframe_c = dataframe_c.transpose()

        merged = dataframe_a.merge(dataframe_b, left_index = True, right_index = True)
        merged = merged.merge(dataframe_c, right_index = True, left_index = True)
        
        driver.quit()
        
        
        df = df.append(merged)
        
        
df.to_csv(r'C:\Users\vollm\scraping\UIDstesting1000.csv')

#len(uids)
for urls in range(len(uids)):
    url = 'https://www.uid.admin.ch/Detail.aspx?uid_id='+uids.loc[urls][0]
    page= requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    fieldsets = soup.find_all('fieldset', class_='tab-content')
    uid_div = soup.find_all('div', 'fieldsets')
    sleep(randint(2,10))
    
       