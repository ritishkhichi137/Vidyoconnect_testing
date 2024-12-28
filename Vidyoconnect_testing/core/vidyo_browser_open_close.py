from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from utils.wait_handler import WaitHandler
from utils.vidyo_all_Xpaths import VIDYO_XPATHS

class VidyoConnect:
    def __init__(self, demo_mode=False):
        self.demo_mode = demo_mode
        self.driver = None
        
    def initialize_browser(self, browser_type):
        """Initialize specific browser with appropriate options"""
        try:
            if browser_type.lower() == 'chrome':
                options = webdriver.ChromeOptions()
                options.add_argument('--use-fake-ui-for-media-stream')
                options.add_argument('--use-fake-device-for-media-stream')
                options.add_argument('--start-maximized')
                options.add_argument('--disable-gpu')  # Helps prevent GPU errors
                options.add_experimental_option('excludeSwitches', ['enable-logging']) 
                options.add_argument('--enable-unsafe-swiftshader')
                service = ChromeService(ChromeDriverManager().install())
                self.driver = webdriver.Chrome(service=service, options=options)
                
            elif browser_type.lower() == 'edge':
                options = webdriver.EdgeOptions()
                options.use_chromium = True
                options.add_argument('--use-fake-ui-for-media-stream')
                options.add_argument('--use-fake-device-for-media-stream')
                options.add_argument('--start-maximized')
                options.add_argument('--disable-gpu')  # Helps prevent GPU errors
                options.add_argument('--enable-unsafe-swiftshader')
                options.add_experimental_option('excludeSwitches', ['enable-logging']) 
                service = EdgeService(EdgeChromiumDriverManager().install())
                self.driver = webdriver.Edge(service=service, options=options)
            
            else:
                raise ValueError(f"Unsupported browser type: {browser_type}")
            
            return self.driver
            
        except Exception as e:
            print(f"Error initializing {browser_type} browser: {e}")
            raise

    def join_meeting(self, meeting_url, username):
        """Join meeting from specific browser"""
        try:
            # Navigate to meeting
            self.driver.get(meeting_url)
            
            # Enter username
            username_field = WaitHandler.wait_for_element(self.driver, VIDYO_XPATHS['username_field'], demo_mode=self.demo_mode)
            username_field.send_keys(username)
            
            # Join meeting
            join_button = WaitHandler.wait_for_element(self.driver, VIDYO_XPATHS['join_button'], demo_mode=self.demo_mode)
            join_button.click()
            
        except Exception as e:
            print(f"Error joining meeting: {e}")
            raise

    def end_meeting(self):
        """End call for specific browser"""
        try:
            end_call_button = WaitHandler.wait_for_element(self.driver, VIDYO_XPATHS['end_call_button'], demo_mode=self.demo_mode)
            end_call_button.click()
            return True
        except Exception as e:
            print(f"Error ending call: {e}")
            return False

    def quit(self):
        """Quit the browser"""
        if self.driver:
            # Get browser logs before quitting
            try:
                logs = self.driver.get_log('browser')
                print("Browser Logs:")
                for log in logs:
                    print(f"{log['level']}: {log['message']}")
            except:
                pass
                
            self.driver.quit()