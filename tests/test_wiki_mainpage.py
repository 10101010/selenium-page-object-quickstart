from framework.pages.main_page import MainPage


def test_search_on_mainpage(selenium):
    page = MainPage(selenium)
    page.search_for('Software Testing')

    assert 'Software testing' in selenium.title

    from time import sleep; sleep(3)
