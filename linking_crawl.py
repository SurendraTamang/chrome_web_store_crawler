import requests
from lxml import html
import csv
import random
import json

LIST_OF_USER_AGENTS = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36',

                       'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36',

                       ]


def get_response(url):
    headers = {'User-Agent': random.choice(LIST_OF_USER_AGENTS)}
    response = requests.get(url=url, headers=headers)
    if response.ok:
        return response
    else:
        return None


def crawl(url):

    OUTPUT = 'productivity.csv'
    response = get_response(url)
    if response:

        page = html.fromstring(response.content)

        name = page.xpath("//h1/text()")[0]
        try:
            website = page.xpath('//a[@class="e-f-y"]/@href')[0]
        except:
            website = page.xpath('//a[@class="e-f-y"]/@href')
        try:
            offered_by = page.xpath('//a[@class="e-f-y"]/text()')[0]

        except:
            offered_by = page.xpath('//span[@class="oc"]/text()')

        img_url = page.xpath('//img/@src')[0]
        ratings = page.xpath('//meta[@itemprop="ratingValue"]/@content')[0]
        users = page.xpath(
            '//span[@class="e-f-ih"]/text()')[0].replace('users', '')
        rating_count = page.xpath(
            '//meta[@itemprop="ratingCount"]/@content')[0]
        #updated_date = page.xpath('//span[@class="C-b-p-D-Xe h-C-b-p-D-xh-hh"]/text()')
        #size = page.xpath('//span[@class="C-b-p-D-Xe h-C-b-p-D-za"]/text()')
        update_date = page.xpath(
            '//span[text()="Updated:"]/following-sibling::span/text()')[0]
        size = page.xpath(
            '//span[text()="Size:"]/following-sibling::span/text()')[0]
        try:
            languages = page.xpath(
                '//span[text()="Languages:"]/following-sibling::span/text()')[0].replace('See all', '')
        except:
            languages = page.xpath(
                '//span[text()="Languages:"]/following-sibling::span/text()')
        developer_address = page.xpath(
            '//div[text()="Developer"]/following-sibling::div/a/@href')
        description = page.xpath(
            '//div[@itemprop="description"]/following-sibling::pre/text()')

        with open(OUTPUT, 'a', newline='', encoding='utf-8') as f:
            sheet = csv.writer(f)
            data = [name, offered_by, website, img_url, ratings, users, rating_count,
                    update_date, size, languages, developer_address, description]
            print(data)
            sheet.writerow(data)
    else:
        print("Not scraped this url", url)


if __name__ == "__main__":
    OUTPUT = 'productivity.csv'
    URL = 'https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg'
    with open(OUTPUT, 'w', encoding="utf-8") as csv_file:
        thewriter = csv.writer(csv_file)
        heading = ['name', 'offered_by', 'website', 'img_url', 'ratings', 'users',
                   'rating_count', 'update_date', 'size', 'languages', 'developer_address', 'description']
        thewriter.writerow(heading)
    with open('productivity.json', 'r+') as f:
        json_file = json.load(f)
        list_of_urls = json_file['category']
        for url in list_of_urls:
            crawl(url)
