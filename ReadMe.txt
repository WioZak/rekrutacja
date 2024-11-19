In order to run on a local machine (tested on MacOS):
1. Install latest version of python https://www.python.org/
2. Install pip
3. In console, install the Pytest plugin:
    pyhton3 pip install pytest-playwright
4. Install the required browsers:
    playwright install
5. Install plugin for generating reports
    pip install pytest-html
6. In the console, go to AutomatedTests directory. To run all the tests in headed mode, type:
    pytest --headed
and click Enter.

All run options are defined in pytest.ini file
Report can be found in AutomatedTests/report.html file. Example report is in the repository

Test script supports different translations. Since SauceLabs is not translated to Spanish, there will be failed test cases for es_ES locale.

Tests run in Github Actions on macOS instance once every day.
YML file is defined so that we can run a specific suite, in this case test_login, using step:
    pytest AutomatedTests/test_login.py --base-url https://www.saucedemo.com/v1/index.html
