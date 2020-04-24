# Prerequisite - new environment is ready


import unittest,UpdateEnvironment, Functions, HtmlTestRunner, datetime, time

env = UpdateEnvironment # change to NewEnvironment in case needed

class policies_regression(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.wait_time = 15
        cls.headless_mode = 0
        cls.chrome_driver_path = UpdateEnvironment.chrome_driver_path
        cls.firefox_driver_path = UpdateEnvironment.firefox_driver_path
        cls.admin_address = UpdateEnvironment.admin_address
        cls.shield_ip = UpdateEnvironment.shield_ip
        cls.shield_machine_user = UpdateEnvironment.shield_machine_user
        cls.shield_machine_pass = UpdateEnvironment.shield_machine_pass
        cls.branch = UpdateEnvironment.branch
        cls.chrome_download_folder = UpdateEnvironment.chrome_download_folder
        cls.proxy_address = UpdateEnvironment.proxy_address
        cls.restore_file_path = UpdateEnvironment.restore_file_path

    def test_policies_general_view(self):
        # Verify Policies compact mode by default
        Functions.PrintText('Start test_policies_general_view - '
                            'Test purpose is to verify default compact mode,'
                            ' switch to verbose mode, verify columns are sortable, and every option appears for each list')
        self.admin_driver = Functions.StartBrowser('chromedriver', self.chrome_driver_path,'OFF', self.headless_mode, self.proxy_address)
        Functions.AdminLogin(self.admin_driver, self.wait_time, self.admin_address)
        # Go to Policies page
        Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="el_1"]/a/span')
        # Check default compact view
        res = Functions.VerifyElementInvisibility(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="policies-grid"]/vaadin-grid-cell-content[6]/div/vaadin-grid-sorter')
        if res == 1:
            Functions.PrintText('Download column invisible step - *PASS*')
        # Change to Verbose mode
        Functions.PressOnObject(self.admin_driver, self.wait_time, 'XPATH', '//*[@id="toggle-data"]/i')
        # Check additional columns visibility
        #####CONTINUE#####




        # self.admin_driver.quit()

    # def test_policies_regression(self):
    #
    #     # Set policies configuration
    #     kwargs = {'access':'White', 'upload':'Enabled'}
    #     Functions.PoliciesConfig('chromedriver', UpdateEnvironment.chrome_driver_path,'OFF',
    #                              UpdateEnvironment.headless_mode, UpdateEnvironment.proxy_address,
    #                              10, UpdateEnvironment.admin_address, **kwargs )

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=".", report_name= 'Policies Regression Test Report', add_timestamp=True,report_title='Policies Regression Test Report'))
    unittest.main()