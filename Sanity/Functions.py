import os,time, datetime, shutil, csv, unittest, HtmlTestRunner, cv2, csv, pyautogui, paramiko, subprocess, select, glob
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import FirefoxOptions
##############################################################
def StartBrowser(browser_type, browser_path,shield_status, headless_mode, proxy_address):


    if 'chromedriver' in browser_type:
        try:
            options = ChromeOptions()

            if shield_status == 'ON':
                options.add_argument('--proxy-server=%s' % proxy_address)
            if headless_mode == 1:
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')
                options.add_argument("--start-maximized")
            # options.add_argument('user-data-dir=/Users/shaiadani/Library/Application Support/Google/Chrome/Default')
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--no-sandbox')  # Bypass OS security model
            options.add_argument('--disable-infobars')
            options.add_experimental_option('prefs', {'profile.default_content_settings.cookies': 1, 'safebrowsing.enabled': False})
            driver = webdriver.Chrome(options=options, executable_path=browser_path)
            driver.set_window_size('1920', '878')
            return driver
        except:
            PrintText('Error occurred in StartBrowser function')
            exit('Error occurred in StartBrowser function')
    elif 'geckodriver' in browser_type:
        options = FirefoxOptions()
        desired_capability = webdriver.DesiredCapabilities.FIREFOX
        try:
            if shield_status == 'ON':
                proxy = proxy_address
                desired_capability['proxy'] = {
                    'proxyType': "manual",
                    'httpProxy': proxy,
                    'ftpProxy': proxy,
                    'sslProxy': proxy,
                }

            if headless_mode == 1:
                options.add_argument('--headless')

            options.add_argument('--no-sandbox')  # Bypass OS security model
            options.add_argument('--disable-infobars')
            driver = webdriver.Firefox(options=options,capabilities=desired_capability,executable_path=browser_path)
            driver.set_window_size('1920', '900')
            return driver
        except:
            PrintText('Error occurred in StartBrowser function')
            exit('Error occurred in StartBrowser function')

##############################################################
def GoToURL(driver, url, headless_mode):

    try:
        PrintText('URL is ' + url )
        driver.get(url)  # open browser with specific site
        if headless_mode == 0:
            driver.maximize_window()  # maximize window
        # time.sleep(10)
    except:
        PrintText('Error occurred in GoToURL function')
        exit('Error occurred in GoToURL function')

##############################################################
def EnterTextToField(driver, wait_time,locate_by_method, object_recognizer, text_to_enter, focus = 'ON' ):
    try:
        if locate_by_method == 'ID':
            if focus != 'OFF':
                scrollToElement = WebDriverWait(driver, wait_time).until(
                    EC.presence_of_element_located((By.ID, object_recognizer)))
                driver.execute_script("arguments[0].scrollIntoView();", scrollToElement)
            WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.ID, object_recognizer))).send_keys(text_to_enter)
        elif locate_by_method == 'NAME':
            if focus != 'OFF':
                scrollToElement = WebDriverWait(driver, wait_time).until(
                    EC.presence_of_element_located((By.NAME, object_recognizer)))
                driver.execute_script("arguments[0].scrollIntoView();", scrollToElement)
            WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.NAME, object_recognizer))).send_keys(text_to_enter)
        elif locate_by_method == 'XPATH':
            if focus != 'OFF':
                scrollToElement = WebDriverWait(driver, wait_time).until(
                    EC.presence_of_element_located((By.XPATH, object_recognizer)))
                driver.execute_script("arguments[0].scrollIntoView();", scrollToElement)
            WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.XPATH, object_recognizer))).send_keys(text_to_enter)
        time.sleep(3)
    except:
        PrintText('Error occurred in EnterTextToField function')

        exit('Error occurred in EnterTextToField function')
##############################################################
def PressOnObject(driver, wait_time,locate_by_method, object_recognizer, focus = 'ON'):
    try:
        if locate_by_method == 'ID':
            if focus != 'OFF':
                scrollToElement = WebDriverWait(driver, wait_time).until(
                    EC.presence_of_element_located((By.ID, object_recognizer)))
                driver.execute_script("arguments[0].scrollIntoView();", scrollToElement)
            WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.ID, object_recognizer))).click()
        elif locate_by_method == 'NAME':
            if focus != 'OFF':
                scrollToElement = WebDriverWait(driver, wait_time).until(
                    EC.presence_of_element_located((By.NAME, object_recognizer)))
                driver.execute_script("arguments[0].scrollIntoView();", scrollToElement)
            WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.NAME, object_recognizer))).click()
        elif locate_by_method == 'XPATH':
            if focus != 'OFF':
                scrollToElement = WebDriverWait(driver, wait_time).until(
                    EC.presence_of_element_located((By.XPATH, object_recognizer)))
                driver.execute_script("arguments[0].scrollIntoView();", scrollToElement)
            WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.XPATH, object_recognizer))).click()
        time.sleep(3)

    except:
        PrintText('Error occurred in PressOnObject function')
        # exit('Error occurred in PressOnObject function')
