import unittest,HtmlTestRunner, datetime, time, Functions, LoadEnvironmentLocal, multiprocessing


class load1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.StartTime = time.perf_counter()



    def test_load1(self):
        self.shield_mode = LoadEnvironmentLocal.shield_mode
        self.load_run_time = LoadEnvironmentLocal.load_run_time
        self.test_run_time = time.time() + 60 * self.load_run_time  # Gets current time + 60 seconds * required load run time
        self.remote_browser = LoadEnvironmentLocal.remote_browser
        self.proxy_address = LoadEnvironmentLocal.proxy_address
        self.chrome_driver_path = LoadEnvironmentLocal.chrome_driver_path
        self.headless_mode = LoadEnvironmentLocal.headless_mode
        self.tabs_count = LoadEnvironmentLocal.tabs_count
        self.wait_time_between_new_tabs = LoadEnvironmentLocal.wait_time_between_new_tabs
        # self.wait_time_before_browser_quit = LoadEnvironmentLocal.wait_time_before_browser_quit
        self.urls = LoadEnvironmentLocal.urls
        self.load_statistics_file = LoadEnvironmentLocal.load_statistics_file
        # self.parallel_actions = LoadEnvironmentLocal.parallel_actions
        self.ramp_up_time = LoadEnvironmentLocal.ramp_up_time
        self.max_concurrent_sessions = LoadEnvironmentLocal.max_concurrent_sessions
        self.max_session_time = LoadEnvironmentLocal.max_session_time


        def LoadBrowsers():
            Functions.Browse_open_x_tabs(self.load_statistics_file, self.remote_browser,
                                         self.proxy_address,
                                         self.chrome_driver_path,
                                         self.headless_mode,
                                         self.tabs_count,
                                         self.wait_time_between_new_tabs,
                                         self.max_session_time,
                                         self.shield_mode,
                                         self.urls)

        while time.time() < self.test_run_time:
            load_browsers = []
            # while len(load_browsers) < int(self.max_concurrent_sessions / self.tabs_count):
            for i in range(int(self.max_concurrent_sessions/self.tabs_count)):
                i = multiprocessing.Process(target=LoadBrowsers)
                load_browsers.append(i)


            instances = []

            for test in load_browsers:
                # while len(instances) < int(self.max_concurrent_sessions/self.tabs_count):
                test.start()
                instances.append(test)
                time.sleep(self.ramp_up_time)
                # # Sync all tests to finish together
                # for instance in instances:
                #     instance.join()

    @classmethod
    def tearDownClass(cls):
        cls.EndTime = time.perf_counter()
        print('Test ran for {}'.format(cls.EndTime - cls.StartTime))
        Functions.PrintText('Test ran for {}'.format(cls.EndTime - cls.StartTime))



if __name__ == '__main__':
    unittest.main()