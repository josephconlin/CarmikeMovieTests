__author__ = 'Joseph Conlin'
"""
Tests for page objects
"""
from TestBrowser import TestBrowser
from HeaderPage import Header
from TheatersPage import Theaters
import TheaterDetailPage
# from FileInput import ReadExcel

import unittest
from selenium.common.exceptions import NoSuchElementException
from random import randint

# Setup some common test variables
_headerSearchText = "Provo, UT"
_headerSearchTextNoSpaces = "ABC123"


class HeaderTests(unittest.TestCase):
    def setUp(self):
        self.driver = TestBrowser().get_browser()
        self.header = Header(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_search(self):
        currentPage = self.driver.current_url
        self.header.do_search(_headerSearchTextNoSpaces)
        newPage = self.driver.current_url
        self.assertNotEqual(currentPage, newPage, "Searching did not navigate to a new page")
        # self.assertIn(_headerSearchTextNoSpaces, newPage, "Search text not found in search URL string")

    # def test_search_random_input_from_excel(self):
    #     # Get a random row greater than 0 to avoid the header and get that search data from the default input file
    #     # Within each row of data in the input file, [0] is the search string, [1] is the theater name, [2] is zip code
    #     index = randint(1,6)
    #     input = ReadExcel.get_sheet_values()
    #
    #     searchText = input[index][0]
    #     expectedZip = str(input[index][2])
    #     currentPage = self.driver.current_url
    #     self.header.do_search(searchText)
    #     newPage = self.driver.current_url
    #     self.assertNotEqual(currentPage, newPage, "Searching did not navigate to a new page")
    #     self.assertIn(expectedZip, self.driver.page_source, "Expected zip code not found in results page")


class TheatersTests(unittest.TestCase):
    def setUp(self):
        self.driver = TestBrowser().get_browser()
        # For internal testing purposes, navigate to the theater search results page
        self.header = Header(self.driver)
        self.header.do_search(_headerSearchText)
        self.theaters = Theaters(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_theaters_list(self):
        self.assertNotEqual(0, len(self.theaters.theatersList), "Did not create theaters list")
        self.assertNotEqual(0, len(self.theaters.theatersList[0]), "Did not get a valid list of theaters")

    # def test_search_random_input_from_excel(self):
    #     # Get a random row greater than 0 to avoid the header and get that search data from the default input file
    #     # Within each row of data in the input file, [0] is the search string, [1] is the theater name, [2] is zip code
    #     index = randint(1,6)
    #     input = ReadExcel.get_sheet_values()
    #
    #     searchText = input[index][0]
    #     theaterText = input[index][1]
    #
    #     if(_headerSearchText != searchText):
    #         # Setup did a different search than we want - redo the search and update the variables
    #         self.header = Header(self.driver)
    #         self.header.do_search(searchText)
    #         self.theaters = Theaters(self.driver)
    #
    #     currentPage = self.driver.current_url
    #     self.theaters.click_theater(theaterText)
    #     newPage = self.driver.current_url
    #     theaterName = TheaterDetailPage.TheaterDetail(self.driver).theaterName
    #     self.assertNotEqual(currentPage, newPage, "Selecting a theater did not navigate to a new page")
    #     self.assertIn(theaterText.lower(), theaterName.lower(),
    #                   "Did not end up on theater detail page for selected theater")


class TheaterDetailTests(unittest.TestCase):
    def setUp(self):
        self.driver = TestBrowser().get_browser()
        # For internal testing purposes, navigate to a theater details page
        self.header = Header(self.driver)
        self.header.do_search(_headerSearchText)
        self.theaters = Theaters(self.driver)
        # self.theaters.click_theater(_theaterLinkText)
        self.theater = TheaterDetailPage.TheaterDetail(self.driver)
        self.theaterCalendar = TheaterDetailPage.TheaterCalendar(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_change_days(self):
        currentSelectDate = self.theaterCalendar.selectedDate
        self.theaterCalendar.click_date_by_index(2)
        newTheaterCalendar = TheaterDetailPage.TheaterCalendar(self.driver)
        newSelectDate = newTheaterCalendar.selectedDate
        self.assertNotEqual(currentSelectDate, newSelectDate,
                            "Selecting a different day did not navigate to a new page")

    def test_movies_list_different_days(self):
        currentMovieList = self.theater.theaterMoviesList
        currentSelectDate = self.theaterCalendar.selectedDate
        self.theaterCalendar.click_date_by_index(1)
        newTheater = TheaterDetailPage.TheaterDetail(self.driver)
        newMovieList = newTheater.theaterMoviesList
        newTheaterCalendar = TheaterDetailPage.TheaterCalendar(self.driver)
        newSelectDate = newTheaterCalendar.selectedDate
        self.assertNotEqual(currentSelectDate+currentMovieList[0].movieShowTimeList[0],
                            newSelectDate+newMovieList[0].movieShowTimeList[0],
                            "Movie date and time from today matches movie date and time from tomorrow")


if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(HeaderTests)
    testsToRun = [
        HeaderTests,
        TheatersTests,
        TheaterDetailTests,
    ]
    suite = unittest.TestSuite([unittest.TestLoader().loadTestsFromTestCase(test) for test in testsToRun])
    unittest.TextTestRunner(verbosity=2).run(suite)