##############################################################
def CheckObjectText(driver, wait_time,locate_by_method, object_recognizer, expected_text, focus = 'ON'):
    try:
        if locate_by_method == 'ID':
            if focus != 'OFF':
                scrollToElement = WebDriverWait(driver, wait_time).until(
                    EC.presence_of_element_located((By.ID, object_recognizer)))
                driver.execute_script("arguments[0].scrollIntoView();", scrollToElement)

            if WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.ID, object_recognizer))).text == expected_text:
                PrintText('Object text match expected')
            else:
                exit('Object text does not match expected')
        elif locate_by_method == 'NAME':
            if focus != 'OFF':
                scrollToElement = WebDriverWait(driver, wait_time).until(
                    EC.presence_of_element_located((By.NAME, object_recognizer)))
                driver.execute_script("arguments[0].scrollIntoView();", scrollToElement)

            if WebDriverWait(driver, wait_time).until(
                    EC.presence_of_element_located((By.NAME, object_recognizer))).text == expected_text:
                PrintText('Object text match expected')
            else:
                exit('Object text does not match expected')
        elif locate_by_method == 'XPATH':
            if focus != 'OFF':
                scrollToElement = WebDriverWait(driver, wait_time).until(
                    EC.presence_of_element_located((By.XPATH, object_recognizer)))
                driver.execute_script("arguments[0].scrollIntoView();", scrollToElement)
            if WebDriverWait(driver, wait_time).until(
                    EC.presence_of_element_located((By.XPATH, object_recognizer))).text == expected_text:
                PrintText('Object text match expected')
            else:
                exit('Object text does not match expected')
    except:
        PrintText('Error occurred in CheckObjectText function')
        return -1
        # exit('Error occurred in CheckObjectText function')
######################################################################
def SelectOptionFromList(driver, wait_time,locate_by_method, object_recognizer, option, focus = 'ON'):
    try:
        if locate_by_method == 'NAME':
            if focus != 'OFF':
                scrollToElement = WebDriverWait(driver, wait_time).until(
                    EC.presence_of_element_located((By.NAME, object_recognizer)))
                driver.execute_script("arguments[0].scrollIntoView();", scrollToElement)
            select_list_values = driver.find_element_by_name(object_recognizer)
            values = select_list_values.find_elements_by_tag_name('option')
            for value in values:
                # print(value.text)
                if value.text == option:
                    value.click()
                    # print('Option Clicked')
                    break
                else:
                    PrintText('Option not found')
        elif locate_by_method == 'XPATH':
            if focus != 'OFF':
                scrollToElement = WebDriverWait(driver, wait_time).until(
                    EC.presence_of_element_located((By.XPATH, object_recognizer)))
                driver.execute_script("arguments[0].scrollIntoView();", scrollToElement)
            # print('Object found')
            select_list_values = driver.find_element_by_xpath(object_recognizer)
            values = select_list_values.find_elements_by_tag_name('option')
            for value in values:
                # print(value.text)
                if value.text == option:
                    value.click()
                    # print('Option Clicked')
                    break
                else:
                    PrintText('Option not found')
        elif locate_by_method == 'ID':
            if focus != 'OFF':
                scrollToElement = WebDriverWait(driver, wait_time).until(
                    EC.presence_of_element_located((By.ID, object_recognizer)))
                driver.execute_script("arguments[0].scrollIntoView();", scrollToElement)
            # print('Object found')
            select_list_values = driver.find_element_by_id(object_recognizer)
            values = select_list_values.find_elements_by_tag_name('option')
            for value in values:
                # print(value.text)
                if value.text == option:
                    value.click()
                    # print('Option Clicked')
                    break
                else:
                    PrintText('Option not found</br>')

    except:
        PrintText('Error occurred in SelectOptionFromList function')
        exit('Error occurred in SelectOptionFromList function')

######################################################################
def SwitchToFrame(driver, wait_time,locate_by_method, object_recognizer):
    try:
        if locate_by_method == 'ID':
                WebDriverWait(driver, wait_time).until(EC.frame_to_be_available_and_switch_to_it((By.ID, object_recognizer)))
                # print('Frame located and switch to')
        elif locate_by_method == 'NAME':
                WebDriverWait(driver, wait_time).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, object_recognizer)))
                # print('Frame located and switch to')
        elif locate_by_method == 'XPATH':
            WebDriverWait(driver, wait_time).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, object_recognizer)))
            # print('Frame located and switch to')
    except:
        PrintText('Error occurred in WaitForObjectInPage function')
        exit('Error occurred in WaitForObjectInPage function')

