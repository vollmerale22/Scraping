# Trade-Project

Scraping from the website: https://www.uid.admin.ch/search.aspx

In order to scrape the website, data that is requested and responses will be send, while keeping the UID's state of the searching person. With every POST request, the _VIEWSTATE field is passed around. The server decodes and loads the client's UID frm this date, performs some processing, computes the value for the new view state based on the new values and renders the resulting page with the new view state as a hidden field. 

# Background
![image](https://user-images.githubusercontent.com/71836453/130313915-918531a2-7e5d-42b7-8c87-e087311e461a.png)

A request to "Search.aspx" has been made. Clicking on the details from the resulting searches leads you to the request details where all the details can be seen.

# Method
Search for:
https://www.uid.admin.ch/Detail.aspx?uid_id=CHE...

For each UID in the list, it is iterated through the Scrapy Spider. 
1. Initiate Crawl process through the start URL
2. Importantly: set download_delay to 10 seconds in Spider and settings.py
3. Scrapy Request through the range of the UID list
4. Select items with CSS Selector
5. Yield items
6. Output: csv file

Since the website will notice the frequent site visits soon, one can either implement rotating proxies to disguise the IP Adress or delay the download speed. 

*Note:*
Testing.py is another method for doing this scraping task. Here we work with Selenium and Beautiful Soup. A Chrom Driver is used to open every request, scrape the data, append to the csv file and close the website. The items are also slected with the CSS Selector.
