# -*- coding: utf-8 -*-
"""
Created on Mon May 17 12:46:52 2021

@author: AV
"""
import scrapy
import document
from bs4 import BeautifulSoup
from urllib.parse import unquote
from selenium import webdriver
import requests
from requests import get
import urllib.request
import pandas as pd 
import numpy as np
from time import sleep
from random import randint

# Document for first 100 UIDs
uids = pd.read_csv(r'C:\Users\vollm\scraping\UIDlist - Copy.csv', index_col=None)





#### Brute force method ####

UID=[] #List to store the UID
status=[] #List to store status of company
extension=[] #List to store UID extension
name = [] # Legal name of company
additional_name = [] # Additional name
old_name = []
translation = []
c_o = []
address = [] # Street/No.
complement = []
zip = [] # ZIP and Town
canton= [] # List to store canton
country = [] # List to store canton
municipality = [] # List to store municipality
municipality_no = [] # List to store municipality number
EGID = [] # List to store EGID
validation = [] # List to store last validation
PO_number = []
ZIP_PO = []
legal = [] # List to store legal form 
RC_status = [] # List to store RC status
uid_headquarter = []
reference = [] # List to store reference number
VAT_register_status = [] # List to store VAT register status
VAT_number = [] # List to store VAT number 
VAT_start_of_obligation =[]
VAT_end_of_obligation = [] # Start of obligation 

