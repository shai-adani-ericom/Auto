from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import unittest,HtmlTestRunner, datetime, time

def Performance():
    # Use Navigation Timing  API to calculate the timings that matter the most
    navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
    responseStart = driver.execute_script("return window.performance.timing.responseStart")
    domComplete = driver.execute_script("return window.performance.timing.domComplete")

    ''' Calculate the performance'''
    responsetime_calc = responseStart - navigationStart
    pagefullload_calc = domComplete - responseStart
    round_trip = responsetime_calc + pagefullload_calc

    print("Response time: {} ms".format(str(responsetime_calc)))
    print("Page full load time: {} ms".format(str(pagefullload_calc)))
    print("Round trip : {} ms".format(str(round_trip)))


def OpenNewTab(*args):
    for i,arg in enumerate(args):
        print('Web page '+str(i) + ' ' + arg)
        time.sleep(1)
        driver.execute_script("window.open('" + str(arg) + "')")
        Performance()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[i+1])
        time.sleep(1)
class load_test(unittest.TestCase):

def PrepareGrid(browser_type, browser_version, os, instances_count):

    browser_path = '../drivers/chromedriver 81'
    driver = webdriver.Chrome(executable_path=browser_path)
    driver.get("http://tSs6t1WI7e9xBkIPeChaaaRShxbZVCdf:lvbEnYdk2dItng9sIgtJharoxtdjWgo7@ADANI.gridlastic.com/preset?"
               "&browserName1=chrome"
               "&browserVersion1=latest"
               "&platform1=win10"
               "&nodes1=5")



# Main
urls = ['http://www.google.com',
        'http://www.gmail.com',
        'http://www.cnn.com',
        'http://www.youtube.com',
        'http://www.instagram.com'
        ]
proxy_address = 'Shield-Load-80e1f451a8f2c519.elb.eu-central-1.amazonaws.com:3128'
options = ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--proxy-server=%s' % proxy_address)
options.add_argument('--disable-gpu')
options.add_argument("--start-maximized")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--no-sandbox')  # Bypass OS security model
options.add_argument('--disable-infobars')


for i in range (5):
    print('Starting the {} cycle'.format(i+1))
    driver = webdriver.Remote(
        command_executor="http://tSs6t1WI7e9xBkIPeChaaaRShxbZVCdf:lvbEnYdk2dItng9sIgtJharoxtdjWgo7@ADANI.gridlastic.com:80/wd/hub",
        desired_capabilities={
            # "browserName": "MicrosoftEdge",
            "browserName": "chrome",
            "browserVersion": "latest",
            "video": "True",
            "platform": "WIN10",
            "platformName": "windows",
        },
        options=options)
    print("Video: http://s3-eu-west-1.amazonaws.com/be8f5d0a-c2d2-9383-27b0-464cabf83d80/e97e4b2c-f903-9941-7915-dce56d84b8f0/play.html?" + driver.session_id)
    driver.implicitly_wait(3)
    driver.maximize_window()
    OpenNewTab(*urls)
    time.sleep(20)
    driver.quit()




