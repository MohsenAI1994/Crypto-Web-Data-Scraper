"""
_Import and refrence essencial libraries
"""
from functools import wraps
from types import FunctionType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time, asyncio, urllib, urllib3, os, json, re, num2words

""" Define essential args 
User-agent is pc sensitive
(x86)
"""

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
CHROMEDRIVER_EXECUTABLE_PATH = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'

class __webdriver__(webdriver.Chrome):
    def __init__(self, options = None, service = None, keep_alive = True):

        """
         _Use --no-sandbox to avoid security issues.
         _Use --headless to send http response without gui.
         _Use user-agent to pass pc configuration to the server.
         _Use --incognito to send http request anonymously.
         _Use maximize window to get full screen chormedriver.
         _Use set_window_size when using headless.
        """

        service = ChromeService(executable_path = CHROMEDRIVER_EXECUTABLE_PATH)

        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument("--window-size=1229x895")
        options.add_argument(f'user-agent={USER_AGENT}')
        options.add_argument("--incognito")

        return super().__init__( options = options, service = service, keep_alive = True)

    def find_element(self, by, value = None) :
        while True:
            try:
                super().find_element(by, value)
                time.sleep(0.01)       

            except(Exception):
                print(f'proccessing {value}')   

            else:
                print('HTML element has been found')
                return super().find_element(by, value)
                               
    def get(self, url: str) -> None:
        while True:
            try:
                super().get(url) 
                time.sleep(0.01)       
                
            except(Exception):
                print(f'proccessing {url}')

            else:
                print('HTML element has been found')
                return super().get(url) 