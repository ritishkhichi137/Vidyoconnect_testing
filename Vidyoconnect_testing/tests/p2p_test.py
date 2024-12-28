import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from core.vidyo_browser_open_close import VidyoConnect
from core.participant_count import ParticipantCounter
from core.media_checker import MediaChecker
from config.config import MEETING_CONFIG, BROWSER_TYPES, EXCEL_CONFIG

class P2PTest:
    def __init__(self, debug=False):
        self.debug = debug
        
    def log(self, message):
        if self.debug:
            print(f"[DEBUG] {message}")

    def run_browser_test(self, browser_type, demo_mode=False):
        vidyo = VidyoConnect(demo_mode=demo_mode)
        try:
            start_time = datetime.now()
            
            # Initialize and join meeting
            vidyo.initialize_browser(browser_type)
            vidyo.join_meeting(
                MEETING_CONFIG['url'],
                f"{MEETING_CONFIG['base_username']}_{browser_type}"
            )
            
            # Collect metrics
            join_time = (datetime.now() - start_time).total_seconds()
            media_status = MediaChecker.check_media_status(vidyo.driver)
            network_quality = MediaChecker.check_network_quality(vidyo.driver)
            participant_count = ParticipantCounter.count_participants(vidyo.driver)
            
            time.sleep(MEETING_CONFIG['test_duration_seconds'])
            
            results = {
                'status': 'PASS',
                'browser_version': vidyo.driver.capabilities['browserVersion'],
                'join_time': round(join_time, 2),
                'audio_status': media_status['audio']['status'],
                'video_status': media_status['video']['status'],
                'network_quality': network_quality['status'],
                'participant_count': participant_count['count'],
                'network_metrics': network_quality['metrics'],
                'audio_metrics': media_status['audio'],
                'video_metrics': media_status['video']
            }
            
            vidyo.end_meeting()
            return results
            
        except Exception as e:
            self.log(f"Error in browser test {browser_type}: {str(e)}")
            return {
                'status': 'FAIL',
                'error': str(e),
                'browser_type': browser_type
            }
        finally:
            vidyo.quit()

    def run_parallel_tests(self, demo_mode=False):
        with ThreadPoolExecutor(max_workers=len(BROWSER_TYPES)) as executor:
            future_to_browser = {
                executor.submit(self.run_browser_test, browser, demo_mode): browser 
                for browser in BROWSER_TYPES
            }
            
            results = {}
            for future in future_to_browser:
                browser = future_to_browser[future]
                try:
                    results[browser] = future.result()
                except Exception as e:
                    self.log(f"Error in parallel test execution for {browser}: {str(e)}")
                    results[browser] = {
                        'status': 'FAIL',
                        'error': str(e),
                        'browser_type': browser
                    }
                    
            return results