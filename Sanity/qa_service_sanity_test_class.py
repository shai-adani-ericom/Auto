import unittest,QAServiceEnvironment, Functions, HtmlTestRunner, datetime, time

class sanity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.pop = 'qa-ericom.shield-service.net:3128'
        cls.wait_time = QAServiceEnvironment.wait_time
        cls.chrome_driver_path = QAServiceEnvironment.chrome_driver_path
        cls.chrome_download_folder = QAServiceEnvironment.chrome_download_folder
        cls.pop_address = QAServiceEnvironment.wait_time
        cls.tenant_url = QAServiceEnvironment.tenant_url
        cls.tenant_user = QAServiceEnvironment.tenant_user
        cls.tenant_password = QAServiceEnvironment.tenant_password
        cls.headless_mode = QAServiceEnvironment.headless_mode


    # All listed tests will be executed for each pop

    # browse to google in proxy mode
    def test_1_browse_in_proxy_mode(self):
        # Start Chrome browser
        self.client_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path, 'ON', self.headless_mode,
                                                    self.pop)
        time.sleep(5)
        # Go to specific web page
        Functions.GoToURL(self.client_driver, 'https://www.google.com/', 0)
        time.sleep(10)
        # Wait for page Access now page to be loaded and switch to frame
        Functions.SwitchToFrame(self.client_driver, self.wait_time, 'ID', 'crystal-frame-top')
        # Enter text to field
        Functions.EnterTextToField(self.client_driver, self.wait_time, 'NAME', 'q', 'Shai Adani')
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
        time.sleep(10)
        # # Search word in report
        # # words = ['www.google.com']
        Functions.SearchValuesInTable(self.admin_driver, self.wait_time, '//*[@id="content"]/table', 'www.google.com')
        time.sleep(3)
        self.admin_driver.quit()

    # browse to pdf file and verify print enabled

    # download the file and verify it was downloaded

    # browse to suspicious site and verify it was blocked


    # close browsers


    # #########################################################################################################################################

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=".", report_name= 'New Env Sanity Test Report', add_timestamp=True,report_title='New Env Sanity Test Report'))
    unittest.main()