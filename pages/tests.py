from django.http import response
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.

class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_hompage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')
    
    def test_homepage_contains_correct_html(self): # new
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self): # new
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

