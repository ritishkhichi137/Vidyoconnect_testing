import pandas as pd
from datetime import datetime
import traceback
from tests.p2p_test import P2PTest
from config.config import EXCEL_CONFIG

class TestRunner:
    def __init__(self, debug=False):
        self.debug = debug
        self.results_df = pd.DataFrame(columns=EXCEL_CONFIG['headers'])
        
    def log_results(self, results):
        for browser, result in results.items():
            row = {
                'Browser': browser,
                'Version': result.get('browser_version', 'Unknown'),
                'Status': result.get('status', 'FAIL'),
                'Join Time (seconds)': f"{result.get('join_time', 0)} seconds",
                'Audio Status': result.get('audio_status', 'FAIL'),
                'Video Status': result.get('video_status', 'FAIL'),
                'Network Quality': result.get('network_quality', 'UNKNOWN'),
                'Participants Detected': result.get('participant_count', 0),
                'Test Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'Error Message': result.get('error', '')
            }
            
            # Create a DataFrame from the row and exclude empty or all-NA entries
            row_df = pd.DataFrame([row]).dropna(how='all')
            
            # Concatenate the DataFrame
            self.results_df = pd.concat([self.results_df, row_df], ignore_index=True)
        
        self.results_df.to_excel(EXCEL_CONFIG['filename'], index=False)
    def run_tests(self, demo_mode=False):
        try:
            p2p_test = P2PTest(debug=self.debug)
            results = p2p_test.run_parallel_tests(demo_mode)
            self.log_results(results)
            
            print("\n=== Test Results Summary ===")
            for browser, result in results.items():
                print(f"\n{browser.upper()}:")
                for key, value in result.items():
                    if key == 'join_time':
                        print(f"  {key}: {value} seconds")
                    elif key not in ['network_metrics', 'audio_metrics', 'video_metrics']:
                        print(f"  {key}: {value}")
            
            return results
            
        except Exception as e:
            print(f"Test execution failed: {e}")
            if self.debug:
                traceback.print_
if __name__ == "__main__":
    runner = TestRunner(debug=True)
    runner.run_tests(demo_mode=False)