__author__ = 'Joseph Conlin'
"""
Page Object for Carmike.com theater search results page
"""


class Theaters:
    # Class to define elements of the theater search results page
    def __init__(self, driver):
        self.driver = driver
        self._theaterListContainer = driver.find_element_by_class_name("showTimeSchedule")
        self.theatersList = []
        for theater in self._theaterListContainer.find_elements_by_class_name("showTimeTheaterName"):
            self.theatersList.append(theater.text)
