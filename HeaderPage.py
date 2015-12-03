__author__ = 'Joseph Conlin'
"""
Page Object for Carmike.com header items
"""


class Header:
    # Class to define elements of the header
    def __init__(self, driver):
        self.driver = driver
        self.searchText = driver.find_element_by_id("SearchBox")
        self.searchSubmit = driver.find_element_by_id("MasterSearchButton")

    def input_search_string(self, searchString):
        self.searchText.clear()
        self.searchText.send_keys(searchString)

    def do_search(self, searchString=''):
        self.input_search_string(searchString)
        self.searchSubmit.click()
