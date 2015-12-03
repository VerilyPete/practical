from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from locators import MainPageLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    def is_title_matches(self):
        """This'll scream if we're opened the wrong page."""
        return "Angular2" in self.driver.title

    def click_toggle_all(self):
        """Toggles all items to completed"""
        element = self.driver.find_element(*MainPageLocators.TOGGLE_ALL)
        element.click()

    def click_first_incomplete(self):
        """Sets the first incomplete item in the list to complete."""
        element = self.driver.find_element(*MainPageLocators.CLICK_FIRST_INCOMPLETE)
        element.click()

    def click_first_complete(self):
        """Sets the first complete item in the list to incomplete."""
        element = self.driver.find_element(*MainPageLocators.CLICK_FIRST_COMPLETE)
        element.click()

    def get_todo_count(self):
        """This simply reports back the count of not-yet-completed items from the app."""
        element = self.driver.find_element(*MainPageLocators.TODO_COUNT)
        return element.text

    def complete_first_item(self):
        """Marks first incomplete item as completed."""
        element = self.driver.find_element(*MainPageLocators.COMPLETE_FIRST)
        element.click()

    def complete_third_item(self):
        """Marks the third incomplete item as complete."""
        element = self.driver.find_element(*MainPageLocators.COMPLETE_THIRD)

    def count_of_incomplete_items(self):
        """Returns the count of todo items that aren't set to complete"""
        element_list = self.driver.find_elements(*MainPageLocators.INCOMPLETE_ITEMS)
        return len(element_list)

    def sum_of_incomplete_items(self):
        """Returns the count of todo items that aren't set to complete"""
        int_list = []
        element_list = self.driver.find_elements(*MainPageLocators.INCOMPLETE_ITEMS)
        for item in element_list:
            int_list.append(int(item.text))
        return sum(int_list)

    def completed_item_count(self):
        """Returns the count of todo items that have the status of completed."""
        element_list = self.driver.find_elements(*MainPageLocators.COMPLETED_ITEMS)
        return len(element_list)

    def count_of_complete_and_incomplete(self):
        """Returns total number of complete + incomplete items."""
        return self.completed_item_count() + self.count_of_incomplete_items()

    def total_number_selected(self):
        """Returns the count of items that currently have focus."""
        element_list = self.driver.find_elements(*MainPageLocators.TOTAL_SELECTED)
        return len(element_list)

    def add_todo_item(self, todo_item_list):
        """When passed a list via todo_item_list , this adds the list's items to the todo list."""
        element = self.driver.find_element(*MainPageLocators.ADD_TODO_ITEM)
        for todo_item in todo_item_list:
            element.send_keys(todo_item)
            element.send_keys(Keys.RETURN)

    def clear_single_completed_item(self):
        """Deletes single item when invoked with single completed item."""
        element = self.driver.find_element(*MainPageLocators.CLEAR_SINGLE_COMPLETED)
        element.click()

    def clear_all_completed(self):
        """Clears all completed items when invoked"""
        element = self.driver.find_element(*MainPageLocators.CLEAR_ALL_COMPLETED)
        element.click()

    def destroy_single_incomplete(self):
        """Destroys currently selected list item. Requires that an item has focus."""
        element = self.driver.find_element(*MainPageLocators.DESTROY_SINGLE_INCOMPLETE)
        element.click()

    def first_item_text(self):
        """Returns the text of the first item in the list."""
        element = self.driver.find_element(*MainPageLocators.DCLICK1)
        return element.text

    def doubleclick_first_item(self):
        """Double clicks the first uncompleted item in the list."""
        element = self.driver.find_element(*MainPageLocators.DCLICK1)
        ActionChains(self.driver).double_click(on_element=element).perform()

    def doubleclick_first_item_with_text(self):
        """Double clicks the first uncompleted item in the list and attempts to enter text."""
        element = self.driver.find_element(*MainPageLocators.DCLICK1)
        ActionChains(self.driver).double_click(on_element=element).send_keys("QWERTY").perform()

    def doubleclick_second_item(self):
        """Double clicks second uncompleted item in the list."""
        element = self.driver.find_element(*MainPageLocators.DCLICK2)
        ActionChains(self.driver).double_click(on_element=element).perform()

    def d_click_first_completed(self):
        """Double-clicks first completed item in list"""
        element = self.driver.find_element(*MainPageLocators.CCLICK1)
        ActionChains(self.driver).double_click(on_element=element).perform()

    def d_click_second_completed(self):
        """Double-clicks second completed item in list."""
        element = self.driver.find_element(*MainPageLocators.CCLICK2)
        ActionChains(self.driver).double_click(on_element=element).perform()
