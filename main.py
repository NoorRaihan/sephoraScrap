from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import json
import pandas as pd

# GLOBAL VARIABLES
PRODUCT_ID = "nudestix-nudies-matte-all-over-face-color-blush"
TARGET_URL = "https://www.sephora.my/api/v2.4/products/{product}/reviews?page[number]=1&page[size]=100000&sort=recent&filter[rating]={rate}"
content = None
driver = None
soup = None
all_reviews = {}
merged_reviews = []

# INITIATE ALL THE SELENIUM STUFFS AND BS4
def init():
    global driver, soup, content, all_reviews

    service = Service()
    option = webdriver.ChromeOptions()
    #option.add_argument("--headless") #Run like ninja ;)
    option.add_argument("--disable-gpu")
    #option.add_argument("--incognito")
    option.add_argument("--window-size=1920x1080")
    option.add_argument('--no-sandbox')
    option.add_argument("--disable-blink-features=AutomationControlled") 
    option.add_experimental_option("excludeSwitches", ["enable-automation"]) 
    option.add_experimental_option("useAutomationExtension", False) 
    driver = webdriver.Chrome(service=service, options=option)

    mainProcess()
    
#PROCESS
def mainProcess():
    global content, soup, all_reviews

    for i in range(1,6):
        #time.sleep(2)
        driver.get(TARGET_URL.format(product=PRODUCT_ID,rate=i))
        #time.sleep(2)
        content = driver.page_source

        soup = BeautifulSoup(content, features="html.parser")
        extractData()
    #print(all_reviews['1.0'][0])

    for rate in all_reviews:
        raw2Csv('data_'+rate, all_reviews[rate])

#EXTRACT ALL DATA FROM JSON
def extractData():
    global content, soup, all_reviews, merged_reviews

    raw_json = json.loads(soup.find("pre").string)
    datas = raw_json['data']

    
    for data in datas:
        review = data['attributes']

        key = str(review['rating'])

        review['text'] = review['text'].replace('\n', '')
        review['text'] = review['text'].replace('\r', '')
        review['title'] = review['text'].replace('\n', '')
        review['title'] = review['text'].replace('\r', '')

        #map to extract only necessary data
        # tempAttr['review-title'] = review['title']
        # tempAttr['reviewer-name'] = review['reviewer-name']
        # tempAttr['review-desc'] = review['text']
        # tempAttr['review-rate'] = review['rating']
        # tempAttr['reviewer-country'] = review['country-name']
        # tempAttr['is-staff'] = review['is-staff']

        if(key in all_reviews.keys()):
            all_reviews[key].append(review)
        else:
            all_reviews[key] = []
            all_reviews[key].append(review)
        
        merged_reviews.append(review)

    raw2Csv('data_full', merged_reviews)

def raw2Csv(filename, data):
    #print(data)
    df = pd.DataFrame(data)
    df.to_csv(filename+'.csv',sep='|', index=False, encoding='utf-8')

init()
