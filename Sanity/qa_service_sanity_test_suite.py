import unittest, HtmlTestRunner
from qa_service_sanity_test_class import sanity # Call to Module and imports the class

#Test # 1
Test = unittest.TestLoader().loadTestsFromTestCase(sanity) #Loads tests from AlertsPageSanity (test_AlertsSanity will be loaded)

test_suite = unittest.TestSuite([Test])
# runner = HtmlTestRunner.HTMLTestRunner(output='QA Service Sanity')# Define new parameters variable

runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, output='QA Service Sanity',
                                                       report_name='QA Service Sanity',
                                                       add_timestamp=True,
                                                       report_title='QA Service Sanity Report')

runner.run(test_suite) # Run test suite with parameters variable



