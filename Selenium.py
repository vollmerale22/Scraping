# -*- coding: utf-8 -*-
# Main code
"""

@author: AV
Method using Selenium and BeautifulSoup
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

   
# Document for UIDs
uids = pd.read_excel(r'S:\3_Hiwi\Vollmer\Scraping\List_of_UIDs_sorted.xlsx', index_col=None)
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
        
        try: 
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
            lei= (soup.select('#cphContent_ctl55+ .col-sm-4 div'))[0].text.strip()
            reg_status = (soup.select('#cphContent_ctl56+ .col-sm-4 div'))[0].text.strip()
            reg_date=(soup.select('#cphContent_ctl57+ .col-sm-4 div'))[0].text.strip()
            valid_until= (soup.select('#cphContent_ctl58+ .col-sm-4 div'))[0].text.strip()
        except IndexError:
            pass
        continue
        
        
        
        contents.append([uid, status, extension, name, additional_name, translation, c_o, street, complement, zip_town,
                        canton, country, municipality, municipality_no, egid, last_validation,po_box,
                        zip_po,legal,rc_status,uid_head,reference,vat_status,vat_number,start_obl,end_obl,
                        lei,reg_status,reg_date,valid_until])
        
        driver.quit()
        

df = pd.DataFrame(contents)
        
       
        
        
df.to_csv(r'S:\3_Hiwi\Vollmer\Scraping\Results\Results.csv')
                
  
