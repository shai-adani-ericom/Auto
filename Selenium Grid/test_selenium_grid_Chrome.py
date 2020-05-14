# file test_1.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#
# PROXY = "your_subdomain.gridlastic.com:8001"; # hosted Squid proxy on your selenium grid hub
# #PROXY = "your_subdomain.gridlastic.com:7001"; # An example Gridlastic Connect endpoint
#
# desired_capabilities['proxy'] = {
#     "httpProxy":PROXY,
#     "ftpProxy":PROXY,
#     "sslProxy":PROXY,
#     "noProxy":None,
#     "proxyType":"MANUAL",
#     "class":"org.openqa.selenium.Proxy",
#     "autodetect":False
# }

# driver = webdriver.Remote(
#     command_executor="http://tSs6t1WI7e9xBkIPeChaaaRShxbZVCdf:lvbEnYdk2dItng9sIgtJharoxtdjWgo7@ADANI.gridlastic.com:80/wd/hub",
#     desired_capabilities={
#         "browserName": "chrome",
#         "browserVersion": "latest",
#         "video": "False",
#         "platform": "WIN10",
#         "platformName": "windows",
#     })
driver = webdriver.Remote(
    command_executor="http://tSs6t1WI7e9xBkIPeChaaaRShxbZVCdf:lvbEnYdk2dItng9sIgtJharoxtdjWgo7@ADANI.gridlastic.com:80/wd/hub",
    desired_capabilities={
        "browserName": "firefox",
        "browserVersion": "75",
        "video": "True",
        "platform": "WIN10",
        "platformName": "windows",
    })
print("Video: " + driver.session_id)

try:
    driver.implicitly_wait(30)
    driver.maximize_window()  # Note: driver.maximize_window does not work on Linux selenium version v2, instead set window size and window position like driver.set_window_position(0,0) and driver.set_window_size(1920,1080)
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.send_keys("documentation")
    elem.send_keys(Keys.RETURN)
    time.sleep(10)
    assert "No results found." not in driver.page_source
finally:
    driver.quit()