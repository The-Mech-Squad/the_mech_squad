from django.test import TestCase
from django.test import Client

class TestHomepage(TestCase):
    def setUp(self):
        client = Client()

    def test_homepage_can_render_showcase_html(self):
        response = self.client.get("//")

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "homepage.html")

    def test_hal_html_can_render(self):
        response = self.client.get("/hal/")

        self.assertEqual(response.status_code, 200)
        
        self.assertTemplateUsed(response, "hal.html")

# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from selenium import webdriver
#
# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')

# assert 'Space Trash' in browser.title
