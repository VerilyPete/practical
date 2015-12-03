#!/usr/local/bin/python


import unittest
from selenium import webdriver
import page


class TodoAddTwoAndDestroyOne(unittest.TestCase):
    """Open the page, adds two items, destroys one."""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:9090/angular2/")

    def test_todo_add_two_destroy_one(self):
        """
        Opens the TodoMVC Angular2 page, tests the addition of two items
        and destroys a single item."""

        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches(), "angular2 title doesn't match."

        todo_list = ["Buy medicine for ferret bites.", "Borrow a ladder to retrieve kite."]

        main_page.add_todo_item(todo_list)
        main_page.click_first_incomplete()
        main_page.destroy_single_incomplete()
        assert main_page.get_todo_count() == "1 item left", "App's reported Item count doesn't match"
        assert main_page.count_of_complete_and_incomplete() == 1, "Test's reported item count doesn't match."

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
