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

    def test_0_service_proxy_sanity(self):
        for pop in self.pops:
            self.pop = pop
            print('￿STARTING SANITY CYCLE FOR POP {}'.format(pop))
            self.client_driver = Functions.service_browse('chromedriver', self.chrome_driver_path, 'ON',
                                                          self.headless_mode, self.pop, self.wait_time)
            Functions.service_check_active_session_report('chromedriver', self.chrome_driver_path, 'OFF',
                                                          self.headless_mode,self.pop, self.wait_time, self.tenant_url,
                                                          self.tenant_user, self.tenant_password)
            self.client_driver.quit()
            Functions.service_verify_print_enabled_and_download('chromedriver', self.chrome_driver_path, 'ON',
                                                                self.headless_mode, self.pop, self.wait_time, self.chrome_download_folder)

            Functions.service_block_suspicious_site('chromedriver', self.chrome_driver_path, 'ON',
                                                                        self.headless_mode, self.pop,
                                                    self.wait_time, self.tenant_url, self.tenant_user, self.tenant_password)

    #########################################################################################################################################

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=".", report_name= pop, add_timestamp=True,report_title='Cloud Sanity Test Report'))
   unittest.main()