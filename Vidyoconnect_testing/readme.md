# VidyoConnect P2P Testing Framework


## Overview
The VidyoConnect P2P Testing Framework is an automated testing solution designed to facilitate peer-to-peer call testing across multiple browsers. This framework supports parallel execution of tests, verification of media status, participant counting, and generates comprehensive reports in Excel format. It is particularly useful for ensuring the reliability and performance of VidyoConnect in various browser environments.

## Features
- **Multi-Browser Support**: The framework supports testing on both Chrome and Edge browsers, ensuring broad compatibility and coverage.
- **Parallel Test Execution**: Tests can be executed concurrently across multiple browsers, significantly reducing the time required for comprehensive testing.
- **Media Status Verification**: The framework checks the status of audio and video devices to ensure they are functioning correctly during the call.
- **Participant Counting**: It counts the number of participants in the call, providing insights into the call's dynamics.
- **Demo Mode**: A demo mode is available for presentations, allowing for a controlled testing environment.
- **Excel Report Generation**: Detailed test reports are generated in Excel format, making it easy to analyze and share results.


## Installation
1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

2. **Install requirements**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the tests, use the following code:
```python
from tests.test_runner import TestRunner

runner = TestRunner()
results = runner.run_tests(demo_mode=False)
```

## Project Structure
```
Vidyoconnect_testing/
├── config/
│   ├── __init__.py
│   └── config.py
├── core/
│   ├── __init__.py
│   ├── vidyo_browser_open_close.py
│   ├── participant_count.py
│   └── media_checker.py
├── utils/
│   ├── __init__.py
│   ├── wait_handler.py
│   └── vidyo_all_Xpaths.py
├── tests/
│   ├── __init__.py
│   └── p2p_test.py
├── requirements.txt
└── multi_browser_test.py
```

## Configuration
### `config/config.py`
```python
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
```

### Core Modules
#### `core/vidyo_browser_open_close.py`
This module handles the automation of opening and closing VidyoConnect calls. It includes methods to initialize the browser, join a meeting, and end a meeting.

#### `core/participant_count.py`
This module is responsible for counting the number of participants in the call. It uses various strategies to ensure accurate counting, even if the participant elements are dynamically loaded or have different class names.

#### `core/media_checker.py`
This module verifies the status of audio and video devices and checks the network quality. It uses JavaScript to interact with the browser's media devices and network information APIs.

### Utilities
#### `utils/wait_handler.py`
This utility manages wait times for elements to be available. It uses Selenium's WebDriverWait to wait for elements to become clickable or visible.

#### `utils/vidyo_all_Xpaths.py`
This file contains all the necessary XPaths required for the tests. It centralizes the XPaths to make the code more maintainable and easier to update.

### Tests
#### `tests/p2p_test.py`
This module runs parallel tests for multiple browsers using threading. It initializes the browser, joins the meeting, collects metrics, and generates results.

### Running the Tests
#### `multi_browser_test.py`
This script connects all the modules and runs the automation, generating results in the desired Excel file. It serves as the entry point for executing the tests.

## Requirements
See `requirements.txt` for a complete list of dependencies.