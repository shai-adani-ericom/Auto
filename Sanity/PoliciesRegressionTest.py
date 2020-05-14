# Prerequisite - new environment is ready


import unittest,UpdateEnvironment, Functions, HtmlTestRunner, datetime, time

env = UpdateEnvironment # change to NewEnvironment in case needed

class policies_regression(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.wait_time = 15
        cls.headless_mode = 0
        cls.chrome_driver_path = env.chrome_driver_path
        cls.firefox_driver_path = env.firefox_driver_path
        cls.admin_address = env.admin_address
        cls.shield_ip = env.shield_ip
        cls.shield_machine_user = env.shield_machine_user
        cls.shield_machine_pass = env.shield_machine_pass
        cls.branch = env.branch
        cls.chrome_download_folder = env.chrome_download_folder
        cls.proxy_address = env.proxy_address
        cls.restore_file_path = env.restore_file_path

    # def test_1_policies_general_view(self):
    #     # Verify Policies compact mode by default
    #     Functions.PrintText('Start test_1_policies_general_view')
    #     self.admin_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path,'OFF', self.headless_mode, self.proxy_address)
    #     Functions.AdminLogin(self.admin_driver, self.wait_time, self.admin_address)
    #     # Go to Policies page
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="el_1"]/a/span')
    #     # Check default compact view
    #     res = Functions.VerifyElementInvisibility(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="policies-grid"]/vaadin-grid-cell-content[6]/div/vaadin-grid-sorter')
    #     if res == 1:
    #         Functions.PrintText('Download column invisible step - *PASS*')
    #     # Change to Verbose mode
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="toggle-data"]/i')
    #     # Check additional columns visibility
    #     object_recognizers_by_xpath = ['//*[@id="policies-grid"]/vaadin-grid-cell-content[1]',
    #                                    '//*[@id="policies-grid"]/vaadin-grid-cell-content[2]',
    #                                    '//*[@id="policies-grid"]/vaadin-grid-cell-content[3]',
    #                                    '//*[@id="policies-grid"]/vaadin-grid-cell-content[4]',
    #                                    '//*[@id="policies-grid"]/vaadin-grid-cell-content[5]',
    #                                    '//*[@id="policies-grid"]/vaadin-grid-cell-content[6]',
    #                                    '//*[@id="policies-grid"]/vaadin-grid-cell-content[7]',
    #                                    '//*[@id="policies-grid"]/vaadin-grid-cell-content[8]',
    #                                    '//*[@id="policies-grid"]/vaadin-grid-cell-content[9]',
    #                                    '//*[@id="policies-grid"]/vaadin-grid-cell-content[10]',
    #                                    '//*[@id="policies-grid"]/vaadin-grid-cell-content[11]',
    #                                    '//*[@id="policies-grid"]/vaadin-grid-cell-content[12]',
    #                                    '//*[@id="policies-grid"]/vaadin-grid-cell-content[13]',
    #                                    '//*[@id="policies-grid"]/vaadin-grid-cell-content[14]',
    #                                    '//*[@id="policies-grid"]/vaadin-grid-cell-content[15]',
    #                                    '//*[@id="policies-grid"]/vaadin-grid-cell-content[16]']
    #     # for object_recognizer in object_recognizers_by_xpath:
    #     #     Functions.VerifyElementIsVisible(self.admin_driver, self.wait_time, 'XPATH', object_recognizer)
    #     Functions.PrintText('All columns are visible in Verbose mode step - *PASS*')
    #     # Check sort on Domain\Category column
    #     time.sleep(2)
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="policies-grid"]/vaadin-grid-cell-content[2]')
    #     time.sleep(2)
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
    #                             '//*[@id="policies-grid"]/vaadin-grid-cell-content[2]')
    #     time.sleep(2)
    #     Functions.CheckObjectText(self.admin_driver, self.wait_time, 'XPATH', '//*[@slot="vaadin-grid-cell-content-69"]',
    #                              'safebrowsing-cache.google.com', focus='ON')
    #     time.sleep(2)
    #     Functions.PrintText('Column Domain\Category has been successfully sorted step - *PASS*')
    #     self.admin_driver.quit()
    #
    #     # select the Default - All and click the Edit option.Go over each policy and check all values exist (in the drop down list):
    #
    #     Functions.PoliciesValuesExists('chromedriver', UpdateEnvironment.chrome_driver_path,'OFF',
    #                              UpdateEnvironment.headless_mode, UpdateEnvironment.proxy_address,
    #                              10, UpdateEnvironment.admin_address )
    #
    #
    # def test_2_policies_regression_override_policy(self):
    #     Functions.PrintText('Start test_2_policies_regression_override_policy ')
    #
    #     # Set policies configuration
    #     kwargs = {'access':'Shield', 'upload':'Enabled', 'cookies':'Disable', 'media':'Stream',
    #               'suspend':'1h', 'clipboard':'Enable', 'certificate':'Ignore', 'adblock': 'Enable'}
    #     Functions.PoliciesConfig('chromedriver', UpdateEnvironment.chrome_driver_path,'OFF',
    #                              UpdateEnvironment.headless_mode, UpdateEnvironment.proxy_address,
    #                              10, UpdateEnvironment.admin_address, **kwargs )
    #     # Set Override media = Crystal and verify shield in Crystal mode instead of Stream mode
    #     self.admin_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path,'OFF', self.headless_mode, self.proxy_address)
    #     Functions.AdminLogin(self.admin_driver, self.wait_time, self.admin_address)
    #     # Go to Policies page
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="el_1"]/a/span')
    #     time.sleep(2)
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="content"]/div/div/div[1]/div/div[3]/ul/li[3]/i')
    #     time.sleep(2)
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
    #                             '//*[@id="policies-grid"]/vaadin-grid-cell-content[86]/vaadin-checkbox')
    #     time.sleep(2)
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
    #                             '//*[@id="content"]/div/div/div[1]/div/div[1]/ul/li[2]/i')
    #     time.sleep(2)
    #     Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'NAME','media', 'Crystal')
    #     time.sleep(2)
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
    #                             '//*[@id="middle"]/div[2]/cc-modal/div/div/div/div[3]/table/tbody/tr/td[2]/div/button[1]')
    #     time.sleep(2)
    #     self.admin_driver.quit()
    #     # Browsing to google via shield and verify it is on Crystal mode
    #     Functions.PrintText('Browsing to google via shield and verify it is on Crystal mode')
    #     # Start Chrome browser
    #     self.client_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON',
    #                                                           self.headless_mode, self.proxy_address)
    #     # Go to specific web page
    #     self.url = 'https://www.google.com/'
    #     # Go to URL in mode
    #     Functions.GoToURL(self.client_driver, self.url, 0)
    #     # Wait for page Access now page to be loaded and switch to frame
    #     Functions.SwitchToFrame(self.client_driver, self.wait_time, 'ID', 'crystal-frame-top')
    #     # Enter text to field
    #     Functions.EnterTextToField(self.client_driver, self.wait_time, 'NAME', 'q', 'Shai Adani')
    #     Functions.HitEnter()
    #     # Close Client browser
    #     self.client_driver.quit()
    #     Functions.PrintText('Override functionality OK - system is in Crystal mode instead of Stream mode step - *PASS*')
    #     Functions.PrintText('Go to google web page in proxy less mode and verify it  works in Crystal mode as defined in new policy')
    #     # Start Chrome browser
    #     self.client_driver_proxyless = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'OFF',
    #                                                           self.headless_mode, self.proxy_address)
    #     # Go to specific web page
    #     self.url = 'https://www.google.com/'
    #     self.proxyless_url = 'https://' + self.shield_ip + ':30443' + '/?url=' + self.url
    #     # Go to URL in proxyless mode
    #     Functions.GoToURL(self.client_driver_proxyless, self.proxyless_url, 0)
    #     # Wait for page Access now page to be loaded and switch to frame
    #     Functions.SwitchToFrame(self.client_driver_proxyless, self.wait_time, 'ID', 'crystal-frame-top')
    #     # Enter text to field
    #     Functions.EnterTextToField(self.client_driver_proxyless, self.wait_time, 'NAME', 'q', 'Shai Adani')
    #     Functions.HitEnter()
    #     # # Close Client browser
    #     Functions.PrintText('Close client - proxyless mode')
    #     self.client_driver_proxyless.quit()
    #     Functions.PrintText('Override functionality proxy less OK - system is in Crystal mode instead of Stream mode step - *PASS*')
    #
    #     # Return Override configuration to default
    #     kwargs = {'media': 'Default'}
    #     Functions.OverrideConfig('chromedriver', UpdateEnvironment.chrome_driver_path,'OFF',
    #                              UpdateEnvironment.headless_mode, UpdateEnvironment.proxy_address,
    #                              10, UpdateEnvironment.admin_address, **kwargs)
    #
    # def test_3_policies_regression_new_policy(self):
    #     Functions.PrintText('Start test_3_policies_regression_new_policy ')
    #     # Create new policy for www.google.com
    #     domains_names = ['www.google.com'] # Bug with Enter after last domain's name
    #     kwargs = {'media': 'Crystal'}
    #     Functions.AddNewPolicy('chromedriver', UpdateEnvironment.chrome_driver_path,'OFF',
    #                              UpdateEnvironment.headless_mode, UpdateEnvironment.proxy_address,
    #                              10, UpdateEnvironment.admin_address, *domains_names, **kwargs )
    #     # Go to google web page and verify it  works in Crystal mode
    #     Functions.PrintText(
    #         'Go to google web page and verify it  works in Crystal mode as defined in new policy')
    #     self.client_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON',
    #                                                           self.headless_mode, self.proxy_address)
    #     self.url = 'https://www.google.com/'
    #     # Go to URL in mode
    #     Functions.GoToURL(self.client_driver, self.url, 0)
    #     # Wait for page Access now page to be loaded and switch to frame
    #     Functions.SwitchToFrame(self.client_driver, self.wait_time, 'ID', 'crystal-frame-top')
    #     # Enter text to field
    #     Functions.EnterTextToField(self.client_driver, self.wait_time, 'NAME', 'q', 'Shai Adani')
    #     Functions.HitEnter()
    #     # Close Client browser
    #     self.client_driver.quit()
    #     # Go to google web page in proxy less mode and verify it  works in Crystal mode
    #     Functions.PrintText('Go to google web page in proxy less mode and verify it  works in Crystal mode as defined in new policy')
    #     # Start Chrome browser
    #     self.client_driver_proxyless = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'OFF',
    #                                                           self.headless_mode, self.proxy_address)
    #     # Go to specific web page
    #     self.url = 'https://www.google.com/'
    #     self.proxyless_url = 'https://' + self.shield_ip + ':30443' + '/?url=' + self.url
    #     # Go to URL in proxyless mode
    #     Functions.GoToURL(self.client_driver_proxyless, self.proxyless_url, 0)
    #     # Wait for page Access now page to be loaded and switch to frame
    #     Functions.SwitchToFrame(self.client_driver_proxyless, self.wait_time, 'ID', 'crystal-frame-top')
    #     # Enter text to field
    #     Functions.EnterTextToField(self.client_driver_proxyless, self.wait_time, 'NAME', 'q', 'Shai Adani')
    #     Functions.HitEnter()
    #     # # Close Client browser
    #     Functions.PrintText('Close client - proxyless mode')
    #     self.client_driver_proxyless.quit()
    #     Functions.PrintText('New Policy functionality OK - system is in Crystal mode instead of Stream mode for www.google.com in poroxy less mode step - *PASS*')
    #
    # def test_4_policies_access(self):
    #     Functions.PrintText('Start test_4_policies_access ')
    #
    #     # Config default policy to shield + Crystal
    #     # Set policies configuration
    #     kwargs = {'access':'Shield', 'media':'Crystal'}
    #     Functions.PoliciesConfig('chromedriver', UpdateEnvironment.chrome_driver_path,'OFF',
    #                              UpdateEnvironment.headless_mode, UpdateEnvironment.proxy_address,
    #                              10, UpdateEnvironment.admin_address, **kwargs )
    #     # open URL and verify it was loaded in shield\crystal mode mode
    #     Functions.PrintText('open URL and verify it was loaded in shield\crystal mode mode')
    #     # Start Chrome browser
    #     self.client_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON',
    #                                                           self.headless_mode, self.proxy_address)
    #     # Go to specific web page
    #     self.url = 'https://www.google.com/'
    #     # Go to URL in mode
    #     Functions.GoToURL(self.client_driver, self.url, 0)
    #     # Wait for page Access now page to be loaded and switch to frame
    #     Functions.SwitchToFrame(self.client_driver, self.wait_time, 'ID', 'crystal-frame-top')
    #     # Enter text to field
    #     Functions.EnterTextToField(self.client_driver, self.wait_time, 'NAME', 'q', 'Shai Adani')
    #     Functions.HitEnter()
    #     # Close Client browser
    #     self.client_driver.quit()
    #     Functions.PrintText('Access shield step - *PASS*')
    #     Functions.PrintText('Go to google web page in proxy less mode and verify it is being accessed via shield')
    #     # Start Chrome browser
    #     self.client_driver_proxyless = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'OFF',
    #                                                           self.headless_mode, self.proxy_address)
    #     # Go to specific web page
    #     self.url = 'https://www.google.com/'
    #     self.proxyless_url = 'https://' + self.shield_ip + ':30443' + '/?url=' + self.url
    #     # Go to URL in proxyless mode
    #     Functions.GoToURL(self.client_driver_proxyless, self.proxyless_url, 0)
    #     # Wait for page Access now page to be loaded and switch to frame
    #     Functions.SwitchToFrame(self.client_driver_proxyless, self.wait_time, 'ID', 'crystal-frame-top')
    #     # Enter text to field
    #     Functions.EnterTextToField(self.client_driver_proxyless, self.wait_time, 'NAME', 'q', 'Shai Adani')
    #     Functions.HitEnter()
    #     # # Close Client browser
    #     Functions.PrintText('Close client - proxyless mode')
    #     self.client_driver_proxyless.quit()
    #     Functions.PrintText('Access shield proxy less step - *PASS*')
    #
    #     # Config default policy to white
    #     # Set policies configuration
    #     kwargs = {'access':'White', 'media':'Crystal'}
    #     Functions.PoliciesConfig('chromedriver', UpdateEnvironment.chrome_driver_path,'OFF',
    #                              UpdateEnvironment.headless_mode, UpdateEnvironment.proxy_address,
    #                              10, UpdateEnvironment.admin_address, **kwargs )
    #     # open URL and verify it was loaded in white mode
    #     Functions.PrintText('open URL and verify it was loaded in white mode')
    #     # Start Chrome browser
    #     self.client_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON',
    #                                                           self.headless_mode, self.proxy_address)
    #     # Go to specific web page
    #     self.url = 'https://www.google.com/'
    #     # Go to URL in mode
    #     Functions.GoToURL(self.client_driver, self.url, 0)
    #     #Verify crystal-frame-top iframe is invisible
    #     Functions.VerifyElementInvisibility(self.client_driver, self.wait_time, 'ID', 'crystal-frame-top')
    #     Functions.PrintText('Google was loaded in white mode - step *PASS*')
    #     # Enter text to field
    #     Functions.EnterTextToField(self.client_driver, self.wait_time, 'NAME', 'q', 'Shai Adani')
    #     Functions.HitEnter()
    #     # Close Client browser
    #     self.client_driver.quit()
    #     Functions.PrintText('Access white step - *PASS*')
    #
    #
    #
    #     # Config default policy to black
    #
    #     # Set policies configuration
    #     kwargs = {'access':'Black', 'media':'Crystal'}
    #     Functions.PoliciesConfig('chromedriver', UpdateEnvironment.chrome_driver_path,'OFF',
    #                              UpdateEnvironment.headless_mode, UpdateEnvironment.proxy_address,
    #                              10, UpdateEnvironment.admin_address, **kwargs )
    #     # open URL and verify it was loaded in white mode
    #     Functions.PrintText('open URL and verify it was loaded in white mode')
    #     # Start Chrome browser
    #     self.client_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON',
    #                                                           self.headless_mode, self.proxy_address)
    #     # Go to specific web page
    #     self.url = 'https://www.google.com/'
    #     # Go to URL in mode
    #     Functions.GoToURL(self.client_driver, self.url, 0)
    #     # Check if page was blocked
    #     Functions.CheckIfPageBlocked(self.client_driver, self.wait_time)
    #     time.sleep(3)
    #     Functions.PrintText('Access Black step - *PASS*')
    #     self.client_driver.quit()
    #     Functions.PrintText('Go to google web page in proxy less mode and verify it is being blocked')
    #     # Start Chrome browser
    #     self.client_driver_proxyless = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'OFF',
    #                                                           self.headless_mode, self.proxy_address)
    #     # Go to specific web page
    #     self.url = 'https://www.google.com/'
    #     self.proxyless_url = 'https://' + self.shield_ip + ':30443' + '/?url=' + self.url
    #     # Go to URL in proxyless mode
    #     Functions.GoToURL(self.client_driver_proxyless, self.proxyless_url, 0)
    #     # Check if page was blocked
    #     Functions.CheckIfPageBlocked(self.client_driver_proxyless, self.wait_time)
    #     time.sleep(3)
    #     Functions.PrintText('Google was blocked in black mode proxyless - step *PASS*')
    #     self.client_driver_proxyless.quit()
    #     Functions.PrintText('Access Black proxy less step - *PASS*')
    #
    #     # Return system config to Shield\Stream
    #     kwargs = {'access': 'Shield', 'media': 'Stream'}
    #     Functions.PoliciesConfig('chromedriver', UpdateEnvironment.chrome_driver_path, 'OFF',
    #                              UpdateEnvironment.headless_mode, UpdateEnvironment.proxy_address,
    #                              10, UpdateEnvironment.admin_address, **kwargs)

    # def test_5_policies_download(self):  # Disable Preview Enable Sanitize
    #     Functions.PrintText('Start test_5_policies_download ')
    #     # Config default policy to shield + Crystal
    #     # Set policies configuration
    #     kwargs = {'access': 'Shield', 'media': 'Crystal'}
    #     Functions.PoliciesConfig('chromedriver', UpdateEnvironment.chrome_driver_path, 'OFF',
    #                              UpdateEnvironment.headless_mode, UpdateEnvironment.proxy_address,
    #                              10, UpdateEnvironment.admin_address, **kwargs)
    #     # Set Download = Disable
    #     self.admin_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path,'OFF', self.headless_mode, self.proxy_address)
    #     Functions.AdminLogin(self.admin_driver, self.wait_time, self.admin_address)
    #     # Go to Policies page
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="el_1"]/a/span')
    #     # Edit Default - All Domain
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
    #                             '//*[@id="policies-grid"]/vaadin-grid-cell-content[69]/vaadin-checkbox')
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
    #                             '//*[@id="content"]/div/div/div[1]/div/div[1]/ul/li[2]/i')
    #     # Policies - Edit Default - All Domain
    #     Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'XPATH',
    #                                    '//*[@id="middle"]/div[2]/cc-modal/div/div/div/div[2]/dcl-wrapper/edit-defaults-modal-body-class/div/div/div/form/div/table/tbody/tr[1]/td[4]/select', 'Disable')
    #
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
    #                             '//*[@id="middle"]/div[2]/cc-modal/div/div/div/div[3]/table/tbody/tr/td[2]/div/button[1]')
    #     self.admin_driver.quit()
    #
    #     # Open Chrome Browser and verify download option is invisible
    #     Functions.PrintText('Open Chrome Browser and verify download option is invisible in Disable mode')
    #     # Start Chrome browser
    #     self.client_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON', self.headless_mode, self.proxy_address)
    #     # Go to specific web page
    #     self.url = 'https://www.ericom.com/doc/TechnicalReferences/EricomBlazeAdminManual.pdf'
    #     Functions.GoToURL(self.client_driver, self.url, 0)
    #     # Wait for page Access now page to be loaded and switch to frame
    #     Functions.SwitchToFrame(self.client_driver, self.wait_time, 'ID', 'crystal-frame-top')
    #     # Verify print\download buttons are invisible
    #     Functions.VerifyElementInvisibility(self.client_driver, self.wait_time, 'ID', 'download')
    #     self.client_driver.quit()
    #     Functions.PrintText('Download - Disable step - *PASS*')
    #
    #     # Set Download = Preview
    #     self.admin_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path,'OFF', self.headless_mode, self.proxy_address)
    #     Functions.AdminLogin(self.admin_driver, self.wait_time, self.admin_address)
    #     # Go to Policies page
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="el_1"]/a/span')
    #     # Edit Default - All Domain
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
    #                             '//*[@id="policies-grid"]/vaadin-grid-cell-content[69]/vaadin-checkbox')
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
    #                             '//*[@id="content"]/div/div/div[1]/div/div[1]/ul/li[2]/i')
    #     # Policies - Edit Default - All Domain
    #     Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'XPATH',
    #                                    '//*[@id="middle"]/div[2]/cc-modal/div/div/div/div[2]/dcl-wrapper/edit-defaults-modal-body-class/div/div/div/form/div/table/tbody/tr[1]/td[4]/select', 'Disable')
    #
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
    #                             '//*[@id="middle"]/div[2]/cc-modal/div/div/div/div[3]/table/tbody/tr/td[2]/div/button[1]')
    #     self.admin_driver.quit()
    #
    #     # Open Chrome Browser and verify download option is invisible
    #     Functions.PrintText('Open Chrome Browser and verify download option is invisible in Preview mode')
    #     # Start Chrome browser
    #     self.client_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON', self.headless_mode, self.proxy_address)
    #     # Go to specific web page
    #     self.url = 'https://www.ericom.com/doc/TechnicalReferences/EricomBlazeAdminManual.pdf'
    #     Functions.GoToURL(self.client_driver, self.url, 0)
    #     # Wait for page Access now page to be loaded and switch to frame
    #     Functions.SwitchToFrame(self.client_driver, self.wait_time, 'ID', 'crystal-frame-top')
    #     # Verify print\download buttons are invisible
    #     Functions.VerifyElementInvisibility(self.client_driver, self.wait_time, 'ID', 'download')
    #     self.client_driver.quit()
    #     Functions.PrintText('Print - Preview step - *PASS*')
    #
    #     # Set Download = Enable
    #     self.admin_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path,'OFF', self.headless_mode, self.proxy_address)
    #     Functions.AdminLogin(self.admin_driver, self.wait_time, self.admin_address)
    #     # Go to Policies page
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="el_1"]/a/span')
    #     # Edit Default - All Domain
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
    #                             '//*[@id="policies-grid"]/vaadin-grid-cell-content[69]/vaadin-checkbox')
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
    #                             '//*[@id="content"]/div/div/div[1]/div/div[1]/ul/li[2]/i')
    #     # Policies - Edit Default - All Domain
    #     Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'XPATH',
    #                                    '//*[@id="middle"]/div[2]/cc-modal/div/div/div/div[2]/dcl-wrapper/edit-defaults-modal-body-class/div/div/div/form/div/table/tbody/tr[1]/td[4]/select', 'Enable')
    #
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
    #                             '//*[@id="middle"]/div[2]/cc-modal/div/div/div/div[3]/table/tbody/tr/td[2]/div/button[1]')
    #     self.admin_driver.quit()
    #
    #     # Open Chrome Browser and verify print option is visible in Enable mode
    #     Functions.PrintText('Open Chrome Browser and verify download option is visible in Enable mode')
    #     # Start Chrome browser
    #     self.client_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON', self.headless_mode, self.proxy_address)
    #     # Go to specific web page
    #     self.url = 'https://www.ericom.com/doc/TechnicalReferences/EricomBlazeAdminManual.pdf'
    #     Functions.GoToURL(self.client_driver, self.url, 0)
    #     # Wait for page Access now page to be loaded and switch to frame
    #     Functions.SwitchToFrame(self.client_driver, self.wait_time, 'ID', 'crystal-frame-top')
    #     time.sleep(5)
    #     # Go to online PDF file, download and verify it was downloaded
    #     Functions.VerifyFileDownload(self.client_driver, self.wait_time, 'ID', 'download', self.chrome_download_folder, 'EricomBlazeAdminManual.pdf')
    #     time.sleep(5)
    #     # Close Client browser
    #     self.client_driver.quit()
    #     Functions.PrintText('Print - Enable step - *PASS*')
    #
    #
    #     # Set Download = Sanitize
    #     self.admin_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path,'OFF', self.headless_mode, self.proxy_address)
    #     Functions.AdminLogin(self.admin_driver, self.wait_time, self.admin_address)
    #     # Go to Policies page
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="el_1"]/a/span')
    #     # Edit Default - All Domain
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
    #                             '//*[@id="policies-grid"]/vaadin-grid-cell-content[69]/vaadin-checkbox')
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
    #                             '//*[@id="content"]/div/div/div[1]/div/div[1]/ul/li[2]/i')
    #     # Policies - Edit Default - All Domain
    #     Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'XPATH',
    #                                    '//*[@id="middle"]/div[2]/cc-modal/div/div/div/div[2]/dcl-wrapper/edit-defaults-modal-body-class/div/div/div/form/div/table/tbody/tr[1]/td[4]/select', 'Sanitize')
    #
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
    #                             '//*[@id="middle"]/div[2]/cc-modal/div/div/div/div[3]/table/tbody/tr/td[2]/div/button[1]')
    #     self.admin_driver.quit()
    #
    #     # Open Chrome Browser and verify print option is visible in Sanitize mode
    #     Functions.PrintText('Open Chrome Browser and verify download option is visible in Sanitizeable mode')
    #     # Start Chrome browser
    #     self.client_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON', self.headless_mode, self.proxy_address)
    #     # Go to specific web page
    #     self.url = 'https://www.ericom.com/doc/TechnicalReferences/EricomBlazeAdminManual.pdf'
    #     Functions.GoToURL(self.client_driver, self.url, 0)
    #     # Wait for page Access now page to be loaded and switch to frame
    #     Functions.SwitchToFrame(self.client_driver, self.wait_time, 'ID', 'crystal-frame-top')
    #     time.sleep(5)
    #     # Go to online PDF file, download and verify it was downloaded
    #     Functions.VerifyFileDownload(self.client_driver, self.wait_time, 'ID', 'download', self.chrome_download_folder, 'EricomBlazeAdminManual.pdf')
    #     time.sleep(5)
    #     # Close Client browser
    #     self.client_driver.quit()
    #     Functions.PrintText('Download - Sanitize step - *PASS*')
    #
    #     # Check File Transfer - All - Last 15 minutes report
    #     # Admin Login
    #     self.admin_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'OFF', self.headless_mode,
    #                                                self.proxy_address)
    #     Functions.AdminLogin(self.admin_driver, self.wait_time, self.admin_address)
    #     # Go to Reports page
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="el_4"]/a/span')
    #     Functions.PrintText(
    #         'Check File Transfer - All - Last 15 minutes report')
    #     Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'NAME', 'selectCategory', 'File Transfer')
    #     time.sleep(2)
    #     Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'NAME', 'selectReport', 'All')
    #     time.sleep(2)
    #     Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'NAME', 'selectTime',
    #                                    'Last 15 minutes') #Last 15 minutes
    #     time.sleep(2)
    #     # Run
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'CSS_SELECTOR',
    #                             '#content > table > tbody > tr:nth-child(1) > td:nth-child(5) > button')
    #     time.sleep(5)
    #     # Search word in report
    #     words = ['EricomBlazeAdminManual','pdf','1.3 MB','Sanitize','Download','Success']
    #     Functions.SearchValuesInTable(self.admin_driver, self.wait_time, '//*[@id="file_transfer_summary_report"]/tbody', *words)#//*[@id="content"]/table
    #     time.sleep(3)
    #     words = ['EricomBlazeAdminManual', 'pdf', '1.3 MB', 'Enable', 'Download', 'Success']
    #     Functions.SearchValuesInTable(self.admin_driver, self.wait_time,
    #                                    '//*[@id="file_transfer_summary_report"]/tbody',*words)  # //*[@id="content"]/table
    #     time.sleep(3)
    #     Functions.PrintText('Download test - *PASS*')
    #     self.admin_driver.quit()


    # def test_6_policies_readonly(self):  # Interactive Crystal, Read-Only Stream # Bug with Read-Olny Crystal
    #     Functions.PrintText('Start test_6_policies_readonly ')
    #     # Config default policy to shield + Crystal
    #     # Set policies configuration
    #     kwargs = {'access': 'Shield', 'media': 'Crystal'}
    #     Functions.PoliciesConfig('chromedriver', UpdateEnvironment.chrome_driver_path, 'OFF',
    #                              UpdateEnvironment.headless_mode, UpdateEnvironment.proxy_address,
    #                              10, UpdateEnvironment.admin_address, **kwargs)
    #     self.admin_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path,'OFF', self.headless_mode, self.proxy_address)
    #     Functions.AdminLogin(self.admin_driver, self.wait_time, self.admin_address)
    #     # Go to Policies page
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="el_1"]/a/span')
    #     # Edit Default - All Domain
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
    #                             '//*[@id="policies-grid"]/vaadin-grid-cell-content[69]/vaadin-checkbox')
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
    #                             '//*[@id="content"]/div/div/div[1]/div/div[1]/ul/li[2]/i')
    #     # Policies - Edit Default - All Domain
    #     Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'XPATH',
    #                                    '//*[@id="middle"]/div[2]/cc-modal/div/div/div/div[2]/dcl-wrapper/edit-defaults-modal-body-class/div/div/div/form/div/table/tbody/tr[2]/td[2]/select', 'Interactive')
    #
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
    #                             '//*[@id="middle"]/div[2]/cc-modal/div/div/div/div[3]/table/tbody/tr/td[2]/div/button[1]')
    #     self.admin_driver.quit()
    #
    #     # Open Chrome Browser and verify that text can be entered into web page text field
    #     Functions.PrintText('Open Chrome Browser and verify that text can be entered into web page text field')
    #     # Start Chrome browser
    #     self.client_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON', self.headless_mode, self.proxy_address)
    #     # Go to specific web page
    #     self.url = 'https://www.google.com/'
    #     Functions.GoToURL(self.client_driver, self.url, 0)
    #     # Wait for page Access now page to be loaded and switch to frame
    #     Functions.SwitchToFrame(self.client_driver, self.wait_time, 'ID', 'crystal-frame-top')
    #     time.sleep(2)
    #     # Enter text to field
    #     Functions.EnterTextToField(self.client_driver, self.wait_time, 'NAME', 'q', 'Shai Adani')
    #     time.sleep(2)
    #     Functions.CheckObjectTextByFieldValue(self.client_driver, self.wait_time, 'NAME', 'q',
    #                                  'Shai Adani', focus='ON')
    #     self.client_driver.quit()
    #     Functions.PrintText('Read-Only/Crystal - Interactive step - *PASS*')
    #
    #
    #     # Config default policy to shield + Stream
    #     # Set policies configuration
    #     kwargs = {'access': 'Shield', 'media': 'Stream'}
    #     Functions.PoliciesConfig('chromedriver', UpdateEnvironment.chrome_driver_path, 'OFF',
    #                              UpdateEnvironment.headless_mode, UpdateEnvironment.proxy_address,
    #                              10, UpdateEnvironment.admin_address, **kwargs)
    #     self.admin_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path,'OFF', self.headless_mode, self.proxy_address)
    #     Functions.AdminLogin(self.admin_driver, self.wait_time, self.admin_address)
    #     # Go to Policies page
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="el_1"]/a/span')
    #     # Edit Default - All Domain
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
    #                             '//*[@id="policies-grid"]/vaadin-grid-cell-content[69]/vaadin-checkbox')
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
    #                             '//*[@id="content"]/div/div/div[1]/div/div[1]/ul/li[2]/i')
    #     # Policies - Edit Default - All Domain
    #     Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'XPATH',
    #                                    '//*[@id="middle"]/div[2]/cc-modal/div/div/div/div[2]/dcl-wrapper/edit-defaults-modal-body-class/div/div/div/form/div/table/tbody/tr[2]/td[2]/select', 'Read-Only')
    #
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
    #                             '//*[@id="middle"]/div[2]/cc-modal/div/div/div/div[3]/table/tbody/tr/td[2]/div/button[1]')
    #     self.admin_driver.quit()
    #
    #     # Open Chrome Browser and verify that text can be entered into web page text field
    #     Functions.PrintText('Open Chrome Browser and verify that Read-Only Mode message appears')
    #     # Start Chrome browser
    #     self.client_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON', self.headless_mode, self.proxy_address)
    #     # Go to specific web page
    #     self.url = 'https://www.youtube.com/'
    #     Functions.GoToURL(self.client_driver, self.url, 0)
    #     # Wait for page Access now page to be loaded and switch to frame
    #     # Functions.SwitchToFrame(self.client_driver, self.wait_time, 'ID', 'ifrm_download')
    #     time.sleep(2)
    #     self.client_driver.refresh()
    #     Functions.VerifyElementIsVisible(self.client_driver, self.wait_time, 'XPATH', '//*[@id="toast-container"]/div')
    #     Functions.PrintText('Read-Only Mode message appears step - *PASS*')
    #     self.client_driver.quit()


    # def test_7_policies_print(self):
    #
    #     Functions.PrintText('Start test_7_policies_print ')
    #
    #     # Config default policy to shield + Stream Download = Enabled Print = Enable
    #     # Set policies configuration
    #     kwargs = {'access': 'Shield', 'media': 'Stream', 'printing': 'Enable'}
    #     Functions.PoliciesConfig('chromedriver', UpdateEnvironment.chrome_driver_path, 'OFF',
    #                              UpdateEnvironment.headless_mode, UpdateEnvironment.proxy_address,
    #                              10, UpdateEnvironment.admin_address, **kwargs)
    #     # Set Download = Enable
    #     self.admin_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path,'OFF', self.headless_mode, self.proxy_address)
    #     Functions.AdminLogin(self.admin_driver, self.wait_time, self.admin_address)
    #     # Go to Policies page
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="el_1"]/a/span')
    #     time.sleep(2)
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="policies-grid"]/vaadin-grid-cell-content[69]/vaadin-checkbox')
    #     time.sleep(2)
    #
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
    #                             '//*[@id="content"]/div/div/div[1]/div/div[1]/ul/li[2]/i')
    #     time.sleep(2)
    #     Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'XPATH',
    #                                    '//*[@id="middle"]/div[2]/cc-modal/div/div/div/div[2]/dcl-wrapper/edit-defaults-modal-body-class/div/div/div/form/div/table/tbody/tr[1]/td[4]/select', 'Enable')
    #     time.sleep(2)
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
    #                             '//*[@id="middle"]/div[2]/cc-modal/div/div/div/div[3]/table/tbody/tr/td[2]/div/button[1]')
    #     time.sleep(2)
    #     self.admin_driver.quit()
    #
    #     # Start Chrome browser
    #     self.client_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON', self.headless_mode, self.proxy_address)
    #     # Go to specific web page
    #     self.url = 'http://unec.edu.az/application/uploads/2014/12/pdf-sample.pdf'
    #     Functions.GoToURL(self.client_driver, self.url, 0)
    #     time.sleep(5)
    #     Functions.SendPrintShortkey()
    #     time.sleep(5)
    #     Functions.PrintText('Go to printer and verify file 1 was printed')
    #     self.client_driver.quit()
    #
    #
    #     # Config default policy to shield + Stream Download = Enabled Print = Protected
    #     # Set policies configuration
    #     kwargs = {'access': 'Shield', 'media': 'Stream', 'printing': 'Protected'}
    #     Functions.PoliciesConfig('chromedriver', UpdateEnvironment.chrome_driver_path, 'OFF',
    #                              UpdateEnvironment.headless_mode, UpdateEnvironment.proxy_address,
    #                              10, UpdateEnvironment.admin_address, **kwargs)
    #     # Set Download = Enable
    #     self.admin_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path,'OFF', self.headless_mode, self.proxy_address)
    #     Functions.AdminLogin(self.admin_driver, self.wait_time, self.admin_address)
    #     # Go to Policies page
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="el_1"]/a/span')
    #     time.sleep(2)
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="policies-grid"]/vaadin-grid-cell-content[69]/vaadin-checkbox')
    #     time.sleep(2)
    #
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
    #                             '//*[@id="content"]/div/div/div[1]/div/div[1]/ul/li[2]/i')
    #     time.sleep(2)
    #     Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'XPATH',
    #                                    '//*[@id="middle"]/div[2]/cc-modal/div/div/div/div[2]/dcl-wrapper/edit-defaults-modal-body-class/div/div/div/form/div/table/tbody/tr[1]/td[4]/select', 'Enable')
    #     time.sleep(2)
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
    #                             '//*[@id="middle"]/div[2]/cc-modal/div/div/div/div[3]/table/tbody/tr/td[2]/div/button[1]')
    #     time.sleep(2)
    #     self.admin_driver.quit()
    #
    #
    #     # Start Chrome browser
    #     self.client_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON', self.headless_mode, self.proxy_address)
    #     # Go to specific web page
    #     self.url = 'http://unec.edu.az/application/uploads/2014/12/pdf-sample.pdf'
    #     Functions.GoToURL(self.client_driver, self.url, 0)
    #     time.sleep(5)
    #     Functions.SendPrintShortkey()
    #     time.sleep(5)
    #     Functions.PrintText('Go to printer and verify file 2 was printed')
    #     Functions.PrintText('Print - Protected step - *PASS*')
    #     self.client_driver.quit()
    #
    #     # Config default policy to shield + Crystal Download = Enabled Print = Disable
    #     # Set policies configuration
    #     kwargs = {'access': 'Shield', 'media': 'Crystal', 'printing': 'Disable'}
    #     Functions.PoliciesConfig('chromedriver', UpdateEnvironment.chrome_driver_path, 'OFF',
    #                              UpdateEnvironment.headless_mode, UpdateEnvironment.proxy_address,
    #                              10, UpdateEnvironment.admin_address, **kwargs)
    #
    #     # Start Chrome browser
    #     self.client_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON', self.headless_mode, self.proxy_address)
    #     # Go to specific web page
    #     self.url = 'http://unec.edu.az/application/uploads/2014/12/pdf-sample.pdf'
    #     Functions.GoToURL(self.client_driver, self.url, 0)
    #     # Wait for page Access now page to be loaded and switch to frame
    #     Functions.SwitchToFrame(self.client_driver, self.wait_time, 'ID', 'crystal-frame-top')
    #     # Verify print\download buttons are invisible
    #     Functions.VerifyElementInvisibility(self.client_driver, self.wait_time, 'ID', 'print')
    #     # Functions.PressOnObject(self.client_driver, self.wait_time, 'ID', 'print') # Crystal Bug - Print button is not responding
    #     time.sleep(5)
    #     Functions.PrintText('Print - Disable step - *PASS*')
    #     self.client_driver.quit()

    # def test_8_policies_suspend(self):
    #     Functions.PrintText('Start test_8_policies_suspend ')
    #     # Set policies configuration
    #     kwargs = {'access': 'Shield', 'media': 'Stream', 'suspend': 'Enable'}
    #     Functions.PoliciesConfig('chromedriver', UpdateEnvironment.chrome_driver_path, 'OFF',
    #                              UpdateEnvironment.headless_mode, UpdateEnvironment.proxy_address,
    #                              10, UpdateEnvironment.admin_address, **kwargs)
    #     # Set Resources config
    #     self.admin_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path,'OFF', self.headless_mode, self.proxy_address)
    #     Functions.AdminLogin(self.admin_driver, self.wait_time, self.admin_address)
    #     # Go to Resources page
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="sideNav"]/ul/li[5]/a/span')
    #     time.sleep(2)
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="properties-panel"]/div/form/div/div/cc-toggle[2]/div/label')
    #     time.sleep(2)
    #     # Set Suspend R/O tab timeout = 1
    #     Functions.EnterTextToField(self.admin_driver, self.wait_time, 'NAME', 'ShortBackgroundIdleTimeoutSeconds', '1')
    #     time.sleep(2)
    #     # Set Suspend R/W tab timeout = 1
    #     Functions.EnterTextToField(self.admin_driver, self.wait_time, 'NAME', 'BackgroundIdleTimeoutSeconds', '1')
    #     time.sleep(2)
    #     Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="wrapper"]/app-root/cc-container-with-menu/cc-pool-container/cc-pool/div/div[2]/button[1]')
    #     time.sleep(2)
    #     self.admin_driver.quit()
    #
    #    # Open Wikipedia and wait for R\O timeout
    #     Functions.PrintText('Open Wikipedia and wait for R\O timeout')
    #     # Start Chrome browser
    #     self.client_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON',
    #                                                           self.headless_mode, self.proxy_address)
    #     # Go to specific web page
    #     self.url = 'https://en.wikipedia.org/wiki/Main_Page'
    #     # Go to URL in mode
    #     Functions.GoToURL(self.client_driver, self.url, 0)
    #     time.sleep(80)
    #     Functions.VerifyElementIsVisible(self.client_driver, self.wait_time, 'XPATH', '/html/body/div/h1')
    #     Functions.PrintText('Suspend - Read Only - session timeout message appears -  step - *PASS*')
    #     self.client_driver.refresh()
    #     time.sleep(15)
    #     Functions.VerifyElementAppearsInPageSource(self.client_driver, self.wait_time, 'XPATH', '//*[@id="shield-shared-frame"]')
    #     Functions.PrintText('Suspend - Read Only - page loaded after timeout refresh -  step - *PASS*')
    #     # Close Client browser
    #     self.client_driver.quit()
    #
    #     # Set Policies - Suspend - Disable and verify no session timeout after 1 minutes
    #     # Set policies configuration
    #     kwargs = {'suspend': 'Disable'}
    #     Functions.PoliciesConfig('chromedriver', UpdateEnvironment.chrome_driver_path, 'OFF',
    #                              UpdateEnvironment.headless_mode, UpdateEnvironment.proxy_address,
    #                              10, UpdateEnvironment.admin_address, **kwargs)
    #
    #    # Open Wikipedia and wait for R\O timeout
    #     Functions.PrintText('Open Wikipedia and wait for R\O timeout')
    #     # Start Chrome browser
    #     self.client_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON',
    #                                                           self.headless_mode, self.proxy_address)
    #     # Go to specific web page
    #     self.url = 'https://en.wikipedia.org/wiki/Main_Page'
    #     # Go to URL in mode
    #     Functions.GoToURL(self.client_driver, self.url, 0)
    #     time.sleep(100)
    #     Functions.VerifyElementInvisibility(self.client_driver, self.wait_time, 'XPATH', '/html/body/div/h1')
    #     Functions.PrintText('Suspend - Disabled - session timeout message did not appear after 1 minute -  step - *PASS*')
    #     # Close Client browser
    #     self.client_driver.quit()
    #
    #
    #     # Set policies configuration
    #     kwargs = {'suspend': '1h'}
    #     Functions.PoliciesConfig('chromedriver', UpdateEnvironment.chrome_driver_path, 'OFF',
    #                              UpdateEnvironment.headless_mode, UpdateEnvironment.proxy_address,
    #                              10, UpdateEnvironment.admin_address, **kwargs)
    #
    #    # Open Wikipedia and wait for R\O timeout
    #     Functions.PrintText('Open Wikipedia and wait for R\O timeout')
    #     # Start Chrome browser
    #     self.client_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON',
    #                                                           self.headless_mode, self.proxy_address)
    #     # Go to specific web page
    #     self.url = 'https://en.wikipedia.org/wiki/Main_Page'
    #     # Go to URL in mode
    #     Functions.GoToURL(self.client_driver, self.url, 0)
    #     time.sleep(120)
    #     Functions.VerifyElementInvisibility(self.client_driver, self.wait_time, 'XPATH', '/html/body/div/h1')
    #     Functions.PrintText('Suspend - 1h - session timeout message not appeared after 1 minute -  step - *PASS*')
    #     time.sleep(3600)
    #     Functions.VerifyElementIsVisible(self.client_driver, self.wait_time, 'XPATH', '/html/body/div/h1')
    #     Functions.PrintText('Suspend - 1h - session timeout message appear after 1 hour -  step - *PASS*')
    #     # Close Client browser
    #     self.client_driver.quit()
    #
    #     #Play youtube movie longer than suspend time and verify it was not suspended
    #     # Set policies configuration
    #     kwargs = {'suspend': 'Enable'}
    #     Functions.PoliciesConfig('chromedriver', UpdateEnvironment.chrome_driver_path, 'OFF',
    #                              UpdateEnvironment.headless_mode, UpdateEnvironment.proxy_address,
    #                              10, UpdateEnvironment.admin_address, **kwargs)
    #     # Open youtube movie and wait for R\O timeout
    #     Functions.PrintText('pen youtube movie and wait for R\O timeout')
    #     # Start Chrome browser
    #     self.client_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON',
    #                                                 self.headless_mode, self.proxy_address)
    #     # Go to specific web page
    #     self.url = 'https://www.youtube.com/watch?v=8SbUC-UaAxE'
    #     # Go to URL in mode
    #     Functions.GoToURL(self.client_driver, self.url, 0)
    #     time.sleep(120)
    #     Functions.VerifyElementInvisibility(self.client_driver, self.wait_time, 'XPATH', '/html/body/div/h1')
    #     Functions.PrintText(
    #         'Suspend - 1 minutes - session timeout message not appeared after 1 minute while playing youtube movie -  step - *PASS*')
    #     # Close Client browser
    #     self.client_driver.quit()

    def test_9_policies_cookies_enable(self):
        Functions.PrintText('Start test_9_policies_cookies_enable ')
        # Set policies configuration
        kwargs = {'access': 'Shield', 'media': 'Crystal', 'suspend': 'Enable', 'cookies': 'Enable'}
        Functions.PoliciesConfig('chromedriver', UpdateEnvironment.chrome_driver_path, 'OFF',
                                 UpdateEnvironment.headless_mode, UpdateEnvironment.proxy_address,
                                 10, UpdateEnvironment.admin_address, **kwargs)
        # Instagram User=QAEricom Pass = Sa762320!
        # Open Instagram and login
        Functions.PrintText('Open Instagram and login ')
        # Start Chrome browser
        self.client_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON',
                                                    self.headless_mode, self.proxy_address)
        # Go to specific web page
        self.url = 'https://www.instagram.com/'
        # Go to URL in mode
        Functions.GoToURL(self.client_driver, self.url, 0)
        time.sleep(10)
        Functions.SwitchToFrame(self.client_driver, self.wait_time, 'ID', 'crystal-frame-top')
        Functions.EnterTextToField(self.client_driver, self.wait_time, 'NAME', 'username', 'QAEricom')
        Functions.EnterTextToField(self.client_driver, self.wait_time, 'NAME', 'password', 'Sa762320!')
        Functions.PressOnObject(self.client_driver, self.wait_time, 'XPATH',
                                '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button')
        time.sleep(10)
        Functions.SwitchToFrame(self.client_driver, self.wait_time, 'ID', 'crystal-frame-top')
        Functions.VerifyElementIsVisible(self.client_driver, self.wait_time, 'XPATH',
                                         '//*[@id="react-root"]/section/main/section/div/h4')
        Functions.PrintText('Instagram login OK  step - *PASS*')
        Functions.PrintText('Navigating to Google')
        # Go to specific web page
        self.url = 'https://www.google.com/'
        # Go to URL in mode
        Functions.GoToURL(self.client_driver, self.url, 0)
        time.sleep(10)
        # Open instagram in new tab
        Functions.PrintText('Open instagram in new tab')
        self.client_driver.execute_script("window.open('"'https://www.instagram.com/'"')")
        #Switch to new tab and verify auto login to instagram
        Functions.PrintText('Switch to new tab and verify auto login to instagram')
        self.client_driver.switch_to.window(self.client_driver.window_handles[1])
        time.sleep(2)
        Functions.SwitchToFrame(self.client_driver, self.wait_time, 'ID', 'crystal-frame-top')
        Functions.VerifyElementIsVisible(self.client_driver, self.wait_time, 'XPATH',
                                         '//*[@id="react-root"]/section/main/section/div/h4')
        Functions.PrintText('Policies - Cookies - Enabled - Instagram loaded while user logged in  step - *PASS*')
        self.client_driver.quit()

    def test_10_policies_cookies_disable(self):
        Functions.PrintText('Start test_9_policies_cookies_disable ')
        # Set policies configuration
        kwargs = {'access': 'Shield', 'media': 'Crystal', 'suspend': 'Enable', 'cookies': 'Disable'}
        Functions.PoliciesConfig('chromedriver', UpdateEnvironment.chrome_driver_path, 'OFF',
                                 UpdateEnvironment.headless_mode, UpdateEnvironment.proxy_address,
                                 10, UpdateEnvironment.admin_address, **kwargs)
        # Instagram User=QAEricom Pass = Sa762320!
        # Open Instagram and login
        Functions.PrintText('Open Instagram and login ')
        # Start Chrome browser
        self.client_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON',
                                                    self.headless_mode, self.proxy_address)
        # Go to specific web page
        self.url = 'https://www.instagram.com/'
        # Go to URL in mode
        Functions.GoToURL(self.client_driver, self.url, 0)
        time.sleep(10)
        Functions.SwitchToFrame(self.client_driver, self.wait_time, 'ID', 'crystal-frame-top')
        Functions.EnterTextToField(self.client_driver, self.wait_time, 'NAME', 'username', 'QAEricom')
        Functions.EnterTextToField(self.client_driver, self.wait_time, 'NAME', 'password', 'Sa762320!')
        Functions.PressOnObject(self.client_driver, self.wait_time, 'XPATH',
                                '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button')
        time.sleep(10)
        Functions.SwitchToFrame(self.client_driver, self.wait_time, 'ID', 'crystal-frame-top')
        Functions.VerifyElementIsVisible(self.client_driver, self.wait_time, 'XPATH',
                                         '//*[@id="react-root"]/section/main/section/div/h4')
        Functions.PrintText('Instagram login OK  step - *PASS*')
        Functions.PrintText('Navigating to Google')
        # Go to specific web page
        self.url = 'https://www.google.com/'
        # Go to URL in mode
        Functions.GoToURL(self.client_driver, self.url, 0)
        time.sleep(10)
        # Open instagram in new tab
        Functions.PrintText('Open instagram in new tab')
        self.client_driver.execute_script("window.open('"'https://www.instagram.com/'"')")
        # Switch to new tab and verify no auto login to instagram
        Functions.PrintText('Switch to new tab and verify no auto login to instagram')
        self.client_driver.switch_to.window(self.client_driver.window_handles[1])
        time.sleep(2)
        Functions.SwitchToFrame(self.client_driver, self.wait_time, 'ID', 'crystal-frame-top')
        Functions.VerifyElementInvisibility(self.client_driver, self.wait_time, 'XPATH',
                                         '//*[@id="react-root"]/section/main/section/div/h4')
        Functions.PrintText('Policies - Cookies - Disabled - Instagram not auto logged in  step - *PASS*')
        self.client_driver.quit()

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)

if __name__ == '__main__':
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=".", report_name= 'Policies Regression Test Report', add_timestamp=True,report_title='Policies Regression Test Report'))
    unittest.main()