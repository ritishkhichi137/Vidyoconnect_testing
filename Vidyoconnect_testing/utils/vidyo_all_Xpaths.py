VIDYO_XPATHS = {
    'join_button': '//*[@id="gustJoinButton"]',
    'username_field': '//*[@id="guest_name"]',
    'mic_toggle': '//*[@id="root"]/div/div/div[3]/div[2]/div[1]/div[2]/span[1]/button',
    'camera_toggle': '//*[@id="root"]/div/div/div[3]/div[2]/div[2]/div/span[1]/button',
    'end_call_button': '//*[@id="root"]/div/div/div[3]/div[1]/span/button',
    'participant_list': '//*[@id="root"]/div/div/div[1]/span/div',
    'chat_input': '//*[@id="chat-inpit-id"]',
    'meeting_loaded': '//*[@id="root"]/div/div/div[1]/div[3]/div[2]',
    'participant_list': '//*[@id="root"]/div/div/div[1]/div[1]',  # Primary participant list XPath
    'alternative_participant_list': "//div[contains(@class, 'participantsList')]//div[contains(@class, 'participant')]" # Alternative participant list XPath
}