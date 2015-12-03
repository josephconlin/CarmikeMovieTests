# Configuration settings for the tests
# baseURL is the starting page for tests
baseURL = 'http://www.carmike.com/default.aspx'

# browserType tells Selenium which browser we want the tests to be run with
# Use names as described here:
# https://selenium.googlecode.com/svn/trunk/docs/api/py/webdriver/selenium.webdriver.common.desired_capabilities.html
browserType = 'FIREFOX'
# browserType = 'INTERNETEXPLORER'
# browserType = 'CHROME'

# seleniumHubURL tells the tests where to find the Selenium hub
seleniumHubURL = 'http://127.0.0.1:4444/wd/hub'

# seleniumWaitTime tells any explicit waits how long to wait before giving up
seleniumWaitTime = 10