######################################################################
def AlertHandling(driver, wait_time, user, password='None', action='None'):

    try:
        WebDriverWait(driver, wait_time).until(EC.alert_is_present())
        if action == 'OK':
            driver.switch_to_alert().accept()  # close the pop up\alert by selecting OK
        elif action == 'CANCEL':
            driver.switch_to_alert().dismiss()  # close the pop up\alert by selecting Cancel
        else:
            driver.switch_to_alert().accept()  # close the pop up\alert by selecting OK

    except:
            PrintText('Alert window was not found')
            # exit('Alert window was not found')
######################################################################
def PrintText(text):

    print(str(
        datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S') + ' ' + text + '</br>'))

######################################################################
def VerifyFrameModePageLoaded(driver, wait_time, text_in_page_title):
    try:
        time.sleep(10)
        WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.ID, 'canvas')))
        if text_in_page_title in str(driver.title):
            PrintText('Frame page loaded with the title ' + str(driver.title) + ' step *PASS*')
        else:
            PrintText('Frame page loaded with unexpected title ' + str(driver.title) + ' step *FAIL*')
    except:
        PrintText('Frame mode page not loaded correctly')
        exit('Frame mode page not loaded correctly')

######################################################################
def VerifyPageBlockedByAuth(driver, wait_time, locate_by_method, object_recognizer):
    time.sleep(10)
    try:
        if locate_by_method == 'ID':
            WebDriverWait(driver, wait_time).until(EC.invisibility_of_element((By.ID, object_recognizer )))
            PrintText(' Page access blocked in Basic Authentication mode - step - *PASS*')
    except:
        PrintText(' Page access was not blocked in Basic Authentication mode - step - *FAIL*' )
        exit(' Page access was not blocked in Basic Authentication mode - step - *FAIL*')

######################################################################
def EnterUserPasswordInAuthWindow(user , password):

    time.sleep(3)
    pyautogui.typewrite(user)
    time.sleep(2)
    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.typewrite(password)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)

######################################################################
def InstallUpdateShield(machine_ip, username, password, branch='dev', env = 'new'):# env = 'new' - new environment env='exisiting' - exisiting environmet
    time.sleep(5)
    if env != 'new':
        try:
            if branch == 'dev':
                commands = 'cd /root/ericomshield/;' \
                           ' wget https://raw.githubusercontent.com/EricomSoftwareLtd/Shield/Dev/Kube/scripts/install-shield-from-container.sh -O install-shield-from-container.sh;' \
                           ' chmod +x install-shield-from-container.sh; ' \
                           'sudo ./install-shield-from-container.sh -d -l -p Erixxx98xxx$'
                # commandsOrg = 'cd /root/ericomshield/;' \
                #            ' wget https://raw.githubusercontent.com/EricomSoftwareLtd/Shield/Dev/Kube/scripts/install-shield.sh -O install-shield.sh;' \
                #            ' chmod +x install-shield.sh; ' \
                #            'sudo ./install-shield.sh -R -l -d -p Ericom123$'
            elif branch == 'staging':
                commands = 'cd /root/ericomshield/;' \
                           ' wget https://raw.githubusercontent.com/EricomSoftwareLtd/Shield/Dev/Kube/scripts/install-shield.sh -O install-shield.sh;' \
                           ' chmod +x install-shield.sh; ' \
                           'sudo ./install-shield.sh -R -l -s -p Ericom123$'

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # ssh.connect(hostname=machine_ip, username=username, password=password, look_for_keys=False)
            ssh.connect(hostname=machine_ip, username=username, password=password)

            stdin, stdout, stderr = ssh.exec_command(commands, get_pty=True)
            for line in iter(stdout.readline, ''):
                print(line, end='')
            print(' Shield upgrade done - step *PASS*')
            ssh.close()
            # time.sleep(180) # Wait for new version containers to start
        except:
            PrintText(' Error occurred during shield machine connected or update  - step - *FAIL*' )
            exit(' Error occurred during shield machine connected or update  - step - *FAIL*')
    else:
        try:
            if branch == 'dev':
                commands = 'cd /root/ericomshield/;' \
                           ' wget https://raw.githubusercontent.com/EricomSoftwareLtd/Shield/Dev/Kube/scripts/install-shield.sh -O install-shield.sh;' \
                           ' chmod +x install-shield.sh; ' \
                           'sudo ./install-shield.sh -R -l -d -p Ericom123$'
            elif branch == 'staging':
                commands = 'cd /root/ericomshield/;' \
                           ' wget https://raw.githubusercontent.com/EricomSoftwareLtd/Shield/Dev/Kube/scripts/install-shield.sh -O install-shield.sh;' \
                           ' chmod +x install-shield.sh; ' \
                           'sudo ./install-shield.sh -R -l -s -p Ericom123$'

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # ssh.connect(hostname=machine_ip, username=username, password=password, look_for_keys=False)
            ssh.connect(hostname=machine_ip, username=username, password=password)

            stdin, stdout, stderr = ssh.exec_command(commands, get_pty=True)
            for line in iter(stdout.readline, ''):
                print(line, end='')
            print(' Successfully connected and installed on new clean machine - step *PASS*')
            ssh.close()
        except:
            PrintText(' Error occurred during shield machine connected or update  - step - *FAIL*' )
            exit(' Error occurred during shield machine connected or update  - step - *FAIL*')


