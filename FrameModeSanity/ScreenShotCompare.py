#Shai Adani
#29/2/2020
#https://pysource.com/2018/07/19/check-if-two-images-are-equal-with-opencv-and-python/

##############################################################
# import relevant modules
from selenium import webdriver
import cv2
from selenium.webdriver.common.keys import Keys
import time, unittest, HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import Automation.Environment
import Automation.Functions

#
# Test Steps
# * Read URLs from external file
# 1 - Open URL in non shield mode
# 2 - Save screenshot
# 3 - Open URL in shield mode
# 4 - Save screenshot
# 5 - Compare screenshots and update results


class URLScreenshotCompare(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.file = Automation.Environment.urls_file




    def test_a_url_screenshots_compare(self):
        # Read URLs from file
        self.lines = Automation.Functions.ReadURLS(self.file)

        for line in self.lines:
            # Set browser type browser
            self.browser_type = Automation.Environment.chrome_driver_path
            # Set browser configuration to ON OFF - with or without proxy
            self.shield_status = 'OFF'
            # Initiate browser
            self.browser = Automation.Functions.StartBrowser(self.browser_type, self.shield_status)
            # Navigate to URL
            Automation.Functions.GoToURL(self.browser, line)
            # Take screenshot
            self.img_no_shield = Automation.Functions.SaveScreenshot(self.browser,
                                                                     Automation.Environment.screenshot_path,
                                                                     self.shield_status)
            time.sleep(3)
            Automation.Functions.CloseBrowser(self.browser)
            time.sleep(3)

            # Set browser type browser
            self.browser_type = Automation.Environment.chrome_driver_path
            # Set browser configuration to ON OFF - with or without proxy
            self.shield_status = 'ON'
            # Initiate browser
            self.browser = Automation.Functions.StartBrowser(self.browser_type, self.shield_status)
            # Navigate to URL
            Automation.Functions.GoToURL(self.browser, line)
            # Take screenshot
            self.img_shield = Automation.Functions.SaveScreenshot(self.browser,
                                                                  Automation.Environment.screenshot_path,
                                                                  self.shield_status)
            time.sleep(3)
            Automation.Functions.CloseBrowser(self.browser)
            time.sleep(3)

            Automation.Functions.CompareScreenshots(self.img_no_shield, self.img_shield,
                                                    Automation.Environment.screenshot_path, line,
                                                    Automation.Environment.threshold)



    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()