df = pd.DataFrame()
#len(uids)
for urls in range(len(uids)):
    url = 'https://www.uid.admin.ch/Detail.aspx?uid_id='+uids.loc[urls][0]
    page= requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    fieldsets = soup.find_all('fieldset', class_='tab-content')
    uid_div = soup.find_all('div', 'fieldsets')
    sleep(randint(2,10))
    for fieldset in fieldsets:
        UID_ID= soup.find(id="cphContent_ctl14")
        UIDs = UID_ID.div.find('div', class_ = 'col-sm-4').text
        UID.append(UIDs)
        
        stat_ID = soup.find(id="cphContent_ctl14")
        stat = stat_ID.div.find('div', class_ = 'col-sm-4').text
        status.append(stat)
        
        extension_ID = soup.find(id="cphContent_ctl16")
        extensions=fieldset.div.find('div', class_ = 'col-sm-4').text
        extension.append(extensions)
        
        name_ID = soup.find(id="cphContent_ctl17")
        names = fieldset.div.find('div', class_ = 'col-sm-10').text
        name.append(names)
        
        old_name_ID = soup.find(id="cphContent_ctl18")
        old_names = old_name_ID.div.find('div', class_ = 'col-sm-10').text
        old_name.append(old_names)
        
        additional_name_ID = soup.find(id="cphContent_ctl19")
        additional_names = fieldset.div.find('div', class_='col-sm-10') if fieldset.div.find('div', class_='col-sm-10') else '-'
        additional_name.append(additional_names) 
        
        translation_ID = soup.find(id="cphContent_ctl20")
        translations = fieldset.div.find('div', class_='col-sm-10') if fieldset.div.find('div', class_='col-sm-10') else '-'
        translation.append(translations) 
        
        c_o_ID = soup.find(id="cphContent_ctl21")
        c_os = additional_names = fieldset.div.find('div', class_='col-sm-10') if fieldset.div.find('div', class_='col-sm-10') else '-'
        c_o.append(c_os) 
        
        address_ID = soup.find(id="cphContent_ctl25")
        address_uid = fieldset.div.find('div', class_ = 'col-sm-10').text
        address.append(address_uid)
        
        complement_ID = soup.find(id="cphContent_ctl26")
        complements = fieldset.div.find('div', class_='col-sm-10') if fieldset.div.find('div', class_='col-sm-10') else '-'
        complement.append(complements) 
        
        zipcode_ID = soup.find(id="cphContent_ctl30")
        zipcode = fieldset.div.find('div', class_ = 'col-sm-10').text
        zip.append(zipcode)
        
        cantons_ID = soup.find(id="cphContent_ctl31")
        cantons= fieldset.div.find('div', class_ = 'col-sm-4').text
        canton(cantons) 
        
        countries_ID = soup.find(id="cphContent_ctl32")
        countries = fieldset.div.find('div', class_ = 'col-sm-4').text
        country.append(countries) 
        
        municipalities_ID = soup.find(id="cphContent_ctl33")
        municipalities = fieldset.div.find('div', class_ = 'col-sm-4').text
        municipality.append(municipalities) 
        
        municipality_no_ID = soup.find(id="cphContent_ctl34")
        municipality_nos = fieldset.div.find('div', class_ = 'col-sm-4').text
        municipality_no.append(municipality_nos) 
        
        EGID_ID = soup.find(id="cphContent_ctl35")
        EGIDs = fieldset.div.find('div', class_ = 'col-sm-3').text
        EGID.append(EGIDs) 
        
        validations_ID = soup.find(id="cphContent_ctl37")
        validations = fieldset.div.find('div', class_ = 'col-sm-4 input-append date').text
        validation.append(validations) 
        
        PO_numbers = soup.find(id="cphContent_ctl38")
        PO_numbers = fieldset.div.find('div', class_='col-sm-4') if fieldset.div.find('div', class_='col-sm-4') else '-'
        PO_number.append(PO_numbers) 
        
        ZIP_POs = soup.find(id="cphContent_ctl42")
        ZIP_POs = fieldset.div.find('div', class_ = 'col-sm-10').text
        ZIP_PO.append(ZIP_POs)
        
        Legal_ID = soup.find(id="cphContent_ctl43")
        legal_status = fieldset.div.find('div', class_ = 'col-sm-4').text
        legal.append(legal_status)
        
        RC_ID = soup.find(id="cphContent_ctl44")
        RC = fieldset.div.find('div', class_ = 'col-sm-4').text
        RC_status.append(RC)
         
        uid_headquarters_ID = soup.find(id="cphContent_ctl45")
        uid_headquarters = fieldset.div.find('div', class_='col-sm-4') if fieldset.div.find('div', class_='col-sm-4') else '-'
        uid_headquarter.append(uid_headquarters) 
        
        reference_no = soup.find(id="cphContent_ctl47")
        reference_no = fieldset.div.find('div', class_ = 'col-sm-3').text
        reference.append(reference_no)
         
        VAT_status_ID = soup.find(id="cphContent_ctl48")
        VAT_status = fieldset.div.find('div', class_ = 'col-sm-4').text
        VAT_register_status.append(VAT_status)
        
        VAT_number_ID = soup.find(id="cphContent_ctl49")
        VAT_numbers = fieldset.div.find('div', class_ = 'col-sm-4').text
        VAT_number.append(VAT_numbers)
        
        VAT_start_ID= soup.find(id="cphContent_ctl50")
        VAT_start =fieldset.div.find('div', class_ = 'col-sm-4 input-append date').text
        VAT_start_of_obligation.append(VAT_start)
        
        VAT_end_ID = soup.find(id="cphContent_ctl51")
        VAT_end = fieldset.div.find('div', class_='col-sm-4 input-append date') if fieldset.div.find('div', class_='col-sm-4 input-append date') else '-'
        VAT_end_of_obligation.append(VAT_end) 

df_test = pd.DataFrame({'UID': UID,'Status': status,'Extension':extension,'Name': name,'Additional name':additional_name,'Translation':translation,'C/o':c_o,'Address':address, 'Complement':complement,'ZIP':zip,'Canton':canton,'Country': country, 'Municipality':municipality,
                          'Municipality_no':municipality_no,'EGID': EGID,'Last validation': validation, 'PO number': PO_number, 'ZIP PO Box' : ZIP_PO, 'Legal form':legal, 'RC status': RC_status,'UID Headquarters':  uid_headquarter, 'Register reference': reference, 
                          'VAT register status': VAT_register_status, 'VAT number': VAT_number, 'Start of obligation VAT':VAT_start_of_obligation, 'End of obligation VAT':VAT_end_of_obligation})
df_test.to_csv(r'C:\Users\vollm\scraping\UIDtest.csv')

            


####### Dynamic approach - not finished - not used ######

def getTag(tagName, attr):
    tags = tagName.split(" ")
    for tag in tags:
        if(tag.startswith(attr)):
            return getTagValue(tag)

def getTagValue(tag):
    begin = tag.find('"')
    end = tag[begin + 1:].find('"')
    href = tag[begin + 1: end + begin + 1]
    return getURL(href)
	
