#!/usr/local/bin/python


import unittest
from selenium import webdriver
import page


class TodoAdd99Select49Test(unittest.TestCase):
    """Open the page, add some items, check the reported count."""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:9090/angular2/")

    def test_todo_add_99_and_select_49(self):
        """
        Opens the TodoMVC Angular2 page, tests the addition of 99 items
        to the list and then completes only the odd-numbered items, summing the evens
        and asserting if this crude checksum fails."""

        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches(), "angular2 title doesn't match."
        todo_list = [number for number in range(1, 100)]
        main_page.add_todo_item(todo_list)
        for item_count in range(1, int(51), 1):
            checkbox = self.driver.find_element_by_xpath("/html/body/todo-app/section[@class='todoapp']"
                                                         "/section[@class='main']/ul[@class='todo-list']"
                                                         "/li[@class='ng-binding'][" + str(item_count) + "]"
                                                         "/div[@class='view']""/input[@class='toggle ng-binding']")
            checkbox.click()

        assert main_page.get_todo_count() == "49 items left", "Item count doesn't match"
        assert main_page.sum_of_incomplete_items() == 2450

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
