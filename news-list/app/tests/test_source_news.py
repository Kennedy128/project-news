import unittest
from ..models import Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_category = Source("abc-news", "ABC News","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.","https://abcnews.go.com",  "en", "us")


    def test_instance(self):
        self.assertTrue(isinstance(self.new_category,Source))

    def test_correct_source_init(self):
        '''
        Test  that confirms that the object is instantiated correctly.
        '''
        self.assertEqual(self.new_category.id, "abc-news")
        self.assertEqual(self.new_category.name, "ABC News")
        self.assertEqual(self.new_category.description, "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.")
        self.assertEqual(self.new_category.url, "https://abcnews.go.com")
        self.assertEqual(self.new_category.category, "general")
        self.assertEqual(self.new_category.language, "en")
        self.assertEqual(self.new_category.country, "us")



if __name__ == '__main__':
    unittest.main()