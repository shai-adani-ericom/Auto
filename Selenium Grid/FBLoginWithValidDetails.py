#This file contains function for FB project
#Author: Shai Adani
#Date 17/02/2019

##############################################################
# import relevant modules
import os, time, datetime, shutil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver import FirefoxOptions
import datetime

class FBValidDetails:
    def __init__(self):
        print("FBValidLogin Test Started")

    def WriteToLog(self, fileName, textToWrite):
        f = open(fileName, 'a')  # opening file for adding text
        timeStamp = str(datetime.datetime.now())  # builtin function from datetime module to get current time
        f.write(timeStamp + " " + textToWrite + '\n')  # writing timestamp + text + \n in order to start a new line!
        f.close()  # Closing file

    def FBLoginWithValidDetailsTest(self):

        self.fileName = "FBLoginWithValidDetailsLog.txt"
        self.resultsFile = "TestResults.txt"

        self.WriteToLog(self.fileName,"Starting with FBLoginWithValidDetails test ")
        # ###################################################################################
        # # chrome working
        # try:
        #     option = Options()  # Use this 3 lines in order to add option to send or disable facebook nitofocations.
        #     option.add_experimental_option("prefs",
        #                                    {"profile.default_content_setting_values.notifications": 1})  # 1 yes 2 No
        #
        #     self.driver=webdriver.Remote(
        #         options=option,
        #         command_executor="http://tSs6t1WI7e9xBkIPeChaaaRShxbZVCdf:lvbEnYdk2dItng9sIgtJharoxtdjWgo7@ADANI.gridlastic.com:80/wd/hub",
        #         desired_capabilities={
        #             "browserName": "chrome",
        #             "browserVersion": "latest",
        #             "video": "True",
        #             "platform": "WIN10",
        #             "platformName": "windows",
        #         })
        #     print ("Video: http://s3-eu-west-1.amazonaws.com/be8f5d0a-c2d2-9383-27b0-464cabf83d80/e97e4b2c-f903-9941-7915-dce56d84b8f0/play.html?"+ self.driver.session_id)
        #
        #     # self.driver = webdriver.Chrome(options=option, executable_path="/Users/shaiadani/PycharmProjects/Ericom/Automation/drivers/chromedriver 81")
        #     self.driver.get("http://www.facebook.com")  # open browser with specific site
        #     self.driver.maximize_window()  # maximize window
        # except:
        #     self.WriteToLog(self.fileName,"ERROR - error occurred during facebook home page upload")
        #     ###################################################################################


        # ###################################################################################
        # # FF working
        # options = FirefoxOptions()
        # desired_capability = webdriver.DesiredCapabilities.FIREFOX
        #
        # options.add_argument('--no-sandbox')  # Bypass OS security model
        # options.add_argument('--disable-infobars')
        # # driver = webdriver.Firefox(options=options, capabilities=desired_capability, executable_path=browser_path)
        # # driver.set_window_size('1920', '900')
        #
        # try:
        #
        #     self.driver=webdriver.Remote(
        #         options=options,
        #         command_executor="http://tSs6t1WI7e9xBkIPeChaaaRShxbZVCdf:lvbEnYdk2dItng9sIgtJharoxtdjWgo7@ADANI.gridlastic.com:80/wd/hub",
        #         desired_capabilities={
        #             "browserName": "firefox",
        #             "browserVersion": "72",
        #             "video": "True",
        #             "platform": "WIN10",
        #             "platformName": "windows",
        #         })
        #     print ("Video: http://s3-eu-west-1.amazonaws.com/be8f5d0a-c2d2-9383-27b0-464cabf83d80/e97e4b2c-f903-9941-7915-dce56d84b8f0/play.html?"+ self.driver.session_id)
        #
        #     self.driver.get("http://www.facebook.com")  # open browser with specific site
        #     self.driver.maximize_window()  # maximize window
        # except:
        #     self.WriteToLog(self.fileName,"ERROR - error occurred during facebook home page upload")
        #     ###################################################################################

        # ###################################################################################
        # # Internet Explorer 11 - working
        #
        # try:
        #
        #     self.driver = webdriver.Remote(
        #         # options=options,
        #         command_executor="http://tSs6t1WI7e9xBkIPeChaaaRShxbZVCdf:lvbEnYdk2dItng9sIgtJharoxtdjWgo7@ADANI.gridlastic.com:80/wd/hub",
        #         desired_capabilities={
        #             "browserName": "internet explorer",
        #             "browserVersion": "11",
        #             "video": "True",
        #             "platform": "WIN10",
        #             "platformName": "windows",
        #         })
        #     print(
        #         "Video: http://s3-eu-west-1.amazonaws.com/be8f5d0a-c2d2-9383-27b0-464cabf83d80/e97e4b2c-f903-9941-7915-dce56d84b8f0/play.html?" + self.driver.session_id)
        #
        #     self.driver.get("http://www.facebook.com")  # open browser with specific site
        #     self.driver.maximize_window()  # maximize window
        # except:
        #     self.WriteToLog(self.fileName, "ERROR - error occurred during facebook home page upload")
        #     ###################################################################################

        ###################################################################################
        # MicrosoftEdge - working

        proxy_address = 'Shield-Load-80e1f451a8f2c519.elb.eu-central-1.amazonaws.com:3128'
        # try:
        options = ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument('--proxy-server=%s' % proxy_address)
        options.add_argument('--disable-gpu')
        options.add_argument("--start-maximized")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--no-sandbox')  # Bypass OS security model
        options.add_argument('--disable-infobars')

        self.driver = webdriver.Remote(
            command_executor="http://tSs6t1WI7e9xBkIPeChaaaRShxbZVCdf:lvbEnYdk2dItng9sIgtJharoxtdjWgo7@ADANI.gridlastic.com:80/wd/hub",
            desired_capabilities={
                # "browserName": "MicrosoftEdge",
                "browserName": "chrome",
                "browserVersion": "latest",
                "video": "True",
                "platform": "WIN10",
                "platformName": "windows",
            },
            options=options)
        print(
            "Video: http://s3-eu-west-1.amazonaws.com/be8f5d0a-c2d2-9383-27b0-464cabf83d80/e97e4b2c-f903-9941-7915-dce56d84b8f0/play.html?" + self.driver.session_id)

        self.driver.get("http://www.facebook.com")  # open browser with specific site

        ''' Use Navigation Timing  API to calculate the timings that matter the most '''

        navigationStart = self.driver.execute_script("return window.performance.timing.navigationStart")
        responseStart = self.driver.execute_script("return window.performance.timing.responseStart")
        domComplete = self.driver.execute_script("return window.performance.timing.domComplete")

        ''' Calculate the performance'''
        responsetime_calc = responseStart - navigationStart
        pagefullload_calc = domComplete - responseStart
        round_trip = responsetime_calc + pagefullload_calc

        print("Response time: {} ms".format(str(responsetime_calc)))
        print("Page full load time: {} ms".format(str(pagefullload_calc)))
        print("Round trip : {} ms".format(str(round_trip)))


        self.driver.maximize_window()  # maximize window
        self.driver.get_screenshot_as_file('PageLoad.png')
        # except:
        #     self.WriteToLog(self.fileName, "ERROR - error occurred during facebook home page upload")
            ###################################################################################
        # locate email field and enter email
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, 'email'))).send_keys('shai.qa.nice@gmail.com')
            time.sleep(2)

        except:
            self.WriteToLog(self.fileName,"Can't find email field - loginToFacebook Test failed" )
            # driver.quit()

        # locate password field and enter password
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, 'pass'))).send_keys('XXXXXX!')
            time.sleep(3)
        except:
            self.WriteToLog(self.fileName, "Can't find password field - loginToFacebook Test failed")
            pass

        # locate Login button and press it
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//input[@value="Log In"]'))).click()
            # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'u_0_2'))).click()
            time.sleep(2)
        except:
            self.WriteToLog(self.fileName, "Can't find password field - loginToFacebook Test failed")
            pass

        self.driver.get_screenshot_as_file("FB Login With Valid Details.png")
        self.WriteToLog(self.fileName,"Ending with FBLoginWithValidDetails test ")

        self.driver.quit()


# Needed if you would like to run this plan within this file
if __name__=='__main__':
    FBValidDetails().FBLoginWithValidDetailsTest()

