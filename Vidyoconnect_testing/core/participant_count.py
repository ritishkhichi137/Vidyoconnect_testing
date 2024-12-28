from selenium.webdriver.common.by import By
from utils.wait_handler import WaitHandler
from utils.vidyo_all_Xpaths import VIDYO_XPATHS

class ParticipantCounter:
    @staticmethod
    def count_participants(driver):
        """Check number of participants in call"""
        try:
            # Wait for participant list to be available
            WaitHandler.wait_for_element(driver, VIDYO_XPATHS['participant_list'])
            
            # Define XPaths for participant elements
            participant_xpath = VIDYO_XPATHS['participant_list']
            alternative_xpath = VIDYO_XPATHS['alternative_participant_list']
            
            try:
                # Try primary XPath
                participants = driver.find_elements(By.XPATH, participant_xpath)
                count = len(participants)
                if count > 0:
                    return {'count': count, 'participants': []}
                
                # Try alternative XPath
                participants = driver.find_elements(By.XPATH, alternative_xpath)
                return {'count': len(participants), 'participants': []}
                
            except Exception:
                # Fallback to JavaScript execution
                participant_count = driver.execute_script("""
                    const participantElements = document.querySelectorAll(
                        '.participants-panel .participant-item, ' +
                        '.participantsList .participant, ' +
                        '[class*="participant"]'
                    );
                    return participantElements.length;
                """)
                
                if participant_count > 0:
                    return {'count': participant_count, 'participants': []}
                
                # Last resort: try to find any element that might represent a participant
                all_possible_participants = driver.find_elements(
                    By.XPATH,
                    "//*[contains(@class, 'participant') or contains(@class, 'user')]"
                )
                return {'count': len(all_possible_participants), 'participants': []}
                
        except Exception as e:
            print(f"Error counting participants: {e}")
            return {'count': 0, 'participants': []}