def getURL(href):
    begin = href.find("'")
    end = href[begin + 1:].find("'")
    return href[begin + 1: end + begin + 1]	
	
def getData(cssID, soup):
    data = soup.find(id=cssID)
    if(data is not None):
        return data.text #to extract the text without html tags
    else:
        return ''

	
# Function to get Form Data
def getFormData(val, response):
    return {
        'ctl00$ScriptManager': 'ctl00$cphContent$btnSearch' + val,
        '__EVENTTARGET': val, 
        '__EVENTARGUMENT': '',
        'VST': val,
        '__VIEWSTATE': unquote(response.css('input#__VIEWSTATE::attr(value)').extract_first()),
        '_EVENTVALIDATION': unquote(response.css('input#_EVENTVALIDATION::attr(value)').extract_first()),
        '__VIEWSTATEGENERATOR': unquote(response.css("input#__VIEWSTATEGENERATOR::attr(value)").extract_first()),
        '__VIEWSTATEENCRYPTED': '',
        'ctl00$cphContent$hidSelectedSearchMode': '',
        '__ASYNCPOST': 'true'
    }
	
class UIDSpider(scrapy.Spider):
    name = 'web_spider'
    start_urls = ["https://www.uid.admin.ch/Detail.aspx?uid_id=CHE-105.909.036&ehra_id=126286"]
    custom_settings = {
        'FEED_URI': 'file://%(data_dir_path)s/scraped-data.csv',
        'FEED_FORMAT': 'csv',
        'HTTPCACHE_ENABLED': True,
        'POSTSTATS_INTERVAL': 200
    }

    def __init__(self, data_dir_path='C:/Users/vollm/Desktop/web-scraper/web-scraper/data', raw_dir_path='C:/Users/vollm/Desktop/web-scraper/web-scraper/data', url=None, *a, **kw):
        self.data_dir_path = data_dir_path
        self.url = url
        super(UIDSpider, self).__init__(*a, **kw)

    def parse(self, response):
        for name in response.css("#ctl00_cphContent_gridSearchresult_ctl00_ctl04_btnDetails").extract():
            val = unquote(getTag(name, "href"))
#This method reads the response object and creates a FormRequest that automatically includes all the pre-filled values from the form, along with the hidden ones.
            yield scrapy.FormRequest(
                'https://www.uid.admin.ch/Detail.aspx?uid_id=CHE-105.909.036&ehra_id=126286',
                formdata=getFormData(val, response),
                callback=self.parse_content
            )

    def parse_status(self, response):
        for status in response.css("#ctl00_cphContent_gridSearchresult_ctl00_ctl04_btnDetails").extract():
            val = unquote(getTag(status, "href"))

            yield scrapy.FormRequest(
                'https://www.uid.admin.ch/Detail.aspx?uid_id=CHE-105.909.036&ehra_id=126286',
                formdata=getFormData(val, response),
                callback=self.parse_uid
            )

    def parse_uid(self, response):
        for uid in response.css('#ctl00_cphContent_gridSearchresult_ctl00_ctl04_btnDetails"').extract():
            val = unquote(getTag(uid, "href"))
			
            yield scrapy.FormRequest(
                'https://www.uid.admin.ch/Detail.aspx?uid_id=CHE-105.909.036&ehra_id=126286',
                formdata=getFormData(val, response),
                callback=self.parse_sum
            )
	
    def parse_sum(self, response):
        all_sum = response.css("#ctl00_cphContent_gridSearchresult_ctl00_ctl04_btnDetails").extract()
        
        company= response.css("#ctl00_cphContent_gridSearchresult_ctl00_ctl04_btnDetails").extract_first()
        status = response.css("#ctl00_cphContent_gridSearchresult_ctl00_ctl04_btnDetails").extract_first()
        uid = response.css("#ctl00_cphContent_gridSearchresult_ctl00_ctl04_btnDetails").extract_first()

        soup = BeautifulSoup(response.text, 'html.parser') #parse the html, that is, take the raw html text (response.text) and break it into Python objects. The second argument is the html parser

        for (i, sum) in enumerate(all_sum):
            
            yield{
                'Company name': company,
                'Status': status,
                'UID': uid,
                'sum': getData("cphContent_ctl21_txtCareOf" + str(i), soup),
                'Address': getData("cphContent_ctl25_lbl_txtStreetReadonly" + str(i), soup),
                'ZIP': getData("cphContent_ctl14_txtPostcode" + str(i), soup),
                'Canton': getData("cphContent_ctl17_lbl_ddlCanton_" + str(i), soup),
                'Country': getData("cphContent_ctl32_lbl_ddlCountry" + str(i), soup),
                'Municipality': getData("cphContent_ctl33_lentxtCommunityName" + str(i), soup),
                'Municipaility No.': getData("cphContent_ctl34_txtCommunityId" + str(i), soup),
                'EGID': getData("cphContent_ctl35_txtEGID" + str(i), soup),
                'Legal form': getData("cphContent_ctl43_ddlLegalform" + str(i), soup),
                'RC Status': getData("cphContent_ctl44_ddlHRStatus" + str(i), soup),
                'VAT number': getData("cphContent_ctl48_ddlVATStatus" + str(i), soup),
            }
            
            
            
