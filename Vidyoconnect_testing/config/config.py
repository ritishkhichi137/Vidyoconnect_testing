#settings.py
MEETING_CONFIG = {
    "url": "https://static.platform.vidyo.io/app/vidyoconnect/23.4.2.3423/index.html?roomdirect.html=&roomKey=OGRaoJS1Ll&pin=false&portal=https%3A%2F%2Fenghouse.vidyocloud.com&f=RzpJUENPOklQQ0k6TW9kOlRMUzpQQzpQdWJDOkNEUjpFUDpSUEk6QkE6TkRDOkNQUjpPQToyMjA6UFI6U1IyOlNSOlRQ&sessionToken=fc1b8bb6-26cf-41f2-bee5-9de9ceff4c25",
    "base_username": "P2P_Tester",
    "test_duration_seconds": 15
}

BROWSER_TYPES = ['chrome', 'edge']

EXCEL_CONFIG = {
    "filename": 'p2p_test_results.xlsx',
    "headers": [
        'Browser',
        'Version',
        'Status',
        'Join Time (seconds)',
        'Audio Status',
        'Video Status',
        'Network Quality',
        'Participants Detected',
        'Test Timestamp',
        'Error Message'
    ]
}