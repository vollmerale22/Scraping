# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 13:17:02 2021

@author: AV
"""

import scrapy
from UIDs.items import UidsItem
import pandas as pd
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess
import time

          

class UIDSpider(scrapy.Spider):
    name = "uid"
    allowed_domains = ['www.uid.admin.ch']
    download_delay = 10
    start_urls = ['http://www.uid.admin.ch/']
    uids = pd.read_excel(r'S:\3_Hiwi\Vollmer\Scraping\List_of_UIDs_sorted.xlsx', sheet_name = '2001-3000',
    index_col = None)
    base_url = 'http://www.uid.admin.ch/Detail.aspx?uid_id={}'  
    
    def parse(self, response):
#        self.log('I could visit' + self.uids['UID'][1])
        for uid in range(len(self.uids)):
           # time.sleep(15)
            yield scrapy.Request(url=self.base_url.format(self.uids['UID'][uid]), callback=self.parse_details)

    
    
    def parse_details(self, response): 
        item = UidsItem()
       
        
        item['uid'] = response.css('#cphContent_ctl14+ .col-sm-4 div::text').extract()
        item['status'] = response.css('#cphContent_ctl15+ .col-sm-4 div::text').extract()
        item['extension'] = response.css('#cphContent_ctl16+ .col-sm-4 div::text').extract()
        item['name'] = response.css('#cphContent_ctl17+ .col-sm-10 div::text').extract()
        item['additional_name'] = response.css('#cphContent_ctl19+ .col-sm-10 div::text').extract()
        item['translation'] = response.css('#cphContent_ctl20+ .col-sm-10 div::text').extract()
        item['c_o'] = response.css('#cphContent_ctl21+ .col-sm-10 div::text').extract()
        item['street'] = response.css('#cphContent_ctl25+ .col-sm-10 div::text').extract()
        item['complement']= response.css('#cphContent_ctl26+ .col-sm-10 div::text').extract()
        item['zip_town'] = response.css('#cphContent_ctl30+ .col-sm-10 div::text').extract()
        item['canton'] = response.css('#cphContent_ctl31+ .col-sm-4 div::text').extract()
        item['country'] = response.css('#cphContent_ctl32+ .col-sm-4 div::text').extract()
        item['municipality'] = response.css('#cphContent_ctl33+ .col-sm-4 div::text').extract()
        item['municipality_no'] = response.css('#cphContent_ctl34+ .col-sm-4 div::text').extract()
        item['egid'] = response.css('#cphContent_ctl35+ .col-sm-3 div::text').extract()
        item['last_validation'] = response.css('#cphContent_ctl37_datLastValidationDate div::text').extract()
        item['po_box'] = response.css('#cphContent_ctl38+ .col-sm-4 div::text').extract()
        item['zip_po'] = response.css('#cphContent_ctl42+ .col-sm-10 div::text').extract()
        item['legal'] = response.css('#cphContent_ctl43+ .col-sm-4 div::text').extract()
        item['rc_status'] = response.css('#cphContent_ctl44+ .col-sm-4 div::text').extract()
        item['uid_head'] = response.css('#cphContent_ctl45+ .col-sm-4 div::text').extract()
        item['reference']= response.css('#cphContent_ctl47+ .col-sm-3 div::text').extract()
        item['vat_status'] = response.css('#cphContent_ctl48+ .col-sm-4 div::text').extract()
        item['vat_number']= response.css('#cphContent_ctl49+ .col-sm-4 div::text').extract()
        item['start_obl'] = response.css('#cphContent_ctl50_datVATBegin div::text').extract()
        item['end_obl'] = response.css('#cphContent_ctl51_datVATEnd div::text').extract()
        item['vat_group'] = response.css('#cphContent_ctl52+ .col-sm-4 div::text').extract()
        item['lei'] = response.css('#cphContent_ctl55+ .col-sm-4 div::text').extract()
        item['reg_status'] = response.css('#cphContent_ctl56+ .col-sm-4 div::text').extract()
        item['reg_date'] = response.css('#cphContent_ctl57+ .col-sm-4 div::text').extract()
        item['valid_until'] = response.css('#cphContent_ctl58+ .col-sm-4 div::text').extract()
            
            
        yield item
                      
# main driver
#process = CrawlerProcess()
#process.crawl(UIDSpider)
#process.start()
# the wrapper to make it run more times
  
