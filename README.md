# Automated tests for [pythonanywhere](http://selenium1py.pythonanywhere.com/)
These tests were written for QA automatization course. 

### Required libraries:
```
Faker 
Pytest
Selenium
Pytest-rerunfailures
```
Make sure that your enviroment contains these libraries or tests will fail
**For installing required libraries use command in new virtual enviroment:**
```
pip install -r requirements.txt
```

## USAGE
Test can be run with following parameters:
- browser, run tests in chosen browser. 
Supported values: chrome, firefox. Default: chrome 
- language, run tests in chosen language.
**NOTE**: Default language: en
Tests will only pass on EN language, **other languages do not supported**
```
pytest -v --tb=line test_items.py --language=en --browser=firefox
```

### Warning
Project contains conftest.py, make sure your folder or subfolder contains another file of that type