######################################################################
def CheckRunnigImagesVersions(machine_ip, username, password='None'):

    try:

        commands = 'cd /root/ericomshield/;' \
                   'pip3 install pyyaml==5.3.1;'

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # ssh.connect(hostname=machine_ip, username=username, password=password, look_for_keys=False)
        ssh.connect(hostname=machine_ip, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(commands, get_pty=True)
        for line in iter(stdout.readline, ''):
            print(line, end='')
        print(' pip3 install pyyaml==5.3.1 done - step *PASS*')
        ssh.close()
    except:
        PrintText(' Error occurred during pip3 install pyyaml==5.3.1  - step - *FAIL*' )
        exit(' Error occurred during pip3 install pyyaml==5.3.1  - step - *FAIL*')
    time.sleep(10)
    try:
        commands = 'cd /root/ericomshield/;' \
                   'python3 checktags.py'
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # ssh.connect(hostname=machine_ip, username=username)
        # ssh.connect(hostname=machine_ip, username=username, password=password, look_for_keys=False)
        ssh.connect(hostname=machine_ip, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(commands, get_pty=True)
        for line in iter(stdout.readline, ''):
            print(line, end='')
            if '*****all images as should*****' in line:
                print(' CheckRunnigImagesVersions *****all images as should***** - step *PASS*')
        ssh.close()
    except:
        PrintText(' Error occurred during CheckRunnigImagesVersions  - step - *FAIL*')
        exit(' Error occurred during CheckRunnigImagesVersions  - step - *FAIL*')

######################################################################
def VerifyElementInvisibility(driver, wait_time, locate_by_method, object_recognizer):

    time.sleep(5)
    try:
        if locate_by_method == 'ID':
            WebDriverWait(driver, wait_time).until(EC.invisibility_of_element((By.ID, object_recognizer)))
            PrintText(' Element invisible - step - *PASS* ' + locate_by_method + ' ' + object_recognizer)
            return 1
        elif locate_by_method == 'XPATH':
            WebDriverWait(driver, wait_time).until(EC.invisibility_of_element((By.XPATH, object_recognizer)))
            PrintText(' Element invisible - step - *PASS* ' + locate_by_method + ' ' + object_recognizer)
            return 1
        elif locate_by_method == 'NAME':
            WebDriverWait(driver, wait_time).until(EC.invisibility_of_element((By.NAME, object_recognizer)))
            PrintText(' Element invisible - step - *PASS* ' + locate_by_method + ' ' + object_recognizer)
            return 1
    except:
        PrintText(' Element is visible - step - *FAIL* ' + locate_by_method + ' ' + object_recognizer)
        exit(' Element is visible - step - *FAIL* ' + locate_by_method + ' ' + object_recognizer)

######################################################################
def VerifyFileDownload(driver, wait_time,  download_button_locate_by_method,
                       download_button_object_recognizer, download_folder, file_name):

    try:
        os.system('cd '+ download_folder+'; rm -Rf *.pdf')

        PressOnObject(driver, wait_time, download_button_locate_by_method, download_button_object_recognizer)
        time.sleep(30)
        if os.path.exists(download_folder+file_name):
            PrintText('Ericom downloaded file appears -  step *PASS*')
        else:
            PrintText('Ericom downloaded file  did not appear -  step *FAIL*')
            exit('Ericom downloaded file did not appear -  step *FAIL*')
    except:
        PrintText('Error occurred during VerifyFileDownload function  -  step *FAIL*')
        exit('Error occurred during VerifyFileDownload function  -  step *FAIL*')
######################################################################
def VerifyElementIsVisible(driver, wait_time, locate_by_method, object_recognizer):

    time.sleep(5)
    try:
        if locate_by_method == 'ID':
            WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.ID, object_recognizer)))
            PrintText(' Element is visible - step - *PASS* ' + locate_by_method + ' ' + object_recognizer)
        elif locate_by_method == 'NAME':
            WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.NAME, object_recognizer)))
            PrintText(' Element is visible - step - *PASS* ' + locate_by_method + ' ' + object_recognizer)
        elif locate_by_method == 'XPATH':
            WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, object_recognizer)))
            PrintText(' Element is visible - step - *PASS* ' + locate_by_method + ' ' + object_recognizer)
    except:
        PrintText(' Element is not visible - step - *FAIL* ' + locate_by_method + ' ' + object_recognizer)
        exit(' Element is not visible - step - *FAIL* ' + locate_by_method + ' ' + object_recognizer)
