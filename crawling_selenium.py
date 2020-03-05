import time
from selenium import webdriver
import csv
OUTPUT = 'links.csv'
class Crawler:
    def __init__(self):
        browser = webdriver.Chrome()
        url = 'https://chrome.google.com/webstore/category/ext/7-productivity'
        browser.get(url)
        number = 0
        number2 = 2500
        for i in range(105):
            script_scroll = "window.scrollTo("+str(number)+","+str(number2)+")"
            print(script_scroll)
            contents = browser.find_elements_by_xpath("//div[@role='row']")
            urls_list = ['urls']
            
            for content in contents:
                link = content.find_element_by_xpath(".//a")
                link_url = link.get_attribute('href')
                urls_list.append(link_url)
            time.sleep(4)
            browser.execute_script(script_scroll)
            number = number2
            number2 = number2 + number2
            with open(OUTPUT,'w',newline='') as f:
                the_writer = csv.writer(f)
                header = 'Links'
                the_writer.writerow([header])
            print(number,number2)
            print(urls_list)
            for j in urls_list:
                with open(OUTPUT,'a',newline='') as f:
                    the_writer = csv.writer(f)
                   # print(j)
                    the_writer.writerow([j])
        
            time.sleep(8)


            
        contents = browser.find_elements_by_xpath("//div[@role='row']")
        for content in contents:
            link = content.find_element_by_xpath(".//a")
            link_url = link.get_attribute('href')
        #    with open(OUTPUT,'a',newline='') as f:
        #       the_writer = csv.writer(f)
        #        the_writer.writerow([link_url])
    
    




chrome_webstore = Crawler()


