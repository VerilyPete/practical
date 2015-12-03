from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    TOGGLE_ALL = (By.XPATH, "/html/body/todo-app/section[@class='todoapp']"
                            "/section[@class='main']/input[@class='toggle-all ng-binding']")
    TODO_COUNT = (By.CLASS_NAME, "todo-count")
    INCOMPLETE_ITEMS = (By.XPATH, "/html/body/todo-app/section[@class='todoapp']/section[@class='main']"
                                  "/ul[@class='todo-list']/li[@class='ng-binding']/div[@class='view']")
    COMPLETED_ITEMS = (By.XPATH, "/html/body/todo-app/section[@class='todoapp']"
                                 "/section[@class='main']/ul[@class='todo-list']"
                                 "/li[@class='ng-binding completed']/div[@class='view']"
                                 "/label[@class='ng-binding']")
    TOTAL_SELECTED = (By.XPATH, "/html/body/todo-app/section[@class='todoapp']"
                                "/section[@class='main']/ul[@class='todo-list']"
                                "/li[@class='ng-binding editing']/input[@class='edit ng-binding']")
    ADD_TODO_ITEM = (By.CLASS_NAME, "new-todo")
    CLEAR_SINGLE_COMPLETED = (By.XPATH, "/html/body/todo-app/section[@class='todoapp']/section[@class='main']"
                                        "/ul[@class='todo-list']/li[@class='ng-binding completed']"
                                        "/div[@class='view']/button[@class='destroy ng-binding']")
    CLEAR_ALL_COMPLETED = (By.XPATH, "/html/body/todo-app/section[@class='todoapp']/footer[@class='footer']"
                                     "/button[@class='clear-completed ng-binding']")
    DESTROY_SINGLE_INCOMPLETE = (By.XPATH, "/html/body/todo-app/section[@class='todoapp']/section[@class='main']"
                                           "/ul[@class='todo-list']/li[@class='ng-binding']/div[@class='view']"
                                           "/button[@class='destroy ng-binding']")
    DCLICK1 = (By.XPATH, "/html/body/todo-app/section[@class='todoapp']/section[@class='main']"
                         "/ul[@class='todo-list']/li[@class='ng-binding'][1]/div[@class='view']"
                         "/label[@class='ng-binding']")
    DCLICK2 = (By.XPATH, "/html/body/todo-app/section[@class='todoapp']/section[@class='main']"
                         "/ul[@class='todo-list']/li[@class='ng-binding'][2]/div[@class='view']"
                         "/label[@class='ng-binding']")
    CCLICK1 = (By.XPATH, "/html/body/todo-app/section[@class='todoapp']/section[@class='main']/ul[@class='todo-list']"
                         "/li[@class='ng-binding completed'][1]/div[@class='view']/label[@class='ng-binding']")
    CCLICK2 = (By.XPATH, "/html/body/todo-app/section[@class='todoapp']/section[@class='main']/ul[@class='todo-list']"
                         "/li[@class='ng-binding completed'][2]/div[@class='view']/label[@class='ng-binding']")
    COMPLETE_FIRST = (By.XPATH, "/html/body/todo-app/section[@class='todoapp']/section[@class='main']"
                                "/ul[@class='todo-list']/li[@class='ng-binding'][1]/div[@class='view']"
                                "/input[@class='toggle ng-binding']")
    CLICK_FIRST_INCOMPLETE = (By.XPATH, "/html/body/todo-app/section[@class='todoapp']/section[@class='main']"
                                        "/ul[@class='todo-list']/li[@class='ng-binding'][1]/div[@class='view']"
                                        "/label[@class='ng-binding']")
    CLICK_FIRST_COMPLETE = (By.XPATH, "/html/body/todo-app/section[@class='todoapp']/section[@class='main']"
                                      "/ul[@class='todo-list']/li[@class='ng-binding completed'][1]/div[@class='view']"
                                      "/label[@class='ng-binding']")
