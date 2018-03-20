from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edith heard about new online app
        #And go check the web site
        self.browser.get('http://localhost:8000/')
        
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finishes the test')


#browser = webdriver.Chrome()
#browser = webdriver.Firefox()
#browser.get('http://localhost:9000')

#assert 'Django' in browser.title
 
#browser.quit()

if __name__ == '__main__':
    unittest.main()
