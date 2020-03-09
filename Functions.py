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
    try:
        f = open(file, 'r') # reading from file
        lines = f.readlines()  # read lines
        f.close()
        return lines
    except:
        print('Error occurred in ReadURLS function')

##############################################################

def StartBrowser(browser_type, shield_status):
    try:
        option = Options()

        if shield_status == 'ON':
            option.add_argument('--proxy-server=%s' % Automation.Environment.proxy)
        option.add_argument('user-data-dir=/Users/shaiadani/Library/Application Support/Google/Chrome/Default')
        # option.add_experimental_option('prefs',
        #                                {'profile.default_content_setting_values.notifications': 1})  # 1 yes 2 No
        # option.add_experimental_option('prefs',
        #                                {'profile.default_content_settings.cookies': 1})  # 1 yes 2 No
        # option.add_experimental_option('prefs',
        #             #                               {'profile.default_content_setting_values.geolocation': 1})  # 1 yes 2 No
        #             # option.add_argument('--lang=es')

        driver = webdriver.Chrome(options=option, executable_path=browser_type)  # Start browser with the option - currently, only chrome

        return driver
    except:
        print('Error occurred in StartBrowser function')
##############################################################
def GoToURL(driver, url):

    try:
        print('URL is ' + url)
        driver.get(url)  # open browser with specific site
        driver.maximize_window()  # maximize window
        time.sleep(10)
    except:
        print('Error occurred in StartBrowser function')


##############################################################
def SaveScreenshot(browser, screenshot_path, shield_status):
    try:
        screenshot_name = (browser.current_url + shield_status)
        chars_to_replace = ['://', '/', '.', '-', '?']
        for char in chars_to_replace:
            screenshot_name = screenshot_name.replace(char, '_')

        browser.get_screenshot_as_file(screenshot_path + screenshot_name + '.png')
        print('Screenshot saved' + screenshot_path + screenshot_name + '.png')
        return screenshot_path + screenshot_name + '.png'
    except:
        print('Error occurred in SaveScreenshot function')


def CompareScreenshots(img_no_shield, img_shield, screenshot_path, line, threshold):

    try:
        print('Start comparing ' + str(img_no_shield) + ' with ' + str(img_shield))
        # org_screenshot = cv2.imread('../TestResults/Screenshots/https_www_facebook_com_OFF copy.png')
        # shield_screenshot = cv2.imread('../TestResults/Screenshots/https_www_facebook_com_OFF copy 2.png')

        org_screenshot = cv2.imread(img_no_shield)
        shield_screenshot = cv2.imread(img_shield)
        if org_screenshot.shape == shield_screenshot.shape:
            print("screenshots size is equal - step PASS")
            print('Shape is  is ' + str(shield_screenshot.shape))
        else:
            print("screenshots size is  NOT equal - step FAIL")

        diff = cv2.subtract(org_screenshot, shield_screenshot)

        r, g, b = cv2.split(diff)
        print('diff pixels =' + str(cv2.countNonZero(b) + cv2.countNonZero(g) + cv2.countNonZero(r)))
        print('org pixels =' + str(org_screenshot.shape[0]*org_screenshot.shape[1]))

        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print("screenshots are exactly equal - test PASS")
        elif ((cv2.countNonZero(b) + cv2.countNonZero(g) + cv2.countNonZero(r)) / (org_screenshot.shape[0] * org_screenshot.shape[1])) < threshold:
            print('screenshots are NOT equal but under ' + str(threshold) + ' % difference - step PASS')
            print('Deviation percentage is % ' + str((cv2.countNonZero(b) + cv2.countNonZero(g) + cv2.countNonZero(r)) / (org_screenshot.shape[0] * org_screenshot.shape[1])))
        else:
            print('b diff = ' + str(cv2.countNonZero(r)) + ' g diff = ' + str(cv2.countNonZero(g)) + ' r diff = ' + str(cv2.countNonZero(b)))
            print('screenshots are NOT equal, more than ' + str(threshold) + ' % difference - step FAIL')
            print('Deviation percentage is % ' + str((cv2.countNonZero(b) + cv2.countNonZero(g) + cv2.countNonZero(r)) / (
                        org_screenshot.shape[0] * org_screenshot.shape[1])))
            chars_to_replace = ['://', '/', '.', '-', '?']
            for char in chars_to_replace:
                line = line.replace(char, '_')

            diff_file_name = screenshot_path + line + 'DIFF.png'
            cv2.imwrite(diff_file_name, diff)
            time.sleep(2)
            print('You can find diff results in the following path: ' + diff_file_name)
            print('Returning ' + diff_file_name)
            return diff_file_name
    except:
        print('Error occurred in CompareScreenshots function')



def CloseBrowser (browser):
    try:
        browser.quit()
    except:
        print('Error occurred in CloseBrowser function')



