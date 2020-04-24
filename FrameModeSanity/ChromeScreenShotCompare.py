#Shai Adani
#29/2/2020
#https://pysource.com/2018/07/19/check-if-two-images-are-equal-with-opencv-and-python/

##############################################################
# import relevant modules
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time, unittest, cv2, HtmlTestRunner
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
import Automation.Environment
import Automation.Functions

class URLScreenshotCompare(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.file = Automation.Environment.urls_file
        # cls.browser_type = browser

    def test_a_url_screenshots_compare_chrome(self):
        Automation.Functions.WriteToLog(Automation.Environment.chrome_results_log_file, 'Chrome URLScreenshotCompare Test started')
        # Read URLs from file
        Automation.Functions.WriteToLog(Automation.Environment.chrome_results_log_file, 'Reading URLs from file')
        Automation.Functions.CreateNewStatisticsFile(Automation.Environment.chrome_statistics_file,
                                                     Automation.Environment.shield_mode,
                                                     Automation.Environment.shield_build)
        self.lines = Automation.Functions.ReadURLS(self.file)

        for line in self.lines:
            # Set browser configuration to ON OFF - with or without proxy
            self.shield_status = 'OFF'
            # Set browser type browser
            self.browser_type = Automation.Environment.chrome_driver_path
            # Set test headless mode
            self.headless_mode = Automation.Environment.healdless_mode
            # Initiate browser
            self.browser = Automation.Functions.StartBrowser(self.browser_type, self.shield_status, self.headless_mode)
            # Navigate to URL
            Automation.Functions.GoToURL(self.browser, line)
            # Take screenshot
            self.img_no_shield = Automation.Functions.SaveScreenshot(self.browser,
                                                                      Automation.Environment.chrome_screenshot_path,
                                                                      self.shield_status)
            time.sleep(3)
            Automation.Functions.CloseBrowser(self.browser)
            time.sleep(3)

            # Set browser type browser
            self.browser_type = Automation.Environment.chrome_driver_path
            # Set browser configuration to ON OFF - with or without proxy
            self.shield_status = 'ON'
            # Initiate browser
            self.browser = Automation.Functions.StartBrowser(self.browser_type, self.shield_status, self.headless_mode)
            # Navigate to URL
            Automation.Functions.GoToURL(self.browser, line)
            # Take screenshot
            self.img_shield = Automation.Functions.SaveScreenshot(self.browser,
                                                                  Automation.Environment.chrome_screenshot_path,
                                                                  self.shield_status)
            time.sleep(3)
            Automation.Functions.CloseBrowser(self.browser)
            time.sleep(3)
            Automation.Functions.CompareScreenshots(self.img_no_shield, self.img_shield,
                                                    Automation.Environment.chrome_screenshot_path, line,
                                                    Automation.Environment.threshold)



    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()



