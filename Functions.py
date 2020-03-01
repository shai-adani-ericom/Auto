# General Functions
##############################################################
import os,time, datetime, shutil, csv, unittest, HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import Automation.Environment

def WriteToLog(self, fileName, textToWrite):
    f = open(fileName, 'a')  # opening file for adding text
    timeStamp = str(datetime.datetime.now())  # builtin function from datetime module to get current time
    f.write(timeStamp + " " + textToWrite + '\n')  # writing timestamp + text + \n in order to start a new line!
    f.close()  # Closing file



# FrameModeSanity Functions
##############################################################
def ReadURLS(file):

    f = open(file, 'r') # reading from file
    lines = f.readlines()  # read lines
    f.close()
    return lines

##############################################################

def StartBrowser(browser_type, shield_status):

    option = Options()
    if shield_status == 'ON':
        option.add_argument('--proxy-server=%s' % Automation.Environment.proxy)
    driver = webdriver.Chrome(options=option, executable_path=browser_type)  # Start browser with the option - currently, only chrome
    return driver
##############################################################
def GoToURL(driver, url):

    driver.get(str(url))  # open browser with specific site
    driver.maximize_window()  # maximize window
    time.sleep(10)

##############################################################
def SaveScreenshot(screenshot_path,shield_status):
    pass
def CompareScreenshots(screenshot_no_shield, screenshot_shield):
    pass


