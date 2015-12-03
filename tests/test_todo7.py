#!/usr/local/bin/python


import unittest
from selenium import webdriver
import page


class TodoAddAFewMarkSomeEtc(unittest.TestCase):
    """Open the page, adds two items, destroys o."""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:9090/angular2/")

    def test_todo_add_two_destroy_one(self):
        """
        Opens the TodoMVC Angular2 page, tests the addition of two items
        marks one complete, adds two more, marks the second complete and then
        destroys the first incomplete item.."""

        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches(), "angular2 title doesn't match."

        todo_list = ["Ponder the meaning of cheese.", "Consider better hobbies."]

        main_page.add_todo_item(todo_list)
        main_page.complete_first_item()

        todo_list2 = ["Read a Russian novel.", "Train cat to sing that 'Adele' song."]

        main_page.add_todo_item(todo_list2)
        assert main_page.count_of_incomplete_items() == 3, "Incomplete items should number 3. They don't."
        main_page.complete_first_item()
        assert main_page.get_todo_count() == "2 items left", "App's reported Item count doesn't match"
        assert main_page.count_of_complete_and_incomplete() == 4, "Test's reported item count doesn't match."
        main_page.click_first_incomplete()
        main_page.destroy_single_incomplete()
        assert main_page.count_of_incomplete_items() == 1, "Test's reported item count doesn't match."

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
