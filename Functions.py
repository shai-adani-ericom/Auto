# General Functions
##############################################################
import os,time, datetime, shutil, csv, unittest, HtmlTestRunner, cv2, csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import Automation.Environment

def WriteToLog(fileName, textToWrite):
    f = open(fileName, 'a')  # opening file for adding text
    timeStamp = str(datetime.datetime.now())  # builtin function from datetime module to get current time
    f.write(timeStamp + " " + textToWrite + '\n')  # writing timestamp + text + \n in order to start a new line!
    f.close()  # Closing file

def CreateNewStatisticsFile(fileName, shield_mode, build_number):
    url_column_name, deviation_column_name, diff__column_file_name = 'URL', 'Deviation%', 'DiffFileName'
    timeStamp = str(datetime.datetime.now())  # builtin function from datetime module to get current time
    statistics_file = fileName+'_'+timeStamp+'_'+build_number+'_'+shield_mode+'.csv'
    with open(statistics_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([url_column_name, deviation_column_name, diff__column_file_name])
        Automation.Environment.statistics_file = statistics_file

def SaveCompareScreenShotsStatistics(statistics_file_name, url, deviation, diff_file):
    with open(statistics_file_name, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([url,deviation,diff_file])



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

def StartBrowser(browser_type, shield_status, headless_mode):

    if 'chromedriver' in browser_type:
        try:
            options = ChromeOptions()

            if shield_status == 'ON':
                options.add_argument('--proxy-server=%s' % Automation.Environment.proxy)
            if headless_mode == 1:
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')
                options.add_argument("--start-maximized")
            options.add_argument('user-data-dir=/Users/shaiadani/Library/Application Support/Google/Chrome/Default')
            options.add_argument('--no-sandbox')  # Bypass OS security model
            options.add_argument('--disable-infobars')
            driver = webdriver.Chrome(options=options, executable_path=browser_type)  # Start browser with the option - currently, only chrome
            driver.set_window_size('1920','878')
            return driver
        except:
            print('Error occurred in StartBrowser function')
    elif 'geckodriver' in browser_type:
        options = FirefoxOptions()
        desired_capability = webdriver.DesiredCapabilities.FIREFOX
        try:
            if shield_status == 'ON':
                proxy = Automation.Environment.proxy
                desired_capability['proxy'] = {
                    'proxyType': "manual",
                    'httpProxy': proxy,
                    'ftpProxy': proxy,
                    'sslProxy': proxy,
                }

            if headless_mode == 1:
                options.add_argument('--headless')

            options.add_argument('--no-sandbox')  # Bypass OS security model
            options.add_argument('--disable-infobars')
            driver = webdriver.Firefox(options=options,capabilities=desired_capability,executable_path=browser_type)
            driver.set_window_size('1920', '900')
            return driver
        except:
             print('Error occurred in StartBrowser function')
    elif 'msedgedriver' in browser_type:
        desired_capability = webdriver.DesiredCapabilities.INTERNETEXPLORER
        # try:
        if shield_status == 'ON':
            proxy = Automation.Environment.proxy
            desired_capability['proxy'] = {
                'proxyType': "manual",
                'httpProxy': proxy,
                'ftpProxy': proxy,
                'sslProxy': proxy,
            }
        driver = webdriver.Edge(executable_path=browser_type, capabilities=desired_capability)
        driver.set_window_size('1920', '900')
        return driver


##############################################################
def GoToURL(driver, url):

    try:
        print('URL is ' + url)
        driver.get(url)  # open browser with specific site
        if Automation.Environment.healdless_mode == 0:
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
        print('Deviation in % = ' + str((((cv2.countNonZero(b) + cv2.countNonZero(g) + cv2.countNonZero(r)) / (org_screenshot.shape[0] * org_screenshot.shape[1])) * 100)))

        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print("screenshots are exactly equal - test PASS")
        elif (((cv2.countNonZero(b) + cv2.countNonZero(g) + cv2.countNonZero(r)) * 100) / (org_screenshot.shape[0] * org_screenshot.shape[1])) < threshold:
            print('screenshots  are NOT equal but under ' + str(threshold) + ' % difference - step PASS')
            print('Deviation in % = ' + str((((cv2.countNonZero(b) + cv2.countNonZero(g) + cv2.countNonZero(r)) / (org_screenshot.shape[0] * org_screenshot.shape[1])) * 100)))
            deviation = str(int(((((cv2.countNonZero(b) + cv2.countNonZero(g) + cv2.countNonZero(r)) / (
                    org_screenshot.shape[0] * org_screenshot.shape[1])) * 100))))
            url = line
            print('Compare test PASS for the following URL :' + line)
        else:
            print('r diff = ' + str(cv2.countNonZero(r)) + ' g diff = ' + str(cv2.countNonZero(g)) + ' b diff = ' + str(cv2.countNonZero(b)))
            print('screenshots are NOT equal, more than ' + str(threshold) + ' % difference - step FAIL')
            print('Deviation in % = ' + str((((cv2.countNonZero(b) + cv2.countNonZero(g) + cv2.countNonZero(r)) / (org_screenshot.shape[0] * org_screenshot.shape[1])) * 100)))
            deviation = str(int(((((cv2.countNonZero(b) + cv2.countNonZero(g) + cv2.countNonZero(r)) / (
                        org_screenshot.shape[0] * org_screenshot.shape[1])) * 100))))
            url = line
            chars_to_replace = ['://', '/', '.', '-', '?']
            for char in chars_to_replace:
                line = line.replace(char, '_')

            statistics_diff_file_name = line + 'DIFF.png'
            diff_file_name = screenshot_path + statistics_diff_file_name
            cv2.imwrite(diff_file_name, diff)
            time.sleep(2)
            print('You can find diff results in the following path: ' + diff_file_name)

        SaveCompareScreenShotsStatistics(Automation.Environment.statistics_file, url, deviation, statistics_diff_file_name)
    except:
        print('Error occurred in CompareScreenshots function')



def CloseBrowser (browser):
    try:
        browser.quit()
    except:
        print('Error occurred in CloseBrowser function')



