# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UidsItem(scrapy.Item):
    # define the fields for your item here like:
     uid = scrapy.Field()
     status = scrapy.Field()
     extension = scrapy.Field()
     name = scrapy.Field()
     additional_name = scrapy.Field()
     translation = scrapy.Field()
     c_o = scrapy.Field()
     street = scrapy.Field()
     complement = scrapy.Field()
     zip_town = scrapy.Field()
     canton = scrapy.Field()
     country= scrapy.Field()
     municipality = scrapy.Field()
     municipality_no = scrapy.Field()
     egid = scrapy.Field()
     last_validation = scrapy.Field()
     po_box = scrapy.Field()
     zip_po = scrapy.Field()
     legal = scrapy.Field()
     rc_status = scrapy.Field()
     uid_head = scrapy.Field()
     reference = scrapy.Field()
     vat_status = scrapy.Field()
     vat_number = scrapy.Field()
     start_obl = scrapy.Field()
     end_obl = scrapy.Field()
     vat_group = scrapy.Field()
     lei = scrapy.Field()
     reg_status = scrapy.Field() 
     reg_date = scrapy.Field()
     valid_until = scrapy.Field()