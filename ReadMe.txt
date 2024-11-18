1. Install latest version of python https://www.python.org/
2. Install pip
3. In console, install the Pytest plugin:
    pyhton3 pip install pytest-playwright
4. Install the required browsers:
    playwright install
5. Install plugin for generating reports
    pip install pytest-html
6. In the console, go to AutomatedTests directory. To run all the tests, type:
    pytest 
and click Enter.

All run options are defined in pytest.ini file
Report can be found in AutomatedTests/report.html file.



Test script supports different locale. Since SauceLabs is not translated to Spanish, there will be failed test cases for es_ES locale.
