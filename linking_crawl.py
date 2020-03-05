import requests
from lxml import html
import csv 
URL = 'https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg'

response = requests.get(URL)
OUTPUT = 'chrome_extension.csv'
page = html.fromstring(response.content)

name = page.xpath("//h1/text()")[0]
try:
    offered_by = page.xpath('//a[@class="e-f-y"]/text()')[0]
    website = page.xpath('//a[@class="e-f-y"]/@href')[0]
except:
    offered_by = page.xpath('//span[@class="oc"]/text()')

img_url = page.xpath('//img/@src')[0]
ratings = page.xpath('//meta[@itemprop="ratingValue"]/@content')[0]
users = page.xpath('//span[@class="e-f-ih"]/text()')[0].replace('users','')
rating_count = page.xpath('//meta[@itemprop="ratingCount"]/@content')[0]
#updated_date = page.xpath('//span[@class="C-b-p-D-Xe h-C-b-p-D-xh-hh"]/text()')
#size = page.xpath('//span[@class="C-b-p-D-Xe h-C-b-p-D-za"]/text()')
update_date = page.xpath('//span[text()="Updated:"]/following-sibling::span/text()')[0]
size = page.xpath('//span[text()="Size:"]/following-sibling::span/text()')[0]
languages = page.xpath('//span[text()="Languages:"]/following-sibling::span/text()')[0].replace('See all','')
developer_address = page.xpath('//div[text()="Developer"]/following-sibling::div/a/@href')
description = page.xpath('//div[@itemprop="description"]/following-sibling::pre/text()')

with open(OUTPUT,'a',newline='',encoding='utf-8') as f:
    sheet = csv.writer(f)
    data = [name,offered_by,website,img_url,ratings,users,rating_count,update_date,size,languages,developer_address,description]
    print(data)
    sheet.writerow(data)
    


