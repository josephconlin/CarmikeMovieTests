__author__ = 'Joseph Conlin'
"""
Page Object for Carmike.com theater detail page
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
import Settings


class MovieDetail:
    # Class to define details about a movie being shown at a specific theater
    def __init__(self, theaterMovieListContainer, driver):
        self._movieNameContainer = theaterMovieListContainer.find_elements_by_tag_name(
            "td")[1].find_elements_by_tag_name("div")[1]
        self._movieShowTimeElements = theaterMovieListContainer.find_elements_by_tag_name(
            "td")[2].find_elements_by_tag_name("a")

        self.movieName = self._movieNameContainer.text

        # movieImageURL is obtained from a modal so click to open, get URL, then click to close
        self._movieNameContainer.click()
        # Wait for the modal to open before continuing
        time.sleep(1)
        WebDriverWait(driver, Settings.seleniumWaitTime).until(
             EC.presence_of_element_located((By.ID, "PosterPanel")))
        self.movieImageURL = driver.find_element_by_id("PosterPanel").find_element_by_tag_name(
            "img").get_attribute("src")
        WebDriverWait(driver, Settings.seleniumWaitTime).until(
             EC.presence_of_element_located((By.ID, "movieModalCloseButton")))
        driver.find_element_by_id("movieModalCloseButton").click()
        # Wait for modal to close before continuing
        time.sleep(1)

        self.movieShowTimeList = self.get_movie_show_times()

    def get_movie_show_times(self):
        """Return a list of strings of the format (h)h:mm, ie 7:00"""
        showTimeList = []
        for showTime in self._movieShowTimeElements:
            showTimeList.append(showTime.text)
        return showTimeList


class TheaterDetail:
    # Class to define elements of the theater detail page
    def __init__(self, driver, index=0):
        self.driver = driver
        self._theaterMoviesListContainer = driver.find_elements_by_class_name("showTimeRowContainer")[index]
        self.theaterName = driver.find_element_by_class_name("showTimeSchedule").find_elements_by_class_name(
            "showTimeTheaterName")[index].text
        self.theaterMoviesList = self.get_movies_list()

    def get_movies_list(self):
        movieList = []
        movies = self._theaterMoviesListContainer.find_elements_by_tag_name("tr")
        for movie in movies:
            movieList.append(MovieDetail(movie, self.driver))
        return movieList


class TheaterCalendar:
    # Class to define elements of the calendar item on the theater detail page.
    def __init__(self, driver):
        self.driver = driver
        self._theaterCalendarOptions = driver.find_element_by_id("MainContent_DateDDL"
                                                                 ).find_elements_by_tag_name("option")
        self._theaterCalendarSelect = Select(driver.find_element_by_id("MainContent_DateDDL"))
        self.selectedDate = self._theaterCalendarSelect.first_selected_option.text

    def wait_for_page_reload(self):
        # Sometimes need to wait for the page reload to complete.  First wait for old objects to become stale
        WebDriverWait(self.driver, Settings.seleniumWaitTime).until(
                      EC.staleness_of(self._theaterCalendarOptions[0]))
        # Now wait for new page object to load. NOTE: This is a duplicate of the _theaterCalendarSelect find statement
        WebDriverWait(self.driver, Settings.seleniumWaitTime).until(
                      EC.visibility_of(self.driver.find_element_by_id("MainContent_DateDDL")))

    """Using any of these click functions will cause a section of the TheaterDetail page to be changed.
       You will need new objects from this file to represent the new HTML page as the driver will have changed.
       Wait after the click so that the new page doesn't accidentally grab the old data elements
    """
    def click_today(self):
        self._theaterCalendarOptions[0].click()
        self.wait_for_page_reload()

    def click_date_by_index(self, i):
        self._theaterCalendarOptions[i].click()
        self.wait_for_page_reload()
