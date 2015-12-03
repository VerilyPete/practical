#!/usr/local/bin/python


import unittest
from selenium import webdriver
import page


class TestAddCompleteRemoveRedux(unittest.TestCase):
    """Open the page, add a list of items, mark all complete, remove all, repeat 12x."""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:9090/angular2/")

    def test_add_and_remove_12x(self):
        """
        Opens the TodoMVC Angular2 page, tests the addition of 9 items, marks them complete
        and removes them 12x.t"""

        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches(), "angular2 title doesn't match."

        revcount = 12
        while revcount >= 0:
            todo_list = ["Mow", "Moo", "Mao", "Waffle", "Lamp", "Dog", "Cat", "Airplane", "Squirrel"]
            main_page.add_todo_item(todo_list)
            main_page.click_toggle_all()
            main_page.clear_all_completed()
            revcount -= 1

        assert main_page.count_of_complete_and_incomplete() == 0

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
