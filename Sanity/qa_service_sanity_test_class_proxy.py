import unittest,QAServiceEnvironment, Functions, HtmlTestRunner, datetime, time


class sanity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.pops = QAServiceEnvironment.qa_pops_proxy
        cls.wait_time = QAServiceEnvironment.wait_time
        cls.chrome_driver_path = QAServiceEnvironment.chrome_driver_path
        cls.chrome_download_folder = QAServiceEnvironment.chrome_download_folder
        # cls.pop_address = QAServiceEnvironment.wait_time
        cls.tenant_url = QAServiceEnvironment.tenant_url
        cls.tenant_user = QAServiceEnvironment.tenant_user
        cls.tenant_password = QAServiceEnvironment.tenant_password
        cls.headless_mode = QAServiceEnvironment.headless_mode
        cls.admin_url = QAServiceEnvironment.admin_url
        cls.admin_user = QAServiceEnvironment.admin_user
        cls.admin_password = QAServiceEnvironment.admin_password

    def test_0_all(self):
        for pop in self.pops:
            self.pop = pop
            self.test_1_browse_in_proxy_mode()
            self.test_2_check_active_session_report_proxy()
            self.test_3_verify_print_enabled_and_download()
            self.test_4_block_suspicious_site()

    # browse to google in proxy mode
    def test_1_browse_in_proxy_mode(self):
        # Start Chrome browser
        self.client_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON', self.headless_mode,
                                                    self.pop)
        print(self.pop)
        time.sleep(5)
        # Go to specific web page
        Functions.GoToURL(self.client_driver, 'https://www.google.com/', 0)
        time.sleep(10)
        # Wait for page Access now page to be loaded and switch to frame
        Functions.SwitchToFrame(self.client_driver, self.wait_time, 'ID', 'crystal-frame-top')
        # Enter text to field
        Functions.EnterTextToField(self.client_driver, self.wait_time, 'NAME', 'q', 'שי עדני בדיקות תוכנה')
        time.sleep(5)
        Functions.HitEnter()
        time.sleep(5)


    def test_2_check_active_session_report_proxy(self):
        # check active session in tenant report - needs tenants gui
        # Tenant Admin Login
        self.admin_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'OFF', self.headless_mode,
                                                   self.pop)
        Functions.TenantAdminLogin(self.admin_driver, self.wait_time, self.tenant_url, self.tenant_user, self.tenant_password)
        # Go to Reports page
        Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="el_1"]/a/span')
        time.sleep(5)
        # Reports - Select Category = Sessions Select Report = Active sessions
        Functions.PrintText('Reports - Select Category = Sessions Select Report = Active sessions')
        time.sleep(3)
        Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'NAME', 'selectCategory', 'Sessions')
        time.sleep(3)
        Functions.SelectOptionFromList(self.admin_driver, self.wait_time, 'NAME', 'selectReport', 'Active Sessions')
        time.sleep(3)
        # run
        Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH',
                                '//*[@id="content"]/table/tbody/tr[1]/td[4]/button')
        time.sleep(5)
        # # Search word in report
        # res= Functions.SearchValuesInTable(self.admin_driver, self.wait_time,
        #                                    '//*[@id="content"]/table',
        #                                    'https://www.google.com')
        if 'https://www.google.com'  in self.admin_driver.page_source:
            print('https://www.google.com appears in active sessions reports - test ***PASS***')
        else:
            print('https://www.google.com NOT appears in active sessions reports - test ***FAIL***')
            self.fail('https://www.google.com NOT appears in active sessions reports - test ***FAIL***')
        time.sleep(3)
        self.admin_driver.quit()
        time.sleep(1)
        # self.client_driver.quit()

    # browse to pdf file and verify print enabled
    def test_3_verify_print_enabled_and_download(self):
        # Open Chrome Browser in Shield\Crystal\sanitize print enable download, print\download
        Functions.PrintText(
            'Open Chrome Browser in Shield\Crystal yes print sanitize download')
        # Start Chrome browser
        self.client_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON', self.headless_mode,
                                                    self.pop)
        # Go to specific web page
        self.url = 'https://www.ericom.com/doc/TechnicalReferences/EricomBlazeAdminManual.pdf'
        Functions.GoToURL(self.client_driver, self.url, 0)
        # Wait for page Access now page to be loaded and switch to frame
        Functions.SwitchToFrame(self.client_driver, self.wait_time, 'ID', 'crystal-frame-top')
        # Press on download option
        time.sleep(5)
        # Go to online PDF file, download and verify it was downloaded
        Functions.VerifyFileDownload(self.client_driver, self.wait_time, 'ID', 'download', self.chrome_download_folder,
                                     'EricomBlazeAdminManual.pdf')
        time.sleep(5)
        # Verify that Print icon is visible
        Functions.VerifyElementIsVisible(self.client_driver, self.wait_time, 'ID', 'print')
        # Close Client browser
        Functions.PrintText('Close Client browser')
        self.client_driver.quit()
        Functions.PrintText('Shield,Crystal, enable print enable download ,no Authentication test - *PASS*')

    # browse to suspicious site and verify it was blocked
    def test_4_block_suspicious_site(self):
        # #6 - Suspicious sites -  Browse to suspicious site and get blocked message, check for session history report
        # Open Chrome Browser in Shield\Stream, Go to URL Press on Object
        Functions.PrintText(
            'Open Client Browser and try to browse to suspicious site, verify blocked by shield')
        # Start Chrome browser
        self.client_driver_chrome = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON',
                                                           self.headless_mode, self.pop)
        # Go to specific web page
        self.url = 'http://plenavia.cl/cxc/D2017HL/u.php'
        Functions.GoToURL(self.client_driver_chrome, self.url, 0)
        # Check if page was blocked
        Functions.CheckIfPageBlocked(self.client_driver_chrome, self.wait_time)
        time.sleep(3)
        self.client_driver_chrome.quit()
        # Check if report contains blocked activity
        # Admin Login
        self.tenant_admin_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'OFF', self.headless_mode,
                                                   self.pop)
        Functions.TenantAdminLogin(self.tenant_admin_driver, self.wait_time, self.tenant_url, self.tenant_user, self.tenant_password)
        # Go to Reports page
        Functions.PressOnObject(self.tenant_admin_driver, self.wait_time, 'XPATH', '//*[@id="el_1"]/a/span')
        # Reports - Select Category = Sessions Select Report = Session History time = Last 15 minutes
        Functions.PrintText('Reports - Select Category = Sessions Select Report = Session History time = Last 15 minutes')
        Functions.SelectOptionFromList(self.tenant_admin_driver, self.wait_time, 'NAME', 'selectCategory', 'Sessions')
        Functions.SelectOptionFromList(self.tenant_admin_driver, self.wait_time, 'NAME', 'selectReport', 'Session History')
        Functions.SelectOptionFromList(self.tenant_admin_driver, self.wait_time, 'NAME', 'selectTime',
                                       'Last 15 minutes')
        # Save
        Functions.PressOnObject(self.tenant_admin_driver, self.wait_time, 'XPATH',
                                '//*[@id="content"]/table/tbody/tr[1]/td[4]/button')
        time.sleep(5)
        # Search word in report
        # words = ['plenavia.cl','black',"Phishing 'Block' Policy", 'Suspected']
        Functions.SearchValuesInTable(self.tenant_admin_driver, self.wait_time,'//*[@id="content"]/table', 'plenavia.cl','black',"Phishing 'Block' Policy", 'Suspected')
        self.tenant_admin_driver.quit()

    #########################################################################################################################################

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=".", report_name= pop, add_timestamp=True,report_title='Cloud Sanity Test Report'))
    # for pops in QAServiceEnvironment.qa_pops_proxy:
    #     pop = pops
    #     print('Sanity on POP {} Started'.format(pop))
        unittest.main()