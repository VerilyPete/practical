#!/usr/local/bin/python


import unittest
from selenium import webdriver
import page


class TodoAddSelectAndClearTest(unittest.TestCase):
    """Open the page, add some items, select two and clear all completed.t."""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:9090/angular2/")

    def test_todo_populate_and_destroy(self):
        """
        Opens the TodoMVC Angular2 page, adds five items, selects two
         and completes all items before removing completed items."""

        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches(), "angular2 title doesn't match."

        todo_list = ["Buy a ferret.", "Learn to speak Cantonese.", "Fly a kite.",
                     "Ride a bicycle to mars", "Clean the garage."]

        main_page.add_todo_item(todo_list)
        main_page.doubleclick_first_item()
        main_page.doubleclick_second_item()
        main_page.click_toggle_all()
        main_page.clear_all_completed()
        assert main_page.count_of_complete_and_incomplete() == 0, "Not all items were removed."

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()