from utils.wait_handler import WaitHandler
from utils.vidyo_all_Xpaths import VIDYO_XPATHS
from selenium.webdriver.support.ui import WebDriverWait

class MediaChecker:
    @staticmethod
    def check_media_status(driver):
        try:
            # Check if audio is enabled using JavaScript
            audio_enabled = driver.execute_script("""
                return navigator.mediaDevices.getUserMedia({audio: true})
                    .then(() => true)
                    .catch(() => false);
            """)
            
            # Check if video is enabled using JavaScript
            video_enabled = driver.execute_script("""
                return navigator.mediaDevices.getUserMedia({video: true})
                    .then(() => true)
                    .catch(() => false);
            """)
            
            # Check UI elements for mic and camera status
            mic_button = WaitHandler.wait_for_element(driver, VIDYO_XPATHS['mic_toggle'])
            camera_button = WaitHandler.wait_for_element(driver, VIDYO_XPATHS['camera_toggle'])
            
            mic_ui_enabled = 'muted' not in mic_button.get_attribute('aria-label').lower()
            camera_ui_enabled = 'disabled' not in camera_button.get_attribute('aria-label').lower()
            
            audio_status = "PASS" if audio_enabled and mic_ui_enabled else "FAIL"
            video_status = "PASS" if video_enabled and camera_ui_enabled else "FAIL"
            
            return {
                'audio': {
                    'status': audio_status,
                    'device_detected': audio_enabled
                },
                'video': {
                    'status': video_status,
                    'device_detected': video_enabled
                }
            }
            
        except Exception as e:
            print(f"Error checking media status: {e}")
            return {
                'audio': {'status': "FAIL", 'device_detected': False},
                'video': {'status': "FAIL", 'device_detected': False}
            }

    @staticmethod
    def check_network_quality(driver):
        """Enhanced network quality check"""
        try:
            network_script = """
                return {
                    rtt: performance.now(),
                    downlink: navigator.connection ? navigator.connection.downlink : 'unknown',
                    effectiveType: navigator.connection ? navigator.connection.effectiveType : 'unknown'
                };
            """
            
            network_stats = driver.execute_script(network_script)
            quality_score = 100
            
            if network_stats['rtt'] > 200:
                quality_score -= 20
            if network_stats['downlink'] < 1:
                quality_score -= 20
            if network_stats['effectiveType'] not in ['4g', '5g']:
                quality_score -= 15
                
            return {
                'quality_score': max(0, quality_score),
                'status': "EXCELLENT" if quality_score > 90 else
                         "GOOD" if quality_score > 70 else
                         "FAIR" if quality_score > 50 else
                         "POOR",
                'metrics': network_stats
            }
            
        except Exception as e:
            print(f"Error checking network quality: {e}")
            return {
                'quality_score': 0,
                'status': "UNKNOWN",
                'metrics': {}
            }