######################################################################
def AdminLogin(admin_driver, wait_time, admin_address):
        PrintText('Admin login started')
        time.sleep(5)
        GoToURL(admin_driver,admin_address, 0 )
        EnterTextToField(admin_driver, wait_time,'NAME', 'username', 'admin')
        EnterTextToField(admin_driver, wait_time, 'NAME', 'password', 'ericomshield')
        PressOnObject(admin_driver, wait_time, 'ID', 'login-submit')
        PrintText('Admin login ended')
######################################################################
def HitEnter():

    pyautogui.press('enter')
######################################################################
def CheckIfPageBlocked(driver, wait_time):

    try:
        time.sleep(10)
        expected_text = 'This URL has been blocked by your system administrator'
        print(WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.TAG_NAME, 'h1'))).text)

        if expected_text in  WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.TAG_NAME, 'h1'))).text:
            PrintText( ' Page was successfully blocked ' + str(driver.title) + ' step - *PASS*')
        else:
            PrintText(' Page was not blocked ' + str(driver.title) + ' step - *FAIL*')
            exit(' Page was not blocked ' + str(driver.title) + ' step - *FAIL*')
    except:
        PrintText(' Error occurred during CheckIfPageBlocked function - step - *FAIL*')
        exit(' Error occurred during CheckIfPageBlocked function - step - *FAIL*')
######################################################################
def SearchValuesInTable(driver, wait_time, object_recognizer, *args): # plenavia.cl - black - Phishing 'Block' Policy -	Suspected

    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, object_recognizer)))
    table = driver.find_element(By.XPATH, object_recognizer)
    table_rows = table.find_elements(By.TAG_NAME, 'tr')

    for row in table_rows:

        columns = row.find_elements(By.TAG_NAME, 'td')

        for arg in args:
            for column in columns:
                if arg == column.text:
                    PrintText(column.text + ' found in table - step *PASS*')
                    break

def CreateNewCleanMachine(browser_type, browser_path, shield_status, headless_mode, proxy_address,
                          jenkins_url, jenkins_user, jenkins_password, email):

    driver = StartBrowser(browser_type, browser_path, shield_status, headless_mode, proxy_address)
    GoToURL(driver,jenkins_url, headless_mode)
    EnterTextToField(driver, 10, 'ID', 'j_username', jenkins_user)
    EnterTextToField(driver, 10, 'NAME', 'j_password', jenkins_password)
    PressOnObject(driver, 10,'NAME', 'Submit')
    time.sleep(5)

    PressOnObject(driver, 10, 'XPATH', '//*[@id="tasks"]/div[4]/a[1]', focus='OFF')
    SelectOptionFromList(driver, 10, 'XPATH', '//*[@id="main-panel"]/form/table/tbody[1]/tr[1]/td[3]/div/select', email, focus='OFF')
    SelectOptionFromList(driver, 10, 'XPATH', '//*[@id="main-panel"]/form/table/tbody[2]/tr[1]/td[3]/div/select', 'clean', focus='OFF')
    SelectOptionFromList(driver, 10, 'XPATH', '//*[@id="main-panel"]/form/table/tbody[3]/tr[1]/td[3]/div/select',
                         '2', focus='OFF')
    PressOnObject(driver, 10, 'ID', 'yui-gen1-button', focus='OFF')
    time.sleep(5)
    driver.quit()


def ActivateNewEnv(browser_type, chrome_driver_path,shield_status ,
                   headless_mode, proxy_address,wait_time, admin_address,
                   activation_portal_url, activation_portal_user, activation_portal_password):
    # open Admin
    admin_driver = StartBrowser(browser_type, chrome_driver_path, shield_status, headless_mode, proxy_address)
    #Admin Login
    AdminLogin(admin_driver, wait_time, admin_address)
    time.sleep(3)
    #Get serial
    PressOnObject(admin_driver, wait_time, 'XPATH',
                  '//*[@id="wrapper"]/app-root/cc-container-with-menu/cc-dashboard-container/cc-dashboard/div[2]/cc-modal/div/div/div/div[3]/table/tbody/tr/td[2]/div/button')
    time.sleep(3)
    PressOnObject(admin_driver,wait_time,'XPATH', '//*[@id="username-menu-button"]/span')
    time.sleep(3)
    PressOnObject(admin_driver, wait_time, 'XPATH', '//*[@id="header"]/nav/ul/li/ul/li[1]/a/span')
    time.sleep(3)

    system_id = WebDriverWait(admin_driver, wait_time).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div/form/div/div/div[1]/div/input'))).get_attribute('value')
    print('System ID = {}'.format(system_id))

    # Open activation poratl
    admin_driver.execute_script("window.open('"+activation_portal_url+"')")
    admin_driver.switch_to.window(admin_driver.window_handles[1])
    time.sleep(2)
    EnterTextToField(admin_driver, 10, 'XPATH', '//*[@id="username"]', activation_portal_user)
    time.sleep(2)
    EnterTextToField(admin_driver, 10, 'XPATH', '//*[@id="password"]', activation_portal_password)
    time.sleep(2)
    PressOnObject(admin_driver, 10,'XPATH', '//*[@id="submit"]')
    time.sleep(5)

    #Open activation poratl
    SelectOptionFromList(admin_driver, wait_time, 'ID', 'user_name', 'Orit Gaon', 'ON')
    EnterTextToField(admin_driver, 10, 'ID', 'opportunity_name', 'TEST')
    EnterTextToField(admin_driver, 10, 'ID', 'system_id', system_id)
    SelectOptionFromList(admin_driver, wait_time, 'NAME', 'license_type', 'Evaluation', 'ON')
    SelectOptionFromList(admin_driver, wait_time, 'NAME', 'license_mode', 'Concurrent User', 'ON')
    PressOnObject(admin_driver, wait_time, 'ID', 'submit', 'ON')
    time.sleep(3)
    system_key = WebDriverWait(admin_driver, wait_time).until(
        EC.presence_of_element_located((By.ID, 'Key'))).get_attribute('value')
    print('System KEY = {}'.format(system_key))

    admin_driver.switch_to.window(admin_driver.window_handles[0])  # switch to Admin window
    time.sleep(3)
    EnterTextToField(admin_driver, 10, 'XPATH', '//*[@id="content"]/div/div/form/div/div/div[2]/div/input', system_key)
    time.sleep(3)
    PressOnObject(admin_driver, wait_time, 'XPATH', '//*[@id="middle"]/div[2]/button', 'ON')

    time.sleep(10)

    admin_driver.quit()

