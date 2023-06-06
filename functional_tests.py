from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_start_list_and_retreive_later(self):

        # To checkout homepage
        self.browser.get('http://localhost:8000')

        # To-do in the header of the web page
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # Entering a to-do item

        # Enter "buy-peacock-feathers" in text box

        # On hitting enter, the page updates, and the page lists "1: Buy peacock feathers" as an item in a to-do list

        # Use textbox to add another to-do "Use peacock feathers to make a fly"

        # Page updates and shows both the items on the list

        # Unique url is generated for the user and there is an explanatory text to that effect

        # Visiting the unique url just to see if its still there

        # Goes back to sleep

if __name__=='__main__':
    unittest.main()