# General Functions
##############################################################
import os,time, datetime, shutil, csv, unittest, HtmlTestRunner, cv2
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

    print('URL is ' + url)
    driver.get(url)  # open browser with specific site
    driver.maximize_window()  # maximize window
    time.sleep(5)

##############################################################
def SaveScreenshot(browser, screenshot_path, shield_status):


    screenshot_name = (browser.current_url + shield_status)
    chars_to_replace = ['://', '/', '.']
    for char in chars_to_replace:
        screenshot_name = screenshot_name.replace(char, '_')

    browser.get_screenshot_as_file(screenshot_path + screenshot_name + '.png')
    print('Screenshot saved' + screenshot_path + screenshot_name + '.png')
    return screenshot_path + screenshot_name + '.png'


def CompareScreenshots(img_no_shield, img_shield, screenshot_path, line):


    print('Start comparing ' + str(img_no_shield) + ' with ' + str(img_shield))
    # org_screenshot = cv2.imread('../TestResults/Screenshots/https_www_facebook_com_OFF copy.png')
    # shield_screenshot = cv2.imread('../TestResults/Screenshots/https_www_facebook_com_OFF copy 2.png')

    org_screenshot = cv2.imread(img_no_shield)
    shield_screenshot = cv2.imread(img_shield)
    if org_screenshot.shape == shield_screenshot.shape:
        print("screenshots size are equal - step PASS")
    else:
        print("screenshots size are  NOT equal - step FAIL")

    diff = cv2.subtract(org_screenshot, shield_screenshot)
    b, g, r = cv2.split(diff)

    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("screenshots are equal - test PASS")
    else:
        print('b diff = ' + str(cv2.countNonZero(b)) + ' g diff = ' + str(cv2.countNonZero(g)) + ' r diff = ' + str(cv2.countNonZero(r)))
        print("screenshots are NOT equal - test FAIL")

        chars_to_replace = ['://', '/', '.']
        for char in chars_to_replace:
            line = line.replace(char, '_')
            print(line)

        diff_file_name = screenshot_path + line + 'DIFF.png'
        cv2.imwrite(diff_file_name, diff)
        time.sleep(2)
        print('You can find diff results in the following path: ' + diff_file_name)




def CloseBrowser (browser):
    browser.quit()


