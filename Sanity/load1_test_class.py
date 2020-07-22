import unittest,HtmlTestRunner, datetime, time, Functions, LoadEnvironment, multiprocessing


class load1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.StartTime = time.perf_counter()



    def test_load1(self):
        self.shield_mode = LoadEnvironment.shield_mode
        self.load_run_time = LoadEnvironment.load_run_time
        self.test_run_time = time.time() + 60 * self.load_run_time  # Gets current time + 60 seconds * required load run time
        self.remote_browser = LoadEnvironment.remote_browser
        self.proxy_address = LoadEnvironment.proxy_address
        self.chrome_driver_path = LoadEnvironment.chrome_driver_path
        self.headless_mode = LoadEnvironment.headless_mode
        self.tabs_count = LoadEnvironment.tabs_count
        self.wait_time_between_new_tabs = LoadEnvironment.wait_time_between_new_tabs
        self.wait_time_before_browser_quit = LoadEnvironment.wait_time_before_browser_quit
        self.urls = LoadEnvironment.urls
        self.load_statistics_file = LoadEnvironment.load_statistics_file
        # self.parallel_actions = LoadEnvironment.parallel_actions
        self.ramp_up_time = LoadEnvironment.ramp_up_time
        self.max_concurrent_sessions = LoadEnvironment.max_concurrent_sessions
        self.max_session_time = LoadEnvironment.max_session_time


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
            # for i in range(self.parallel_actions):
            for i in range(int(self.max_concurrent_sessions/self.tabs_count)):
                i = multiprocessing.Process(target=LoadBrowsers)
                load_browsers.append(i)

            instances = []

            for test in load_browsers:
                test.start()
                instances.append(test)
                time.sleep(self.ramp_up_time)
            # Sync all tests to finish together
            for instance in instances:
                instance.join()

    @classmethod
    def tearDownClass(cls):
        cls.EndTime = time.perf_counter()
        print('Test ran for {}'.format(cls.EndTime - cls.StartTime))
        Functions.PrintText('Test ran for {}'.format(cls.EndTime - cls.StartTime))



if __name__ == '__main__':
    unittest.main()