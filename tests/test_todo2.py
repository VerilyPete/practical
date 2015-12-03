#!/usr/local/bin/python


import unittest
from selenium import webdriver
import page


class TodoAdd99Select2Test(unittest.TestCase):
    """Open the page, add 99 items, select two of them."""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:9090/angular2/")

    def test_todo_add_and_select(self):
        """
        Opens the TodoMVC Angular2 page, tests the addition of 99 items
        and then tests that only a single item is selected."""

        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches(), "angular2 title doesn't match."

        todo_list = [number for number in range(1, 100)]

        main_page.add_todo_item(todo_list)
        assert main_page.get_todo_count() == "99 items left", "Item count doesn't match"
        main_page.doubleclick_first_item()
        main_page.doubleclick_second_item()
        assert main_page.total_number_selected() == 1, "More than one item selected."

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
