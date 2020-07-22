#0 - Connect to remote machine and update - check containers versions - Done
#1- Check version , Set Shield\Crystal\Disable Print\Disable Download - Browse Chrome - Verify can't download\print - proxyless Chrome - Done
#2 - Set Shield\Crystal\Enable Print\Sanitize Download - Browse Chrome - download\print enabled - Done
#3 - Set Shield\Stream\ - Browse Chrome\Firefox - proxyless Chrome\Firefox - Done
#4 - Set Shield\Basic Authentication\ - Verify can't browse without credentials, Verify browsing with credentials - Done
#5 - Set Shield\LDAP Authentication\ - Verify can't browse without credentials, Verify browsing with credentials - Done
#6 - Suspicious sites - Set Shield\Crystal\Supspicious sites blocked - Browse to suspicious site and get blocked message, check for session history report  - Done
#7 - Backup\Restore - Done


import unittest,NewEnvironment, Functions, HtmlTestRunner, datetime, time

class browsing_tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def test_sanity(self):
        Functions.PrintText('Sanity test started')
        self.wait_time = 15
        self.build_number = NewEnvironment.build_number
        self.headless_mode = 0
        self.chrome_driver_path = NewEnvironment.chrome_driver_path
        self.firefox_driver_path = NewEnvironment.firefox_driver_path
        self.admin_address = NewEnvironment.admin_address
        self.shield_ip = NewEnvironment.shield_ip
        self.shield_machine_user = NewEnvironment.shield_machine_user
        self.shield_machine_pass = NewEnvironment.shield_machine_pass
        self.branch = NewEnvironment.branch
        self.chrome_download_folder = NewEnvironment.chrome_download_folder
        self.proxy_address = NewEnvironment.proxy_address
        self.jenkins_url = NewEnvironment.jenkins_url
        self.jenkins_user = NewEnvironment.jenkins_user
        self.jenkins_password = NewEnvironment.jenkins_password
        self.email = NewEnvironment.email
        self.activation_portal_url = NewEnvironment.activation_portal_url
        self.activation_portal_user = NewEnvironment.activation_portal_user
        self.activation_portal_password = NewEnvironment.activation_portal_password
        self.restore_file_path = NewEnvironment.restore_file_path
        self.env = NewEnvironment.env


        #
        # Functions.CreateNewCleanMachine('chromedriver', self.chrome_driver_path, 'OFF', self.headless_mode, self.proxy_address,
        #                                 self.jenkins_url, self.jenkins_user, self.jenkins_password, self.email)
        #
        # self.shield_ip = input('Check your email and enter new machine IP(public IP): ')
        # self.shield_machine_pass = input('Check your email and enter new machine password: ')

        self.shield_ip = '45.32.234.229'
        self.shield_machine_pass = 'k}F1zzBpZdd_%%S3'
        self.admin_address = 'https://'+self.shield_ip+':30181'
        self.proxy_address = self.shield_ip+':3128'
