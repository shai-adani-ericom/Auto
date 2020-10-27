from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import unittest,HtmlTestRunner, datetime, time, Functions, multiprocessing, LoadEnvironmentLocal
from load1_test_classLocal import load1

# print('Load test ran for {} seconds = {} minutes = {} hours'.format(total_run_time, total_run_time/60, total_run_time/3600))
# print('Browsers initiated {}'.format(i-1))
# print('Sessions initiated {}'.format((i-1)*tabs_count))

LoadEnvironmentLocal.load_statistics_file = Functions.CreateLoadStatisticsFile(LoadEnvironmentLocal.fileName,
                                                                          LoadEnvironmentLocal.shield_mode,
                                                                          LoadEnvironmentLocal.build_number)
# parallel_actions = LoadEnvironmentLocal.parallel_actions

#Test # 1
LoadTest = unittest.TestLoader().loadTestsFromTestCase(load1)

# create a test suite
test_suite = unittest.TestSuite([LoadTest])

# running tests suite
unittest.TextTestRunner(verbosity=2).run(test_suite)


# print('Load test ran for {} seconds = {} minutes = {} hours'.format(total_run_time, total_run_time/60, total_run_time/3600))
# print('Browsers initiated {}'.format(i-1))
# print('Sessions initiated {}'.format((i-1)*tabs_count))

# You only have 3 different levels for verbosity:
#
# 0 (quiet): you just get the total numbers of tests executed and the global result
# 1 (default): you get the same plus a dot for every successful test or a F for every failure
# 2 (verbose): you get the help string of every test and the result
