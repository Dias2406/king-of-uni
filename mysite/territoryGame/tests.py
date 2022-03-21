from django.test import Client, TestCase, SimpleTestCase
from django.urls import resolve, reverse
from account.models import Account
from territoryGame.utils import get_center_coordinates, get_zoom
from territoryGame.views import territories_view, detail_territory_view


__author__ = "Edward Calonghi"


class TestUrls (SimpleTestCase):

    def test_territories_url_is_resolved(self):
        url = reverse('territory_game:territories')
        self.assertEquals(resolve(url).func, territories_view)


class TestViews (TestCase):

    def setUp(self):
        self.client = Client()
        self.notClient = Client()
        user = Account.objects.create(email='test@exeter.ac.uk', username='test',password='12345')
        self.client.force_login(user)

    def test_territories_view(self):
        territory_url = reverse('territory_game:territories')
        response = self.client.get(territory_url)
        response2 = self.notClient.get(territory_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response2.status_code, 302)
    
    def test_detail_view(self):
        territory_url = '/territory_game/into'
        response = self.client.get(territory_url)
        response2 = self.notClient.get(territory_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response2.status_code, 302)