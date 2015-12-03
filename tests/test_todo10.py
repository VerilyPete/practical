#!/usr/local/bin/python
# -*- coding: utf-8 -*-


import unittest
from selenium import webdriver
import page


class TestUTF8(unittest.TestCase):
    """Open the page, add a list of alternating duplicate items."""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:9090/angular2/")

    def test_add_and_remove_12x(self):
        """
        Opens the TodoMVC Angular2 page, creates a UTF8 todo list item.."""

        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches(), "angular2 title doesn't match."

        todo_list = [u'idzie wąż wąską dróżką']

        main_page.add_todo_item(todo_list)

        assert main_page.count_of_complete_and_incomplete() == 1

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
