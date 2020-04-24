#Environmet Details
#Shai Adani
#20/2/2020

results_log_file = '../TestResults/CristalResultsLogFile.txt'
chrome_results_log_file = '../TestResults/ChromeResultsLogFile.txt'
firefox_results_log_file = '../TestResults/FirefoxResultsLogFile.txt'
edge_results_log_file = '../TestResults/EdgeResultsLogFile.txt'
chrome_screenshot_path = '../TestResults/ChromeScreenshots/'
edge_screenshot_path = '../TestResults/EdgeScreenshots/'
firefox_screenshot_path = '../TestResults/FirefoxScreenshots/'
chrome_statistics_file = '../TestResults/ChromeCompareStatistics'
firefox_statistics_file = '../TestResults/FirefoxCompareStatistics'
edge_statistics_file = '../TestResults/EdgeCompareStatistics'
urls_file = '../FrameModeSanity/URLS2.txt'


chrome_driver_path = '../drivers/chromedriver'
firefox_driver_path = '../drivers/geckodriver'
edge_driver_path = '../drivers/msedgedriver'

jerusalem_proxy = '126.0.3.51:3128'
proxy = '136.244.105.218:3128'
proxy_state = 1  # 1 with proxy 0 without proxy

threshold = 0  # threshold in % for image comparison - crystal
shield_mode = 'Frame'  # Set shield mode = Crystal or Stream or Frame
shield_build = 'Staging 630'
healdless_mode = 1 # 1 true 0 false

