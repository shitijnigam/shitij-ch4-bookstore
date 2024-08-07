# library functions
from django.test import SimpleTestCase
from django.urls import reverse, resolve

# local functions
from .views import HomePageView

# Create your tests here.


class HomepageTests(SimpleTestCase):

    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        # response = self.client.get("/")
        self.assertEqual(self.response.status_code, 200)

    # def test_homepage_url_name(self):
    #     # response = self.client.get(reverse("home"))
    #     self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        # response = self.client.get("/")
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_html(self):
        # response = self.client.get("/")
        self.assertContains(self.response, "home page")

    def test_homepage_does_not_contain_incorrect_html(self):
        # response = self.client.get("/")
        self.assertNotContains(self.response, "Hi there! I shouldn't be on this page")

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