def ConfigNewEnvAdmin(browser_type, chrome_driver_path,shield_status ,
                   headless_mode, proxy_address,wait_time, admin_address): # After system activation - tech mode, active directory, redirect
    # open Admin
    admin_driver = StartBrowser(browser_type, chrome_driver_path, shield_status, headless_mode, proxy_address)
    # Admin Login
    AdminLogin(admin_driver, wait_time, admin_address)
    time.sleep(3)
    # Go to Setting->General-> Enable Tech Preview = Yes
    PressOnObject(admin_driver, wait_time, 'XPATH', '//*[@id="el_3"]/a/span', 'ON')
    time.sleep(2)
    PressOnObject(admin_driver, wait_time, 'XPATH', '//*[@id="nobackgroundcontent"]/cc-toggle[1]/div/label', 'ON')
    time.sleep(2)
    SelectOptionFromList(admin_driver, wait_time, 'XPATH', '//*[@id="nobackgroundcontent"]/cc-toggle[1]/div/div/div[6]/div/select', 'Yes', 'ON')
    time.sleep(2)
    PressOnObject(admin_driver, wait_time, 'XPATH', '//*[@id="wrapper"]/app-root/cc-container-with-menu/cc-settings-container/cc-settings/div/div[2]/button[1]', 'ON')
    time.sleep(2)
    # Go to Setting->Proxy & Integration -> Enable Redirection Mode = Yes
    PressOnObject(admin_driver, wait_time, 'XPATH', '//*[@id="el_3"]/a/span', 'ON')
    time.sleep(2)
    PressOnObject(admin_driver, wait_time, 'XPATH', '//*[@id="nobackgroundcontent"]/cc-toggle[8]/div/label', 'ON')
    time.sleep(2)

    SelectOptionFromList(admin_driver, wait_time, 'XPATH',
                         '//*[@id="nobackgroundcontent"]/cc-toggle[8]/div/div/div[6]/div/select', 'Yes', 'ON')
    time.sleep(2)
    PressOnObject(admin_driver, wait_time, 'XPATH',
                  '//*[@id="wrapper"]/app-root/cc-container-with-menu/cc-settings-container/cc-settings/div/div[2]/button[1]',
                  'ON')
    time.sleep(2)
    # Go to Profiles->Active Directory Authentication->Primary Active Directory Settings-> Config Proxy
    PressOnObject(admin_driver, wait_time, 'XPATH', '//*[@id="el_5"]/a/span', 'ON')
    time.sleep(2)
    PressOnObject(admin_driver, wait_time, 'XPATH', '//*[@id="nobackgroundcontent"]/cc-toggle[3]/div/label', 'ON')
    time.sleep(2)
    PressOnObject(admin_driver, wait_time, 'XPATH', '//*[@id="nobackgroundcontent"]/cc-toggle[3]/div/div/cc-toggle[1]/div/label', 'ON')
    time.sleep(2)
    EnterTextToField(admin_driver, 10, 'XPATH', '//*[@id="nobackgroundcontent"]/cc-toggle[3]/div/div/cc-toggle[1]/div/div/div[1]/div/input', 'shield.local')
    time.sleep(2)
    EnterTextToField(admin_driver, 10, 'XPATH', '//*[@id="nobackgroundcontent"]/cc-toggle[3]/div/div/cc-toggle[1]/div/div/div[2]/div/input', '192.168.1.6')
    time.sleep(2)
    SelectOptionFromList(admin_driver, wait_time, 'XPATH',
                         '//*[@id="nobackgroundcontent"]/cc-toggle[3]/div/div/cc-toggle[1]/div/div/div[3]/div/select', 'No', 'ON')
    time.sleep(2)
    EnterTextToField(admin_driver, 10, 'XPATH',
                     '//*[@id="nobackgroundcontent"]/cc-toggle[3]/div/div/cc-toggle[1]/div/div/div[4]/div/input',
                     'DC=shield,DC=local')
    time.sleep(2)
    EnterTextToField(admin_driver, 10, 'XPATH',
                     '//*[@id="nobackgroundcontent"]/cc-toggle[3]/div/div/cc-toggle[1]/div/div/div[5]/div/input',
                     'admintest')
    time.sleep(2)
    EnterTextToField(admin_driver, 10, 'XPATH',
                     '//*[@id="nobackgroundcontent"]/cc-toggle[3]/div/div/cc-toggle[1]/div/div/div[6]/div/input',
                     'qwer432!')
    time.sleep(2)
    PressOnObject(admin_driver, wait_time, 'XPATH', '//*[@id="contentprofile"]/div/div[1]/div[2]/input', 'ON')
    time.sleep(2)
    admin_driver.quit()



