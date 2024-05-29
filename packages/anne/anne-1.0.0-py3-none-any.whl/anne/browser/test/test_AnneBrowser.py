from ..src.AnneBrowser import AnneBrowser
from selenium import webdriver
import unittest, time


class TestAnneBrowser(unittest.TestCase):

    def setUp(self):
        self.browser = AnneBrowser(webdriver.Chrome(), True)

    def test_run(self):
        self.browser.openUrl('https://www.google.com')
        self.browser.click(element='textarea#APjFqb', locator='css', wait_mode='cotheclick', timeout=30, anti=True)
        self.browser.sendText(element='textarea#APjFqb', locator='css', content='AnneBrowser', wait_mode='cotheclick', timeout=30, anti=True)
        self.browser.sendKeys('enter')
        time.sleep(5)
        self.browser.scroll(bottom=True)
        self.browser.exit()


# if __name__ == '__main__':
#     unittest.main()


# python -m unittest app.browser.test.test_AnneBrowser

