# Document for first 100 UIDs
uids = pd.read_csv(r'C:\Users\vollm\scraping\UIDlist - Copy.csv', index_col=None)





#### Brute force method ####

UID=[] #List to store the UID
status=[] #List to store status of company
extension=[] #List to store UID extension
name = [] # Legal name of company
additional_name = [] # Additional name
old_name = []
translation = []
c_o = []
address = [] # Street/No.
complement = []
zip = [] # ZIP and Town
canton= [] # List to store canton
country = [] # List to store canton
municipality = [] # List to store municipality
municipality_no = [] # List to store municipality number
EGID = [] # List to store EGID
validation = [] # List to store last validation
PO_number = []
ZIP_PO = []
legal = [] # List to store legal form 
RC_status = [] # List to store RC status
uid_headquarter = []
reference = [] # List to store reference number
VAT_register_status = [] # List to store VAT register status
VAT_number = [] # List to store VAT number 
VAT_start_of_obligation =[]
VAT_end_of_obligation = [] # Start of obligation


url = 'https://www.uid.admin.ch/Detail.aspx?uid_id=CHE100000012'
page= requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
fieldsets = soup.find_all("fieldset")
 #sleep(randint(2,10))
for fieldset in fieldsets:
        UID_ID= soup.find(id="cphContent_ctl14")
        UIDs = UID_ID.find('div', class_ = 'col-sm-4').text
        UID.append(UIDs)
        
        stat_ID = soup.find(id="cphContent_ctl14")
        stat = stat_ID.div.find('div', class_ = 'col-sm-4').text
        status.append(stat)
        
        extension_ID = soup.find(id="cphContent_ctl16")
        extensions=fieldset.div.find('div', class_ = 'col-sm-4').text
        extension.append(extensions)
        
        name_ID = soup.find(id="cphContent_ctl17")
        names = fieldset.div.find('div', class_ = 'col-sm-10').text
        name.append(names)
        
        old_name_ID = soup.find(id="cphContent_ctl18")
        old_names = old_name_ID.div.find('div', class_ = 'col-sm-10').text
        old_name.append(old_names)
        
        additional_name_ID = soup.find(id="cphContent_ctl19")
        additional_names = fieldset.div.find('div', class_='col-sm-10') if fieldset.div.find('div', class_='col-sm-10') else '-'
        additional_name.append(additional_names) 
        
        translation_ID = soup.find(id="cphContent_ctl20")
        translations = fieldset.div.find('div', class_='col-sm-10') if fieldset.div.find('div', class_='col-sm-10') else '-'
        translation.append(translations) 
        
        c_o_ID = soup.find(id="cphContent_ctl21")
        c_os = additional_names = fieldset.div.find('div', class_='col-sm-10') if fieldset.div.find('div', class_='col-sm-10') else '-'
        c_o.append(c_os) 
        
        address_ID = soup.find(id="cphContent_ctl25")
        address_uid = fieldset.div.find('div', class_ = 'col-sm-10').text
        address.append(address_uid)
        
        complement_ID = soup.find(id="cphContent_ctl26")
        complements = fieldset.div.find('div', class_='col-sm-10') if fieldset.div.find('div', class_='col-sm-10') else '-'
        complement.append(complements) 
        
        zipcode_ID = soup.find(id="cphContent_ctl30")
        zipcode = fieldset.div.find('div', class_ = 'col-sm-10').text
        zip.append(zipcode)
        
        cantons_ID = soup.find(id="cphContent_ctl31")
        cantons= fieldset.div.find('div', class_ = 'col-sm-4').text
        canton(cantons) 
        
        countries_ID = soup.find(id="cphContent_ctl32")
        countries = fieldset.div.find('div', class_ = 'col-sm-4').text
        country.append(countries) 
        
        municipalities_ID = soup.find(id="cphContent_ctl33")
        municipalities = fieldset.div.find('div', class_ = 'col-sm-4').text
        municipality.append(municipalities) 
        
        municipality_no_ID = soup.find(id="cphContent_ctl34")
        municipality_nos = fieldset.div.find('div', class_ = 'col-sm-4').text
        municipality_no.append(municipality_nos) 
        
        EGID_ID = soup.find(id="cphContent_ctl35")
        EGIDs = fieldset.div.find('div', class_ = 'col-sm-3').text
        EGID.append(EGIDs) 
        
        validations_ID = soup.find(id="cphContent_ctl37")
        validations = fieldset.div.find('div', class_ = 'col-sm-4 input-append date').text
        validation.append(validations) 
        
        PO_numbers = soup.find(id="cphContent_ctl38")
        PO_numbers = fieldset.div.find('div', class_='col-sm-4') if fieldset.div.find('div', class_='col-sm-4') else '-'
        PO_number.append(PO_numbers) 
        
        ZIP_POs = soup.find(id="cphContent_ctl42")
        ZIP_POs = fieldset.div.find('div', class_ = 'col-sm-10').text
        ZIP_PO.append(ZIP_POs)
        
        Legal_ID = soup.find(id="cphContent_ctl43")
        legal_status = fieldset.div.find('div', class_ = 'col-sm-4').text
        legal.append(legal_status)
        
        RC_ID = soup.find(id="cphContent_ctl44")
        RC = fieldset.div.find('div', class_ = 'col-sm-4').text
        RC_status.append(RC)
         
        uid_headquarters_ID = soup.find(id="cphContent_ctl45")
        uid_headquarters = fieldset.div.find('div', class_='col-sm-4') if fieldset.div.find('div', class_='col-sm-4') else '-'
        uid_headquarter.append(uid_headquarters) 
        
        reference_no = soup.find(id="cphContent_ctl47")
        reference_no = fieldset.div.find('div', class_ = 'col-sm-3').text
        reference.append(reference_no)
         
        VAT_status_ID = soup.find(id="cphContent_ctl48")
        VAT_status = fieldset.div.find('div', class_ = 'col-sm-4').text
        VAT_register_status.append(VAT_status)
        
        VAT_number_ID = soup.find(id="cphContent_ctl49")
        VAT_numbers = fieldset.div.find('div', class_ = 'col-sm-4').text
        VAT_number.append(VAT_numbers)
        
        VAT_start_ID= soup.find(id="cphContent_ctl50")
        VAT_start =fieldset.div.find('div', class_ = 'col-sm-4 input-append date').text
        VAT_start_of_obligation.append(VAT_start)
        
        VAT_end_ID = soup.find(id="cphContent_ctl51")
        VAT_end = fieldset.div.find('div', class_='col-sm-4 input-append date') if fieldset.div.find('div', class_='col-sm-4 input-append date') else '-'
        VAT_end_of_obligation.append(VAT_end) 

df_test = pd.DataFrame({'UID': UID,'Status': status,'Extension':extension,'Name': name,'Additional name':additional_name,'Translation':translation,'C/o':c_o,'Address':address, 'Complement':complement,'ZIP':zip,'Canton':canton,'Country': country, 'Municipality':municipality,
                          'Municipality_no':municipality_no,'EGID': EGID,'Last validation': validation, 'PO number': PO_number, 'ZIP PO Box' : ZIP_PO, 'Legal form':legal, 'RC status': RC_status,'UID Headquarters':  uid_headquarter, 'Register reference': reference, 
                          'VAT register status': VAT_register_status, 'VAT number': VAT_number, 'Start of obligation VAT':VAT_start_of_obligation, 'End of obligation VAT':VAT_end_of_obligation})
df_test.to_csv(r'C:\Users\vollm\scraping\UIDtesting.csv')