def CheckBackUpRetore(machine_ip, username, password , browser_type, chrome_driver_path,shield_status ,
                   headless_mode, proxy_address,wait_time, admin_address, file_path):

    # Go to shield machine and verify backup and daily folders exists
        try:
            commands = 'ls /home/ericom/shield/'

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=machine_ip, username=username, password=password)

            stdin, stdout, stderr = ssh.exec_command(commands, get_pty=True)
            for line in iter(stdout.readline, ''):
                print(line, end='')
                if 'backup' in line and 'daily' in line:
                    PrintText('backup and daily folders appear in /home/ericom/shield - step - *PASS*')
                else:
                    PrintText('backup and\or daily folders not appear in /home/ericom/shield - step - *FAIL*')
                    PrintText('ls output in /home/ericom/shield/ is {}'.format(line))
            ssh.close()
        except:
            PrintText(' Error occurred during CheckBackUpRetore  - step - *FAIL*')
            exit(' Error occurred during CheckBackUpRetore  - step - *FAIL*')

        # Clean previous backups
        try:
            commands = 'rm -Rf /home/ericom/shield/backup/*.json;' \
           'ls /home/ericom/shield/backup/'

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=machine_ip, username=username, password=password)

            stdin, stdout, stderr = ssh.exec_command(commands, get_pty=True)
            for line in iter(stdout.readline, ''):
                print(line, end='')
                if '.json' not in str(line):
                    PrintText('Previous backup files were deleted from  /home/ericom/shield/backup - step - *PASS*')
                else:
                    PrintText('Previous backup files were not deleted from  /home/ericom/shield/backup - step - *FAIL*')
                    PrintText('ls output in /home/ericom/shield/backup/ is {}'.format(line))
            ssh.close()
        except:
            PrintText(' Error occurred during CheckBackUpRetore  - step - *FAIL*')
            exit(' Error occurred during CheckBackUpRetore  - step - *FAIL*')

        # Perform change in Admin
        # open Admin
        admin_driver = StartBrowser(browser_type, chrome_driver_path, shield_status, headless_mode, proxy_address)
        # Admin Login
        AdminLogin(admin_driver, wait_time, admin_address)
        time.sleep(3)

        # Go to Policies page
        PressOnObject(admin_driver, wait_time, 'XPATH', '//*[@id="el_1"]/a/span')
        # Edit Default - All Domain
        PressOnObject(admin_driver, wait_time, 'XPATH',
                                '//*[@id="policies-grid"]/vaadin-grid-cell-content[69]/vaadin-checkbox')
        PressOnObject(admin_driver, wait_time, 'XPATH',
                                '//*[@id="content"]/div/div/div[1]/div/div[1]/ul/li[2]/i')
        # Policies - Edit Default - All Domain
        PrintText('Policies - Edit Default - All Domain - Shield/Crystal/Ignore certificate')
        SelectOptionFromList(admin_driver, wait_time, 'NAME', 'access', 'White')
        time.sleep(1)
        SelectOptionFromList(admin_driver, wait_time, 'NAME', 'media', 'Crystal')
        time.sleep(1)
        SelectOptionFromList(admin_driver, wait_time, 'NAME', 'certificate',
                                       'Ignore')
        time.sleep(1)
        # Save
        PressOnObject(admin_driver, wait_time, 'XPATH',
                        '//*[@id="middle"]/div[2]/cc-modal/div/div/div/div[3]/table/tbody/tr/td[2]/div/button[1]')
        time.sleep(3)

        # Verify backup was created  /home/ericom/shield/ backup daily
        try:
            commands = 'cd /home/ericom/shield/backup/; ls'

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=machine_ip, username=username, password=password)

            stdin, stdout, stderr = ssh.exec_command(commands, get_pty=True)
            for line in iter(stdout.readline, ''):
                print(line, end='')
                if '.json' in str(line):
                    PrintText('Backup file was successfully created under /home/ericom/shield/backup - step - *PASS*')
                else:
                    PrintText('Backup file was not  created under  /home/ericom/shield/backup - step - *FAIL*')
                    PrintText('ls output in /home/ericom/shield/backup/ is {}'.format(line))
                    exit('Backup file was not  created under  /home/ericom/shield/backup - step - *FAIL*')
            ssh.close()
        except:
            PrintText(' Error occurred during CheckBackUpRetore  - step - *FAIL*')
            exit(' Error occurred during CheckBackUpRetore  - step - *FAIL*')


        # Go to Admin, use backup file in order to local folder and restore previous backup  machine_ip, username=username, password=password)

        # Settings -> Restore -> Choose File -> Go to folder -> select backup.json -> Open -> Restore shield -> Yes! Restore -> Wait 20 sec
        PressOnObject(admin_driver, wait_time, 'XPATH', '//*[@id="el_3"]/a/span', file_path)
        time.sleep(2)
        PressOnObject(admin_driver, wait_time, 'XPATH', '//*[@id="nobackgroundcontent"]/cc-toggle[13]/div/label')
        time.sleep(2)
        UploadFile(admin_driver, wait_time, 'XPATH','//*[@id="restoreUploadFile"]', file_path)
        time.sleep(2)
        PressOnObject(admin_driver, wait_time, 'XPATH', '//*[@id="nobackgroundcontent"]/cc-toggle[13]/div/div/div/button')
        time.sleep(2)
        PressOnObject(admin_driver, wait_time, 'XPATH', '//*[@id="wrapper"]/app-root/cc-container-with-menu/cc-settings-container/cc-settings/cc-modal[5]/div/div/div/div[3]/table/tbody/tr/td[2]/div/button[1]')
        time.sleep(60)

        # Verify system configuration restored
        # Go to Policies page
        PressOnObject(admin_driver, wait_time, 'XPATH', '//*[@id="el_1"]/a/span')
        PressOnObject(admin_driver, wait_time, 'XPATH',
                                '//*[@id="policies-grid"]/vaadin-grid-cell-content[69]/vaadin-checkbox')
        PressOnObject(admin_driver, wait_time, 'XPATH',
                                '//*[@id="content"]/div/div/div[1]/div/div[1]/ul/li[2]/i')
        # Policies - Edit Default - All Domain
        PrintText(' Policies - Edit Default - All Domain - Checking that Rendering mode is Stream')
        PrintText('Media field valve is : '+WebDriverWait(admin_driver, wait_time).until(EC.presence_of_element_located((By.NAME, 'media'))).get_attribute('value'))
        if WebDriverWait(admin_driver, wait_time).until(EC.presence_of_element_located((By.NAME, 'media')))\
                .get_attribute('value') == '1':
            PrintText(' Backup/Restore  - step - *PASS*')
        else:
            PrintText(' Backup/Restore  - step - *FAIL*')
            exit(' Backup/Restore  - step - *FAIL*')


