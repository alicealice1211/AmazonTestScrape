# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
import bs4 as bs
import re
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


allProductDimensions=[]
allItemWeight=[]
allShippingWight=[]
allSellerRank=[]
allPrimeMember=[] 
allTitle=[]
allManufacturer=[]
allFulfiller=[] 
nameList= []
linkList=[]
urlPage=[]
n=1
i=0
n=1 
product=0
         
file_name = ('amazn testing'+".csv")
url='https://www.amazon.com/s/ref=sr_nr_p_97_0?fst=as%3Aoff&&&keywords=small+appliance&&ie=UTF8&&qid=1516913444&&rnid=11292771011&rh=i%3Aaps%2Ck%3Asmall+appliance%2Cp_97%3A11292772011'
headers = {'User-Agent':'Mozilla/5.0'}
source_code = requests.get(url, headers=headers)
plain_text = source_code. text
soup = bs.BeautifulSoup(plain_text, 'lxml')



while n <20:
    n+=1
    smallApplianceUrl="https://www.amazon.com/s/ref=sr_pg_"+str(n)+"?fst=as%3Aoff&rh=n%3A2619525011%2Ck%3Asmall+appliances&page="+str(n)+"&keywords=small+appliances&ie=UTF8&qid=1517018435"
    urlPage.append(smallApplianceUrl)


for pageUrl in urlPage:
    url=pageUrl
    headers = {'User-Agent':'Mozilla/5.0'}
    source_code = requests.get(url, headers=headers)
    plain_text = source_code. text
    soup = bs.BeautifulSoup(plain_text, 'lxml')
    linkText=soup.find_all('div',{'class': 'a-row a-spacing-none'})     
    for link in linkText:
        if len(link)<5:
            continue
        else:
            link=str(link)
            link=link.split('"')[5]
            linkList.append(link)

for currentLink in linkList:
    url= currentLink
    headers = {'User-Agent':'Mozilla/5.0'}
    file_name = ('amazn testing'+".csv")
    source_code = requests.get(url, headers=headers)
    plain_text = source_code. text
    soup = bs.BeautifulSoup(plain_text, 'lxml')
#filefrom
    driver = webdriver.Chrome(executable_path=r'C:\Users\alice\Desktop\chromedriver')
    driver.get(currentLink)
    try: 
        title = driver.find_element_by_xpath('//span[@id="productTitle" and @class="a-size-large"]')
        titleName=str(title.get_attribute('innerHTML')).split('\n')[9]
        allTitle.append(titleName)
        product+=1
        print('this is product #: '+ str(product)+ '& on page'+ str(currentLink))    
    except:
        allTitle.append('page take too long time to load')
##for title in titles:
##    print(title.get_attribute('innerHTML'))

    try:
        manufacturer = driver.find_element_by_xpath('//a[@id="bylineInfo" and @class="a-link-normal"]')
        manufacturerName=manufacturer.get_attribute('innerHTML')
        allManufacturer.append(manufacturerName)
##    print(manufacturer.get_attribute('innerHTML'))
    except:
        print('skipped m')
        allManufacturer.append('N/A')
    try:    
        fulfiller = driver.find_element_by_xpath('//div[@id="merchant-info" and @class="a-section a-spacing-mini"]')
        fulfiller = fulfiller.get_attribute('innerHTML').split('.')[0]
        allFulfiller.append(fulfiller)
    except:
        print('noff')
        allFulfiller.append('N/A')
##for fulfiller in fulfillers:
##    print(fulfiller.get_attribute('innerHTML'))

    item_data = driver.find_elements_by_xpath('//td[@class="a-size-base"]')
    try:
        productDimensions = item_data[0].get_attribute('innerHTML')
        allProductDimensions.append(productDimensions)
    except:
        print('noPD')
        allProductDimensions.append('N/A')
    try:
        itemWeight = item_data[1].get_attribute('innerHTML')
        allItemWeight.append(itemWeight)
    except:
        print('noIW')
        allItemWeight.append('N/A')
        
    try:
        shippingWeight = item_data[2].get_attribute('innerHTML').split('(<a href')[0]
        allShippingWight.append(shippingWeight)
    except:
        print('noSW')
        allShippingWight.append('N/A')
##for data in item_data:
##    print(data.get_attribute('innerHTML'))
    seller_ranks= driver.find_elements_by_xpath('//td/span/span')
##for seller_rank in seller_ranks:
##    print(seller_rank.get_attribute('innerHTML'))
    try :
        sellerRank=str(seller_ranks[31].get_attribute('innerHTML')).split(';')[0]
        allSellerRank.append(sellerRank)
    except:
#        sellerRank=str(sellerRanks[1].get_attribute('innerHTML')).split(';')[0]
#        allSellerRank.append(sellerRank)
        i=i+1
        print('skipped', i)
        allSellerRank.append('N/A')
    
    prime=driver.find_elements_by_xpath('//i[@class="a-icon a-icon-prime"]')
#for primeMember in prime:
#    print(primeMember.get_attribute('innerHTML'))
    try :
        primeMember=str(prime[0].get_attribute('innerHTML')).split('>')[1].split('<')[0]
        allPrimeMember.append(primeMember)
    except:
        print('skipped prime')
        allPrimeMember.append('No')
    driver.close()
 
file_name = ('cocobutter'+".csv")
rows=zip(allTitle,allManufacturer, allFulfiller, allProductDimensions,  allItemWeight, shippingWeight, allSellerRank,allPrimeMember) 
with open(file_name, 'w', encoding='utf-8', newline='') as csvfile:
    links_writer=csv.writer(csvfile)
    for row in rows:
        links_writer.writerow(row)

#
#for title, manufacturer, productDimension, itemWeight, shippingWeight, sellerRank, primeMember in zip ()) :
##    title=str(title.get_attribute('innerHTML')).split('\n')[9]
##    allTitle.append(title)
#    
#    manufacturer=manufacturer.get_attribute('innerHTML')
#    allManufacturer.append(manufacturer)
#    
#    fulfiller = fulfiller.get_attribute('innerHTML').split('.')[0]
#    allFulfiller.append(fulfiller)
#    
#    productDimensions = item_data[0].get_attribute('innerHTML')
#    allProductDimensions.append(productDimension)
#    
#    itemWeight = item_data[1].get_attribute('innerHTML')
#    allItemWeight.append(itemWeight)
#    shippingWeight = item_data[2].get_attribute('innerHTML').split('(<a href')[0]
#    allShippingWight.append(shippingWeight)
#    
#    sellerRank=str(seller_ranks[31].get_attribute('innerHTML')).split(';')[0]
#    allSellerRank.append(sellerRank)
#    
#    primeMember=str(prime[0].get_attribute('innerHTML')).split('>')[1].split('<')[0]
#    allPrimeMember.append(primeMember)





#    for coffee, link in zip (soup.find_all(class_='list-title'),soup.find_all(class_='btn')):
#        coffee  = str(coffee).split('>')[2].split('<')[0]
#        allNames.append(coffee)
#        y= str(link)[1:]  
#        link=str(link).split('href="')[1].split('>')[0]
#        link='https://javabeanplus.com'+link
#        allLinks.append(link)
#         
#
#
#
#rows=zip (allNames,allLinks)
#with open(file_name, 'w', encoding='utf-8', newline='') as csvfile:
#    links_writer=csv.writer(csvfile)
#    for row in rows:
#        links_writer.writerow(row)
