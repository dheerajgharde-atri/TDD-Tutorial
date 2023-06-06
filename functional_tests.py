from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element('tag name', 'h1').text
        self.assertIn('To-Do', header_text)

        # Entering a to-do item
        input_box = self.browser.find_element("id", 'id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')

        # Enter "buy-peacock-feathers" in text box
        input_box.send_keys('Buy peacock feathers')

        # On hitting enter, the page updates, and the page lists "1: Buy peacock feathers" as an item in a to-do list
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element('id', 'id_list_table')
        rows = table.find_elements('tag name', 'tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        # Use textbox to add another to-do "Use peacock feathers to make a fly"
        self.assertIn('2: Use peacock feathers to make a fly', [row.text for row in rows])

        # Page updates and shows both the items on the list

        # Unique url is generated for the user and there is an explanatory text to that effect

        # Visiting the unique url just to see if its still there

        # Goes back to sleep

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()