#!/usr/local/bin/python


import unittest
from selenium import webdriver
import page


class TodoAdd5000CompleteAllClearAllTest(unittest.TestCase):
    """Open the page, add 5,000 items. This'll take awhile and spin up your laptop's fans."""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:9090/angular2/")

    def test_todo_add_so_many(self):
        """
        Opens the TodoMVC Angular2 page, tests the addition of 5,000 items,
        marks all 5,000 complete and then removes them.."""

        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches(), "angular2 title doesn't match."

        todo_list = [number for number in range(1, 5001)]

        main_page.add_todo_item(todo_list)
        main_page.click_toggle_all()
        main_page.clear_all_completed()
        assert main_page.count_of_complete_and_incomplete() == 0

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