def UploadFile(driver, wait_time, object_recognizer_type, object_recognizer, file_path):
    if object_recognizer_type == 'XPATH':
        upload = WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, object_recognizer)))
        upload.send_keys(file_path)

def PoliciesConfig(browser_type, chrome_driver_path,shield_status ,
                   headless_mode, proxy_address,wait_time, admin_address, **kwargs):

    # Start Driver
    admin_driver = StartBrowser(browser_type, chrome_driver_path, shield_status, headless_mode, proxy_address)
    # Admin Login
    AdminLogin(admin_driver, wait_time, admin_address)
    # Go to Policies Page
    # Go to Policies page
    PressOnObject(admin_driver, wait_time, 'XPATH', '//*[@id="el_1"]/a/span')
    # Edit Default - All Domain
    PressOnObject(admin_driver, wait_time, 'XPATH',
                            '//*[@id="policies-grid"]/vaadin-grid-cell-content[69]/vaadin-checkbox')
    PressOnObject(admin_driver,wait_time, 'XPATH',
                            '//*[@id="content"]/div/div/div[1]/div/div[1]/ul/li[2]/i')

    print(kwargs)
    for key, value in kwargs.items():

        SelectOptionFromList(admin_driver, wait_time, 'NAME', key, value)
        print('Key = {}, Value = {}'.format(key,value))
        time.sleep(2)
    PressOnObject(admin_driver, wait_time, 'XPATH',
                            '//*[@id="middle"]/div[2]/cc-modal/div/div/div/div[3]/table/tbody/tr/td[2]/div/button[1]')
    time.sleep(3)
    admin_driver.quit()