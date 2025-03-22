"""
_Import and refrence essencial libraries
"""
from Scraper import *
import time, asyncio, urllib, urllib3, os, json, re, num2words
from Scraper import __webdriver__

""" Define essential args .
User-agent is pc sensitive.
UPLOAD_FILE_URL needs DNS to provide a connection to JQUERY caused by OFAC.
"""

COINMARKETCAP_URL = "https://coinmarketcap.com/"
COINMARKETCAP_JSON_FILE_PATH = "06e387dae8db628a49ea418df764e4d376c701f3694c49fef780401ca7c446a1.json"
COINMARKETCAP_XAPTH = '/html/body/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[5]/table/tbody/tr'

"""
_Global json data
"""
coinmarketcap_data = {}

"""
Scrap data from coinmarketcap
"""  
async def coinmarketcap(driver):
    crypto =  [{}]
    
    for PSNUM in range(1, 38):  
        Name = driver.find_element(By.XPATH, f' {COINMARKETCAP_XAPTH}[{PSNUM}]/td[3]/div/a/span/div/div/p').text
        Price = driver.find_element(By.XPATH, f' {COINMARKETCAP_XAPTH}[{PSNUM}]/td[4]').text
        TFHour = driver.find_element(By.XPATH, f' {COINMARKETCAP_XAPTH}[{PSNUM}]/td[6]').text
        MarketCap = driver.find_element(By.XPATH, f' {COINMARKETCAP_XAPTH}[{PSNUM}]/td[8]/p').text
        


        driver.execute_script("window.scrollBy(0, 100);")  
        crypto[0].update([(Name, [Price,TFHour, SevenHour, MarketCap])])

    coinmarketcap_data.update([("crypto", crypto)])       
    write_json(COINMARKETCAP_JSON_FILE_PATH, coinmarketcap_data, 'w')

    return coinmarketcap_data

coinmarketcap_driver = run_webdriver(COINMARKETCAP_URL)

while True:
    asyncio.run(coinmarketcap()))
    time.sleep(60)