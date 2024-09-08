# Guides
1. **Set up Python environment:**
   - Create a virtual environment.
   - Install Playwright and Allure Pytest using pip.
   - Install Allure Command Line.

2. **Initialize Playwright:**
   - Install necessary browser binaries.

3. **Write test cases:**
   - Use Playwright's API to create and run browser tests.
   - Configure Allure to generate test reports.

4. **Run tests and generate reports:**
   - Use pytest to run tests.
   - Use Allure to generate and view reports. 

5. **Test Runner Command Line**
   - Test Runner Config
   - Implementation Example


## 1. Setting Up Your Environment

### Install Python
Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).

### Create a Virtual Environment
It's good practice to use a virtual environment for your project.

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Playwright
You can install Playwright using pip.

```bash
pip install playwright
```

### Install Package requirements
Install defined requirements on the current repository 

```bash
pip install -r requirements.txt
```

### Install Allure Command Line
Follow the instructions to install Allure Command Line from [the official Allure website](https://docs.qameta.io/allure/#_get_started).

For example, on macOS using Homebrew:

```bash
brew install allure
```

On Windows, download the binary from the [official site](https://docs.qameta.io/allure/#_get_started) and add it to your PATH.

## 2. Initialize Playwright

You need to install the necessary browser binaries.

```bash
python -m playwright install
```

## 3. Write Your First Test

Create a new directory for your tests, e.g., `tests`. Inside this directory, create a file called `test_example.py` with the following content:

```python
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture()
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

def test_example(browser):
    page = browser.new_page()
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
```

## 4. Run Your Tests

Run your tests using pytest. This will generate the results for Allure.

```bash
pytest -command-line1 --command-line2 --command-line3
```

### Generate and Open Allure Report

Generate the Allure report using the following command:

```bash
allure serve <directory-name>
```

This will start a local server and open the Allure report in your default web browser.


## 5. Test Runner Command Line
   
### Test Runner Config
- `--headless`: Run tests in headless mode (default: _Non-headless_). 
- `--browser`: Run tests in a different browser chromium, firefox, or webkit. It can be specified multiple times (default: chromium).   
- `--device`: Device to be emulated.  
- `--tracing` Whether to record a trace for each test. on, off, or retain-on-failure (default: off). 
- `--video` Whether to record video for each test. on, off, or retain-on-failure (default: off). 
- `--screenshot` Whether to automatically capture a screenshot after each test. on, off, or only-on-failure (default: off). 
- `--full-page-screenshot` Whether to take a full page screenshot on failure. By default, only the viewport is captured. Requires --screenshot to be enabled (default: off).
- `-n` or `-numproccesses`: The worker to run the tests, requires a number or set as `auto` to run with max device thread
- `--alluredir=<path>`: Store test results in specific directory
- `--reruns=<number>`: Action to retry/retest the failed test, the retest attempts is using the args value
- `--reruns-delay=<number>`: The delay time between test failed completion and retry attempt (numeric format in seconds)


### Implementation:

*Running the test only on specific file*
```bash
pytest tests/test_example.py
```

*Running the test on multiple files*
```bash
pytest tests/test_example.py tests/test_search_filter_menu.py
```

*Running the test on directory*
```bash
pytest tests
```

*Running the test on repository*
```bash
pytest 
```

*Running the test using headless mode*
```bash
pytest --headless
```

*Running the test using headless mode and extract the reports under `reports` folder*
```bash
pytest --headless --alluredir=reports
```

*Running the test on headless mode using as much as possible worker, with 2x retry attempts with 3seconds delay, then extract the report*
```bash
pytest --headless -n=auto --reruns=2 --reruns-delay=3 --alluredir=reports 
```

*Running the test on headless mode using as much as possible worker, with 2x retry attempts with 3seconds delay, with attachment captured avery test session cleared, then extract the report*
```bash
pytest --headless -n=auto --reruns=2 --reruns-delay=3 --screenshot=on --alluredir=reports 
```
**Running the tests on firefox headless and only capture the attachment when the test is failed*
```bash
pytest --headless --browser=firefox --video=retain-on-failure --screenshot=only-on-failure --full-page-screenshot=on
```

