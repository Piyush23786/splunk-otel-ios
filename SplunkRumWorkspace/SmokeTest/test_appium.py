import unittest
import os
import sys
from appium import webdriver
from time import sleep
from random import choice, randint
from datetime import datetime
import Constant

class HybridIOSTests(unittest.TestCase):

    # set up appium
    def setUp(self):
        currentDate = datetime.now().strftime('%Y-%m-%d')
        currentTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        caps = {}
        
        caps['platformName'] = 'iOS'
        caps['appium:app'] = 'storage:filename=SmokeTest.zip' # The filename of the mobile app
        caps['appium:deviceName'] = sys.argv[2]
        caps['appium:platformVersion'] = sys.argv[1]
        caps['sauce:options'] = {}
        caps['sauce:options']['appiumVersion'] = '1.22.3'
        caps['sauce:options']['build'] = 'Platform Configurator Build ' + currentDate
        caps['sauce:options']['name'] = 'Platform Configurator Job ' + currentTime
        
        url = 'https://sso-splunk.saucelabs.com-mahimag:274c9a94-86d1-4b12-9594-57307cfb2c57@ondemand.us-west-1.saucelabs.com:443/wd/hub'
        self.driver=webdriver.Remote(url,caps)
    

    def tearDown(self):
        sleep(1)
        self.driver.quit()

    #Loads every element in the current view.
    def load(self):
        find_next = self.driver.find_element_by_xpath("//*")
        return
            

#     # Validating initializing, app start, and presentation span.
#     def test_SDK_Initialize(self):
#         Constant.sdk_initialize_validation()

#     # URL Session Network POST API call and Network Span validation.
#     def test_API_PostClick(self):
#         self.driver.find_element_by_id("Network Request").click();
#         self.driver.find_element_by_id("URLSession").click();
#         self.driver.find_element_by_id("post").click();
#         Constant.method_post_validation()

#     # URL Session Network GET API call and Network Span validation.
#     def test_API_GetClick(self):
#         self.driver.find_element_by_id("Network Request").click();
#         self.driver.find_element_by_id("URLSession").click();
#         self.driver.find_element_by_id("get").click();
#         Constant.method_get_validation()
        
#     # URL Session Network PUT API call and Network Span validation.    
#     def test_API_PutClick(self):
#         self.driver.find_element_by_id("Network Request").click();
#         self.driver.find_element_by_id("URLSession").click();
#         self.driver.find_element_by_id("put").click();
#         Constant.method_put_validation()
        
#     # URL Session Network DELETE API call and Network Span validation.
#     def test_API_DeleteClick(self):
#         self.driver.find_element_by_id("Network Request").click();
#         self.driver.find_element_by_id("URLSession").click();
#         self.driver.find_element_by_id("delete").click();
#         Constant.method_delete_validation()
        
#     # Alamofire Network POST API call and Network Span validation.
#     def test_Alamofire_PostClick(self):
#         self.driver.find_element_by_id("Network Request").click();
#         self.driver.find_element_by_id("Alamofire").click();
#         self.driver.find_element_by_id("post").click();
#         Constant.method_post_validation()
        
#     # Alamofire Network GET API call and Network Span validation.  
#     def test_Alamofire_GetClick(self):
#         self.driver.find_element_by_id("Network Request").click();
#         self.driver.find_element_by_id("Alamofire").click();
#         self.driver.find_element_by_id("get").click();
#         Constant.method_get_validation()
        
#     # Alamofire Network PUT API call and Network Span validation.
#     def test_Alamofire_PutClick(self):
#         self.driver.find_element_by_id("Network Request").click();
#         self.driver.find_element_by_id("Alamofire").click();
#         self.driver.find_element_by_id("put").click();
#         Constant.method_put_validation()
        
#     # Alamofire Network DELETE API call and Network Span validation.   
#     def test_Alamofire_DeleteClick(self):
#         self.driver.find_element_by_id("Network Request").click();
#         self.driver.find_element_by_id("Alamofire").click();
#         self.driver.find_element_by_id("delete").click();
#         Constant.method_delete_validation()
        
#     # AFNetworking Network POST API call and Network Span validation. 
#     def test_AFNetworking_PostClick(self):
#         self.driver.find_element_by_id("Network Request").click();
#         self.driver.find_element_by_id("AFNetworking").click();
#         self.driver.find_element_by_id("post").click();
#         Constant.method_post_validation()
        
#     # AFNetworking Network GET API call and Network Span validation.   
#     def test_AFNetworking_GetClick(self):
#         self.driver.find_element_by_id("Network Request").click();
#         self.driver.find_element_by_id("AFNetworking").click();
#         self.driver.find_element_by_id("get").click();
#         Constant.method_get_validation()
        
#     # AFNetworking Network PUT API call and Network Span validation.     
#     def test_AFNetworking_PutClick(self):
#         self.driver.find_element_by_id("Network Request").click();
#         self.driver.find_element_by_id("AFNetworking").click();
#         self.driver.find_element_by_id("put").click();
#         Constant.method_put_validation()

#     # AFNetworking Network DELETE API call and Network Span validation.     
#     def test_AFNetworking_DeleteClick(self):
#         self.driver.find_element_by_id("Network Request").click();
#         self.driver.find_element_by_id("AFNetworking").click();
#         self.driver.find_element_by_id("delete").click();
#         Constant.method_delete_validation()
        
#     # Screen navigation span generation and validation.
#     def test_ScreenTrackClick(self):
#         self.driver.find_element_by_id("Screen-Track").click();
#         self.driver.find_element_by_id("Custom Screen Name").click();
#         Constant.screen_track_validation()
    
#     # Generating crash report on ViewDidload.
      def test_CrashOnViewLoadClick(self):
         self.driver.find_element("Crash","q").click();
         self.driver.find_element("Crash on ViewDidload","q").click();
        
#     # Generating crash report on button click.
#     def test_ForceCrashClick(self):
#         self.driver.find_element_by_id("Crash").click();
#         self.driver.find_element_by_id("Force Crash on button Click").click();
    
#     # Generating webview span.
#     def test_WebViewClick(self):
#         self.driver.find_element_by_id("WKWebView").click();
    

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(HybridIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
