from framework.pages.base import BasePage


class MainPage(BasePage):
    """
    MainPage
    """
    URL = 'https://en.wikipedia.org/wiki/Main_Page'
    SEARCH_INPUT = 'searchInput'

    def __init__(self, driver):
        super().__init__(driver)
        self._driver.get(MainPage.URL)

    @property
    def search_input(self):
        return self._driver.find_element_by_id(MainPage.SEARCH_INPUT)

    def search_for(self, search_term):
        self.search_input.send_keys(search_term)
        self.search_input.submit()