#
#         # Functions.InstallUpdateShield(self.shield_ip, self.shield_machine_user,self.shield_machine_pass, self.branch, env='new')
#         # time.sleep(600)
#         Functions.CheckRunnigImagesVersions(self.shield_ip, self.shield_machine_user, self.shield_machine_pass)
#         Functions.ActivateNewEnv('chromedriver', self.chrome_driver_path,'OFF', self.headless_mode,
#                                  self.proxy_address,self.wait_time, self.admin_address,
#                                  self.activation_portal_url, self.activation_portal_user, self.activation_portal_password)
#         Functions.ConfigNewEnvAdmin('chromedriver', self.chrome_driver_path,'OFF', self.headless_mode, self.proxy_address, self.wait_time, self.admin_address)
#         # 1- Check version , Set Shield\Crystal\Disable Print\Disable Download
#         # Browse Chrome\Firefox - Verify can't download\print - proxyless Chrome - Done
#         # Start webdriver for admin
#         Functions.PrintText('Start Admin browser')
#         self.admin_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path,'OFF', self.headless_mode, self.proxy_address)
#         #Admin Login
#         Functions.AdminLogin(self.admin_driver, self.wait_time, self.admin_address)
#         # Check correct build version
#         Functions.PrintText('Check build version')
#         res = Functions.CheckObjectText(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="content"]/div[1]/div[1]/div/div[1]/div/div/ul/li/span', self.build_number )
#         if not res:
#             Functions.PrintText('Admin presents correct build version - step *PASS*')
#         else:
#             Functions.PrintText('Admin presents incorrect build version - step *FAIL*')
#             self.fail('Admin presents in correct build version - step *FAIL*')
#
#         # Go to Policies page
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="el_1"]/a/span')
#         # Edit Default - All Domain
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="policies-grid"]/vaadin-grid-cell-content[69]/vaadin-checkbox')
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="content"]/div/div/div[1]/div/div[1]/ul/li[2]/i')
#         # Policies - Edit Default - All Domain
#         Functions.PrintText('Policies - Edit Default - All Domain - Shield/Crystal/Ignore certificate')
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'NAME', 'access', 'Shield')
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'NAME', 'media', 'Crystal')
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'NAME', 'certificate',
#                                        'Ignore')
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'NAME', 'download', 'Disable')
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'NAME', 'printing', 'Disable')
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="middle"]/div[2]/cc-modal/div/div/div/div[3]/table/tbody/tr/td[2]/div/button[1]')
#         # Go to Profiles page
#         Functions.PrintText('Going to Profiles page - Set Basic Auth = no , set LDAP = no')
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="el_4"]/a/span')
#         # Press on Basic Authentication option
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="nobackgroundcontent"]/cc-toggle[2]/div/label')
#         # Set Enabled  = No
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'XPATH',
#                                        '//*[@id="nobackgroundcontent"]/cc-toggle[2]/div/div/div[1]/div/select',
#                                        'No')
#         # ￿ Press Save button
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="contentprofile"]/div/div[1]/div[2]/input')
#         # Press on Active Directory option
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="nobackgroundcontent"]/cc-toggle[3]/div/label')
#         # Press on LDAP option
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="nobackgroundcontent"]/cc-toggle[3]/div/div/cc-toggle[3]/div/label')
#         # Set Enabled  = No
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'XPATH',
#                                        '//*[@id="nobackgroundcontent"]/cc-toggle[3]/div/div/cc-toggle[3]/div/div/div[1]/div/select',
#                                        'No')
#         # ￿ Press Save button
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="contentprofile"]/div/div[1]/div[2]/input')
#         # ￿ Select OK from Modal window if appears
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="wrapper"]/app-root/cc-container-with-menu/cc-profiles-container/cc-profiles/cc-modal[7]/div/div/div/div[3]/table/tbody/tr/td[2]/div/button[1]')
#         # Close Admin browser
#         Functions.PrintText('Close Admin browser')
#         self.admin_driver.quit()
#         # Open Chrome Browser in Shield\Crystal, Go to URL Press on Object
#         Functions.PrintText('Open Client Browser in Shield\Crystal, Go to URL Press on Object')
#         # Start Chrome browser
#         self.client_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path,'ON', self.headless_mode, self.proxy_address)
#         time.sleep(10)
#         # Go to specific web page
#         self.url = 'https://www.google.com/'
#         Functions.GoToURL(self.client_driver, self.url, 0)
#         time.sleep(10)
#         # Wait for page Access now page to be loaded and switch to frame
#         Functions.SwitchToFrame(self.client_driver, self.wait_time, 'ID', 'crystal-frame-top')
#         # Enter text to field
#         Functions.EnterTextToField(self.client_driver, self.wait_time,'NAME', 'q', 'Shai Adani')
#         Functions.HitEnter()
#         # # Close Client browser
#         Functions.PrintText('Close Client browser')
#         self.client_driver.quit()
#         Functions.PrintText('Shield,Crystal,No Authentication test - *PASS*')
#         # Open Chrome Browser in Shield\Crystal\no print no download, verify print\download buttons are invisible
#         Functions.PrintText('Open Chrome Browser in Shield\Crystal no print no download, verify print\download buttons are invisible')
#         # Start Chrome browser
#         self.client_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON', self.headless_mode, self.proxy_address)
#         # Go to specific web page
#         self.url = 'https://www.ericom.com/doc/TechnicalReferences/EricomBlazeAdminManual.pdf'
#         Functions.GoToURL(self.client_driver, self.url, 0)
#         # Wait for page Access now page to be loaded and switch to frame
#         Functions.SwitchToFrame(self.client_driver, self.wait_time, 'ID', 'crystal-frame-top')
#         # Verify print\download buttons are invisible
#         Functions.VerifyElementInvisibility(self.client_driver, self.wait_time, 'ID', 'print')
#         Functions.VerifyElementInvisibility(self.client_driver, self.wait_time, 'ID', 'download')
#         # # Close Client browser
#         Functions.PrintText('Close Client browser')
#         self.client_driver.quit()
#         Functions.PrintText('Shield,Crystal, no print no download ,no Authentication test - *PASS*')
#         # Open Chrome Browser in non shield, Go to URL Press on Object in proxy-less mode
#         Functions.PrintText('Open Client Browser in non shield\Crystal, Go to URL Press on Object in proxy-less mode')
#         # Start Chrome browser
#         self.client_driver_proxyless = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'OFF', self.headless_mode, self.proxy_address)
#         # Go to specific web page
#         self.url = 'https://www.google.com/'
#         self.proxyless_url = 'https://' + self.shield_ip + ':30443' + '/?url=' + self.url
#         # Go to URL in proxyless mode
#         Functions.GoToURL(self.client_driver_proxyless, self.proxyless_url, 0)
#         # Wait for page Access now page to be loaded and switch to frame
#         Functions.SwitchToFrame(self.client_driver_proxyless, self.wait_time, 'ID', 'crystal-frame-top')
#         # Enter text to field
#         Functions.EnterTextToField(self.client_driver_proxyless, self.wait_time, 'NAME', 'q', 'Shai Adani')
#         Functions.HitEnter()
#         # # Close Client browser
#         Functions.PrintText('Close client - proxyless mode')
#         self.client_driver_proxyless.quit()
#         Functions.PrintText('Proxyless,Crystal,No Authentication test - *PASS*')
# # ###############################################################################################################################################
#         # 2 - Set Shield\Crystal\Enable Print\Sanitize Download - Browse Chrome - download\print enabled - Done
#         # Set Admin config to Shield\Crystal\Ignore Certificate\Sanitize download\Enable print
#         Functions.PrintText('Set Admin config to Shield\Crystal\Ignore Certificate, Sanitize download\Enable print')
#         #Start webdriver for admin
#         Functions.PrintText('Start Admin browser')
#         self.admin_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path,'OFF', self.headless_mode, self.proxy_address)
#         #Admin Login
#         Functions.AdminLogin(self.admin_driver, self.wait_time, self.admin_address)
#         # Go to Policies page
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="el_1"]/a/span')
#         # Edit Default - All Domain
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="policies-grid"]/vaadin-grid-cell-content[69]/vaadin-checkbox')
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="content"]/div/div/div[1]/div/div[1]/ul/li[2]/i')
#         # Policies - Edit Default - All Domain
#         Functions.PrintText('Policies - Edit Default - All Domain - Shield/Crystal/Ignore certificate')
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'NAME', 'access', 'Shield')
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'NAME', 'media', 'Crystal')
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'NAME', 'certificate',
#                                        'Ignore')
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'NAME', 'download', 'Sanitize')
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'NAME', 'printing', 'Enable')
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="middle"]/div[2]/cc-modal/div/div/div/div[3]/table/tbody/tr/td[2]/div/button[1]')
#         # Close Admin browser
#         Functions.PrintText('Close Admin browser')
#         self.admin_driver.quit()
#         # Open Chrome Browser in Shield\Crystal\sanitize print enable download, print\download
#         Functions.PrintText(
#             'Open Chrome Browser in Shield\Crystal yes print sanitize download')
#         # Start Chrome browser
#         self.client_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON', self.headless_mode, self.proxy_address)
#         # Go to specific web page
#         self.url = 'https://www.ericom.com/doc/TechnicalReferences/EricomBlazeAdminManual.pdf'
#         Functions.GoToURL(self.client_driver, self.url, 0)
#         # Wait for page Access now page to be loaded and switch to frame
#         Functions.SwitchToFrame(self.client_driver, self.wait_time, 'ID', 'crystal-frame-top')
#         # Press on download option
#         time.sleep(5)
#         # Go to online PDF file, download and verify it was downloaded
#         Functions.VerifyFileDownload(self.client_driver, self.wait_time, 'ID', 'download', self.chrome_download_folder, 'EricomBlazeAdminManual.pdf')
#         time. sleep(5)
#         # Verify that Print icon is visible
#         Functions.VerifyElementIsVisible(self.client_driver, self.wait_time, 'ID', 'print')
#         # Close Client browser
#         Functions.PrintText('Close Client browser')
#         self.client_driver.quit()
#         Functions.PrintText('Shield,Crystal, no print no download ,no Authentication test - *PASS*')
# ###############################################################################################################
#         #3 - Set Shield\Stream\ - Browse Chrome\Firefox - proxyless Chrome\Firefox - Done
#         # Admin Login
#         self.admin_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'OFF', self.headless_mode, self.proxy_address)
#         Functions.AdminLogin(self.admin_driver, self.wait_time, self.admin_address)
#         # Set Admin config to Shield\Stream\Ignore Certificate
#         Functions.PrintText('Set Admin config to Shield\Crystal\Ignore Certificate')
#         # Go to Policies page
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="el_1"]/a/span')
#         # Edit Default - All Domain
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="policies-grid"]/vaadin-grid-cell-content[69]/vaadin-checkbox')
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="content"]/div/div/div[1]/div/div[1]/ul/li[2]/i')
#         # Policies - Edit Default - All Domain
#         Functions.PrintText('Policies - Edit Default - All Domain - Shield/Crystal/Ignore certificate')
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'NAME', 'access', 'Shield')
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'NAME', 'media', 'Stream')
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'NAME', 'certificate',
#                                 '//*[@id="middle"]/div[2]/cc-modal/div/div/div/div[3]/table/tbody/tr/td[2]/div/button[1]')
#         # Close Admin browser
#         Functions.PrintText('Close Admin browser')
#         self.admin_driver.quit()
#         # Open Chrome Browser in Shield\Stream, Go to URL Press on Object
#         Functions.PrintText('Open Client Browser in Shield\Stream, Go to URL Press on Object')
#         # Start Chrome browser
#         self.client_driver_chrome = Functions.StartBrowser('chromedriver', self.chrome_driver_path,'ON', self.headless_mode, self.proxy_address)
#         # Start FireFox browser
#         self.client_driver_ff = Functions.StartBrowser('geckodriver', self.firefox_driver_path, 'ON', self.headless_mode, self.proxy_address)
#         # Go to specific web page
#         self.url = 'https://www.google.com/'
#         Functions.GoToURL(self.client_driver_chrome, self.url, 0)
#         Functions.GoToURL(self.client_driver_ff, self.url, 0)
#         # Verify that canvas is included in loaded page and title is as expected
#         Functions.VerifyFrameModePageLoaded(self.client_driver_chrome, self.wait_time, 'Google')
#         Functions.VerifyFrameModePageLoaded(self.client_driver_ff, self.wait_time, 'Google')
#         # Close client browser
#         self.client_driver_chrome.quit()
#         self.client_driver_ff.quit()
#         # Open Chrome Browser in non shield, Go to URL Press on Object in proxy-less mode
#         Functions.PrintText('Open Client Browser in non shield\Stream, Go to URL Press on Object in proxy-less mode')
#         # Start Chrome browser
#         self.client_driver_chrome_proxyless = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'OFF', self.headless_mode, self.proxy_address)
#         self.client_driver_ff_proxyless = Functions.StartBrowser('geckodriver', self.firefox_driver_path, 'OFF', self.headless_mode, self.proxy_address)
#         # Go to specific web page
#         self.url = 'https://www.google.com/'
#         self.proxyless_url = 'https://' + self.shield_ip + ':30443' + '/?url=' + self.url
#         # Go to URL in proxyless mode
#         Functions.GoToURL(self.client_driver_chrome_proxyless, self.proxyless_url, 0)
#         Functions.GoToURL(self.client_driver_ff_proxyless, self.proxyless_url, 0)
#         # Verify that canvas is included in loaded page and title is as expected
#         Functions.VerifyFrameModePageLoaded(self.client_driver_chrome_proxyless, self.wait_time, 'Google')
#         Functions.VerifyFrameModePageLoaded(self.client_driver_ff_proxyless, self.wait_time, 'Google')
#         # Close client browser
#         self.client_driver_chrome_proxyless.quit()
#         self.client_driver_ff_proxyless.quit()
# ###############################################################################################################
#         #4 - Set Shield\Basic Authentication\ - Verify can't browse without credentials, Verify browsing with credentials
#         #Set Basic authentication = Yes and verify you don't get required page without credentials
#         #Start webdriver for admin
#         Functions.PrintText('Start Admin browser')
#         self.admin_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path,'OFF', self.headless_mode, self.proxy_address)
#         # Admin Login
#         Functions.AdminLogin(self.admin_driver, self.wait_time, self.admin_address)
#         # Go to Profiles page
#         Functions.PrintText('Going to Profiles page - Set Basic Auth = Yes , set LDAP = no')
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="el_4"]/a/span')
#         # Press on Basic Authentication option
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="nobackgroundcontent"]/cc-toggle[2]/div/label')
#         # Set Enabled  = Yes
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'XPATH',
#                                        '//*[@id="nobackgroundcontent"]/cc-toggle[2]/div/div/div[1]/div/select',
#                                        'Yes')
#         # ￿ Press Save button
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="contentprofile"]/div/div[1]/div[2]/input')
#         # Press on Active Directory option
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="nobackgroundcontent"]/cc-toggle[3]/div/label')
#         # Press on LDAP option
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="nobackgroundcontent"]/cc-toggle[3]/div/div/cc-toggle[3]/div/label')
#         # Set Enabled  = No
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'XPATH',
#                                        '//*[@id="nobackgroundcontent"]/cc-toggle[3]/div/div/cc-toggle[3]/div/div/div[1]/div/select',
#                                        'No')
#         # ￿ Press Save button
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="contentprofile"]/div/div[1]/div[2]/input')
#         # ￿ Select OK from Modal window if appears
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="wrapper"]/app-root/cc-container-with-menu/cc-profiles-container/cc-profiles/cc-modal[7]/div/div/div/div[3]/table/tbody/tr/td[2]/div/button[1]')
#         # Close Admin browser
#         Functions.PrintText('Close Admin browser')
#         self.admin_driver.quit()
#         # Open Chrome Browser in Shield\Stream, Go to URL Press on Object
#         Functions.PrintText('Open Client Browser while Basic Authentication = Yes, Try to go to URL and verify you can not reach it')
#         # Start Chrome browser
#         self.client_driver_chrome = Functions.StartBrowser('chromedriver', self.chrome_driver_path,'ON', self.headless_mode, self.proxy_address)
#         # Go to specific web page
#         self.url = 'https://www.google.com/'
#         Functions.GoToURL(self.client_driver_chrome, self.url, 0)
#         # Verify that page is not accessible while working with basic authentication
#         Functions.VerifyPageBlockedByAuth(self.client_driver_chrome, self.wait_time, 'ID', 'canvas')
#         Functions.PrintText('Page blocked in BASIC authentication mode - step *PASS*')
#         #Enter user name and password in basic authentication window
#         Functions.EnterUserPasswordInAuthWindow('ericom', 'ericomshield')
#         # Verify that page is accessible when providing credentials in basic authentication window
#         Functions.VerifyFrameModePageLoaded(self.client_driver_chrome, self.wait_time, 'Google')
#         Functions.PrintText('Page loaded in BASIC authentication mode after providing credentials- step *PASS*')
#         # Close client browser
#         self.client_driver_chrome.quit()
# # # ################################################################################################################
#         # 5 - Set Shield\LDAP Authentication\ - Verify can't browse without credentials, Verify browsing with credentials
#         # Set Basic authentication = No LDAP = Yes and verify you don't get required page without credentials
#         # Start webdriver for admin
#         Functions.PrintText('Start Admin browser')
#         self.admin_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'OFF',
#                                                    self.headless_mode, self.proxy_address)
#         # Admin Login
#         Functions.PrintText('Admin login')
#         Functions.GoToURL(self.admin_driver, self.admin_address, 0)
#         Functions.EnterTextToField(self.admin_driver, self.wait_time, 'NAME', 'username', 'admin')
#         Functions.EnterTextToField(self.admin_driver, self.wait_time, 'NAME', 'password', 'ericomshield')
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'ID', 'login-submit')
#         # Go to Profiles page
#         Functions.PrintText('Going to Profiles page - Set Basic Auth = No , set LDAP = Yes')
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="el_4"]/a/span')
#         # Press on Basic Authentication option
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="nobackgroundcontent"]/cc-toggle[2]/div/label')
#         # Set Enabled  = No
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'XPATH',
#                                        '//*[@id="nobackgroundcontent"]/cc-toggle[2]/div/div/div[1]/div/select',
#                                        'No')
#         # ￿ Press Save button
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="contentprofile"]/div/div[1]/div[2]/input')
#         # Press on Active Directory option
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="nobackgroundcontent"]/cc-toggle[3]/div/label')
#         # Press on LDAP option
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="nobackgroundcontent"]/cc-toggle[3]/div/div/cc-toggle[3]/div/label')
#         # Set Enabled  = Yes
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'XPATH',
#                                        '//*[@id="nobackgroundcontent"]/cc-toggle[3]/div/div/cc-toggle[3]/div/div/div[1]/div/select',
#                                        'Yes')
#         # ￿ Press Save button
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="contentprofile"]/div/div[1]/div[2]/input')
#         # ￿ Select OK from Modal window if appears
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="wrapper"]/app-root/cc-container-with-menu/cc-profiles-container/cc-profiles/cc-modal[7]/div/div/div/div[3]/table/tbody/tr/td[2]/div/button[1]')
#         # Close Admin browser
#         Functions.PrintText('Close Admin browser')
#         self.admin_driver.quit()
#         # Open Chrome Browser in Shield\Stream, Go to URL Press on Object
#         Functions.PrintText(
#             'Open Client Browser while Basic Authentication = Yes, Try to go to URL and verify you can not reach it')
#         # Start Chrome browser
#         self.client_driver_chrome = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON',
#                                                            self.headless_mode, self.proxy_address)
#         # Go to specific web page
#         self.url = 'https://www.google.com/'
#         Functions.GoToURL(self.client_driver_chrome, self.url, 0)
#
#         # Verify that page is not accessible while working with LDAP authentication
#         Functions.VerifyPageBlockedByAuth(self.client_driver_chrome, self.wait_time, 'ID', 'canvas')
#         Functions.PrintText('Page blocked in LDAP authentication mode - step *PASS*')
#         # Enter user name and password in LDAP authentication window
#         Functions.EnterUserPasswordInAuthWindow('admintest@shield.local', 'qwer432!') # admintest@shield.local  qwer432!
#         # Verify that page is accessible when providing credentials in LDAP authentication window
#         Functions.VerifyFrameModePageLoaded(self.client_driver_chrome, self.wait_time, 'Google')
#         Functions.PrintText('Page loaded in LDAP authentication mode after providing credentials- step *PASS*')
#         # Close client browser
#         self.client_driver_chrome.quit()
# #
# #
#         #SAML
# # #         ###############################################################################################################################################
#         #6 - Suspicious sites - Set Shield\Crystal\Supspicious sites blocked - Browse to suspicious site and get blocked message, check for session history report  - Done
#         # Start webdriver for admin
#         Functions.PrintText('Start Admin browser')
#         self.admin_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'OFF', self.headless_mode,
#                                                    self.proxy_address)
#         # Admin Login
#         Functions.AdminLogin(self.admin_driver, self.wait_time, self.admin_address)
#         # Go to Policies page
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="el_1"]/a/span')
#         # Edit Default - All Domain
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="policies-grid"]/vaadin-grid-cell-content[69]/vaadin-checkbox')
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="content"]/div/div/div[1]/div/div[1]/ul/li[2]/i')
#         # Policies - Edit Default - All Domain
#         Functions.PrintText('Policies - Edit Default - All Domain - Shield/Crystal/Ignore certificate')
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'NAME', 'access', 'Shield')
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'NAME', 'media', 'Crystal')
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'NAME', 'certificate',
#                                        'Ignore')
#         # Save
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="middle"]/div[2]/cc-modal/div/div/div/div[3]/table/tbody/tr/td[2]/div/button[1]')
#         # Go to Settings page
#         Functions.PrintText('Going to Settings page - Set Suspected sites = Block, Potential phishing = block')
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="sideNav"]/ul/li[4]/a/span')
#         # Press on Suspicious sites option
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="nobackgroundcontent"]/cc-toggle[2]/div/label')
#         # Set Suspected sites  = Block
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'XPATH',
#                                        '//*[@id="nobackgroundcontent"]/cc-toggle[2]/div/div/div[1]/div/select',
#                                        'Block')
#         # Set Potential Phishing  = Block
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'XPATH',
#                                        '//*[@id="nobackgroundcontent"]/cc-toggle[2]/div/div/div[2]/div/select',
#                                        'Block')
#         # ￿ Press Save button
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="wrapper"]/app-root/cc-container-with-menu/cc-settings-container/cc-settings/div/div[2]/button[1]')
#
#         # Go to Profiles page
#         Functions.PrintText('Going to Profiles page - Set Basic Auth = no , set LDAP = no')
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="el_4"]/a/span')
#         # Press on Basic Authentication option
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="nobackgroundcontent"]/cc-toggle[2]/div/label')
#         # Set Enabled  = No
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'XPATH',
#                                        '//*[@id="nobackgroundcontent"]/cc-toggle[2]/div/div/div[1]/div/select',
#                                        'No')
#         # ￿ Press Save button
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="contentprofile"]/div/div[1]/div[2]/input')
#         # Press on Active Directory option
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="nobackgroundcontent"]/cc-toggle[3]/div/label')
#         # Press on LDAP option
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="nobackgroundcontent"]/cc-toggle[3]/div/div/cc-toggle[3]/div/label')
#         # Set Enabled  = No
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'XPATH',
#                                        '//*[@id="nobackgroundcontent"]/cc-toggle[3]/div/div/cc-toggle[3]/div/div/div[1]/div/select',
#                                        'No')
#         # ￿ Press Save button
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="contentprofile"]/div/div[1]/div[2]/input')
#         # ￿ Select OK from Modal window if appears
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="wrapper"]/app-root/cc-container-with-menu/cc-profiles-container/cc-profiles/cc-modal[7]/div/div/div/div[3]/table/tbody/tr/td[2]/div/button[1]')
#         # Close Admin browser
#         Functions.PrintText('Close Admin browser')
#         self.admin_driver.quit()
#
#         # Open Chrome Browser in Shield\Stream, Go to URL Press on Object
#         Functions.PrintText(
#             'Open Client Browser and try to browse to suspicious site, verify blocked by shield')
#         # Start Chrome browser
#         self.client_driver_chrome = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON',
#                                                            self.headless_mode, self.proxy_address)
#         # Go to specific web page
#         self.url = 'http://plenavia.cl/cxc/D2017HL/u.php'
#         Functions.GoToURL(self.client_driver_chrome, self.url, 0)
#         # Check if page was blocked
#         Functions.CheckIfPageBlocked(self.client_driver_chrome, self.wait_time)
#         time.sleep(3)
#         self.client_driver_chrome.quit()
#         # Check if report contains blocked activity
#         # Admin Login
#         self.admin_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'OFF', self.headless_mode,
#                                                    self.proxy_address)
#         Functions.AdminLogin(self.admin_driver, self.wait_time, self.admin_address)
#         # Go to Reports page
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="el_3"]/a/span')
#         # Reports - Select Category = Sessions Select Report = Session History time = Last 15 minutes
#         Functions.PrintText('Reports - Select Category = Sessions Select Report = Session History time = Last 15 minutes')
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'NAME', 'selectCategory', 'Sessions')
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'NAME', 'selectReport', 'Session History')
#         Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'NAME', 'selectTime',
#                                        'Last 15 minutes')
#         # Save
#         Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
#                                 '//*[@id="content"]/table/tbody/tr[1]/td[4]/button')
#         # Search word in report
#         # words = ['plenavia.cl','black',"Phishing 'Block' Policy", 'Suspected']
#         Functions.SearchValuesInTable(self.admin_driver, self.wait_time,'//*[@id="content"]/table', 'plenavia.cl','black',"Phishing 'Block' Policy", 'Suspected')
#         self.admin_driver.quit()
        Functions.CheckBackUpRetore(self.shield_ip, self.shield_machine_user, self.shield_machine_pass, 'chromedriver',
                                    self.chrome_driver_path, 'OFF',
                                    self.headless_mode, self.proxy_address, self.wait_time, self.admin_address,
                                    self.restore_file_path, self.env)

    # #########################################################################################################################################

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=".", report_name= 'New Env Sanity Test Report', add_timestamp=True,report_title='New Env Sanity Test Report'))
    unittest.main()