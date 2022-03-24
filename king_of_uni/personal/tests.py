from django.test import Client, TestCase, SimpleTestCase
from django.urls import resolve, reverse
from account.models import Account
from personal.views import home_screen_view, rules_screen_view, leaderboard_view
from gameKeeper.models import Building


__author__ = "Edward Calonghi"


class TestUrls (SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home_screen_view)

    def test_rules_url_is_resolved(self):
        url = reverse('rules')
        self.assertEquals(resolve(url).func, rules_screen_view)

    def test_leaderboard_url_is_resolved(self):
        url = reverse('leaderboard')
        self.assertEquals(resolve(url).func, leaderboard_view)


class TestViews (TestCase):

    def setUp(self):
        self.client = Client()
        self.notClient = Client()
        user = Account.objects.create(email='test@exeter.ac.uk', username='test',password='12345')
        self.client.force_login(user)

    def test_home_screen_view(self):
        home_url = reverse('home')
        response = self.client.get(home_url)
        response2 = self.notClient.get(home_url)
        self.assertEquals(response.status_code, 200)
    
    def test_rules_screen_view(self):
        home_url = reverse('rules')
        response = self.client.get(home_url)
        response2 = self.notClient.get(home_url)
        self.assertEquals(response.status_code, 200)

    def test_leaderbord_view(self):
        leaderboard_url = reverse('leaderboard')
        response = self.client.get(leaderboard_url)
        response2 = self.notClient.get(leaderboard_url)
        self.assertEquals(response.status_code, 200)