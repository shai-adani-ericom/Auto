#Shai Adani
#29/2/2020
#https://pysource.com/2018/07/19/check-if-two-images-are-equal-with-opencv-and-python/

fwegfwsdd sdgsdvsd

##############################################################
# import relevant modules
from selenium import webdriver
import cv2
from selenium.webdriver.common.keys import Keys
import time, unittest, HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import Environment,POMSimpleForm, Functions




class ShowMessageGetSUM(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        Functions.WriteToLog(cls,POMSimpleForm.test_log_file, ' - Test '+POMSimpleForm.class_name +' started - step PASS')
        Functions.WriteToLog(cls, Environment.results_log_file, ' --- Test '+POMSimpleForm.class_name +' started ---')
        option = Options()
        if Environment.proxyState == 1:
            option.add_argument('--proxy-server=%s' % Environment.proxy)
        cls.driver = webdriver.Chrome(options=option,
                                  executable_path=Environment.chrome_driver_path)  # Start chrome with the option. chrome will not pop up message
        cls.driver.get(POMSimpleForm.url)  # open browser with specific site
        cls.driver.maximize_window()  # maximize window
        time.sleep(10)
        cls.driver.switch_to.frame(POMSimpleForm.frame_by_id)  # switch to required frame name
        time.sleep(5)


    def test_a_ShowMessage(self):
        print('Tested link = ' + POMSimpleForm.url)
        # Starting ShowMessage Test
        Functions.WriteToLog(self, POMSimpleForm.test_log_file, ' - Test '+POMSimpleForm.test_name_a+' started -')
        # locate Enter Message Field and enter text
        try:
            scrollToElement = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, POMSimpleForm.enter_message_field_by_id)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scrollToElement)
            time.sleep(3)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, POMSimpleForm.enter_message_field_by_id))).send_keys(POMSimpleForm.text_to_enter)
            Functions.WriteToLog(self, POMSimpleForm.test_log_file, ' - "Enter Message" field was located and text was successfully entered - step PASS')
        except:
            Functions.WriteToLog(self, POMSimpleForm.test_log_file, ' - "Enter Message" field was NOT located and text was NOT successfully entered - step FAIL')
            self.fail()

        time.sleep(5)

        # locate Show Message Button and press it
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, POMSimpleForm.show_message_button_by_xpath))).click()
            Functions.WriteToLog(self, POMSimpleForm.test_log_file,
                                 ' - "Show Message" button was located and pressed  - step PASS')
        except:
            Functions.WriteToLog(self, POMSimpleForm.test_log_file,
                                 ' - "Show Message" button was NOT located  - step FAIL')
            self.fail()
        time.sleep(5)

        # locate Your Message area and get text
        try:
            text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, POMSimpleForm.message_display_by_id))).text
            Functions.WriteToLog(self, POMSimpleForm.test_log_file,
                                 ' - Message content located and captured  - step PASS')
        except:
            Functions.WriteToLog(self, POMSimpleForm.test_log_file,
                                 ' - Message content was NOT located and captured  - step FAIL')
            self.fail()

        time.sleep(5)

        # compare captured text with expected result
        if text == POMSimpleForm.text_to_enter:
            Functions.WriteToLog(self, POMSimpleForm.test_log_file,
                                 ' - Expected text appears  - TEST PASS**')
            Functions.WriteToLog(self, Environment.results_log_file, ' --- Test '+POMSimpleForm.test_name_a+' PASS** ---')
        else:
            Functions.WriteToLog(self, POMSimpleForm.test_log_file,
                                 ' - Expected text does not appear or   - TEST FAIL***')
            Functions.WriteToLog(self, POMSimpleForm.test_log_file,
                                 ' - Expected text was {} while actual text is {}   - TEST FAIL***'.format(POMSimpleForm.text_to_enter,text))
            Functions.WriteToLog(self, Environment.results_log_file, ' - Expected text does not appear or   - TEST FAIL***')
            Functions.WriteToLog(self, Environment.results_log_file,
                                 ' - Expected text was {} while actual text is {}   - TEST FAIL***'.format(POMSimpleForm.text_to_enter,text))

            self.fail()

        time.sleep(3)
        self.driver.get_screenshot_as_file('TestResults' + '/' + POMSimpleForm.class_name + 'Message.png')
        time.sleep(3)
        Functions.WriteToLog(self, POMSimpleForm.test_log_file, ' - Test '+POMSimpleForm.test_name_a+' ended -')
        time.sleep(3)

    def test_b_GetSUM(self):
        print('Tested link = ' + POMSimpleForm.url)
        # Starting GetSum Test
        # locate Enter a field
        try:
            Functions.WriteToLog(self, POMSimpleForm.test_log_file, ' - Test '+POMSimpleForm.test_name_b+' started -')
            scrollToElement = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, POMSimpleForm.num1_by_id)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scrollToElement)
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, POMSimpleForm.num1_by_id))).send_keys(POMSimpleForm.number1)
            Functions.WriteToLog(self, POMSimpleForm.test_log_file, ' - "Enter a" field was located and number1 was successfully entered - step PASS')
        except:
            Functions.WriteToLog(self, POMSimpleForm.test_log_file, ' - "Enter a" field was NOT located and number1 was NOT successfully entered - step FAIL')
            self.fail()

        time.sleep(3)

        # locate Enter b field
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, POMSimpleForm.num2_by_id))).send_keys(POMSimpleForm.number2)
            Functions.WriteToLog(self, POMSimpleForm.test_log_file,
                                 ' - "Enter b" field was located and number2 was successfully entered - step PASS')
        except:
            Functions.WriteToLog(self, POMSimpleForm.test_log_file,
                                 ' - "Enter b" field was NOT located and number2 was NOT successfully entered - step FAIL')
            self.fail()

        time.sleep(5)
        # locate Get Total Button and press it
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, POMSimpleForm.get_total_button_by_xpath))).click()
            Functions.WriteToLog(self, POMSimpleForm.test_log_file,
                                 ' - "Get Total" button was located and pressed  - step PASS')
        except:
            Functions.WriteToLog(self, POMSimpleForm.test_log_file,
                                 ' - "Get Total" button was NOT located  - step FAIL')
            self.fail()
        time.sleep(5)

        # locate Your Display value and get total
        try:
            total = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, POMSimpleForm.sum_display_value_by_id))).text
            Functions.WriteToLog(self, POMSimpleForm.test_log_file,
                                 ' - Display total located and captured  - step PASS')
        except:
            Functions.WriteToLog(self, POMSimpleForm.test_log_file,
                                 ' - Display total was NOT located and captured  - step FAIL')
            self.fail()

        time.sleep(5)

        # compare captured text with expected result
        if total == POMSimpleForm.total:
            Functions.WriteToLog(self, POMSimpleForm.test_log_file,
                                 ' - Expected total appears  - TEST PASS**')
            Functions.WriteToLog(self, Environment.results_log_file, ' --- Test '+POMSimpleForm.test_name_b+' PASS** ---')

        else:
            Functions.WriteToLog(self, POMSimpleForm.test_log_file,
                                 ' - Expected total does not appear or   - TEST FAIL***')

            Functions.WriteToLog(self, POMSimpleForm.test_log_file,
                                 ' - Expected total was {} while actual text is {}   - TEST FAIL***'.format(POMSimpleForm.total,total))

            Functions.WriteToLog(self, Environment.results_log_file, ' - Expected text does not appear or   - TEST FAIL***')

            Functions.WriteToLog(self, Environment.results_log_file,
                                 ' - Expected text was {} while actual text is {}   - TEST FAIL***'.format(POMSimpleForm.total,total))




            self.fail()

        time.sleep(3)
        self.driver.get_screenshot_as_file('TestResults' + '/' + POMSimpleForm.class_name + 'Sum.png')
        time.sleep(3)
        Functions.WriteToLog(self, POMSimpleForm.test_log_file, ' - Test '+POMSimpleForm.test_name_b+' ended -')

        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        Functions.WriteToLog(cls, POMSimpleForm.test_log_file, ' --- Test '+POMSimpleForm.class_name +' ended ---')
        Functions.WriteToLog(cls, Environment.results_log_file, ' --- Test '+POMSimpleForm.class_name +' ended ---')

        time.sleep(3)
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="TestResults", report_name= POMSimpleForm.class_name, add_timestamp=True,report_title=POMSimpleForm.class_name +'Report'))


