#!/usr/local/bin/python


import unittest
from selenium import webdriver
import page


class TodoAddAndCheckReportedTest(unittest.TestCase):
    """Open the page, add some items, check the reported count."""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:9090/angular2/")

    def test_todo_add_and_count(self):
        """
        Opens the TodoMVC Angular2 page, tests the addition of three items
        and verifies the count reported by todo-count"""

        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches(), "angular2 title doesn't match."

        todo_list = ["Mow the house.", "Walk the lawn.", "Paint the dog."]

        main_page.add_todo_item(todo_list)
        assert main_page.get_todo_count() == "3 items left", "Page's Item count doesn't match"
        assert main_page.count_of_incomplete_items() == 3, "Test's item count doesn't match."

    def tearDown(self):
        self.driver.close()

    
if __name__ == "__main__":
    unittest.main()
