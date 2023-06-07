from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
from django.test import LiveServerTestCase

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element('id', 'id_list_table')
                rows = table.find_elements('tag name', 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_start_list_and_retreive_later(self):
        # To checkout homepage
        self.browser.get(self.live_server_url)

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
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # Use textbox to add another to-do "Use peacock feathers to make a fly"
        input_box = self.browser.find_element("id", 'id_new_item')
        input_box.send_keys('Use peacock feathers to make a fly')
        input_box.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Page updates and shows both the items on the list

        # Unique url is generated for the user and there is an explanatory text to that effect

        # Visiting the unique url just to see if its still there

        # Goes back to sleep

        self.fail('Finish the test!')
