import imp
from unicodedata import name
from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from gameKeeper.models import Building
from gameKeeper.views import game_keeper_view, create_building_view, detail_building_view
from account.models import Account
from gameKeeper.forms import CreateBuildingForm


__author__ = "Dias Jakupov"


class TestUrls (SimpleTestCase):

    def test_gameKeeper_url_is_resolved(self):
        url = reverse('game_keeper:settings')
        self.assertEquals(resolve(url).func, game_keeper_view)
    
    def test_create_building_url_is_resolved(self):
        url = reverse('game_keeper:create')
        self.assertEquals(resolve(url).func, create_building_view)
    
    def test_detail_building_url_is_resolved(self):
        url = reverse('game_keeper:detail', kwargs={'slug': 'streatham'})
        self.assertEquals(resolve(url).func, detail_building_view)


class TestViews (TestCase):

    def setUp(self):
        self.client = Client()
        self.notClient = Client()
        user = Account.objects.create(email='test@exeter.ac.uk', username='test',password='12345')
        Building.objects.create(name='Streatham', latitude='12.2222', longitude='32.2333')
        self.client.force_login(user)

    def test_game_keeper_view(self):
        game_keeper_url = reverse('game_keeper:settings')
        response = self.client.get(game_keeper_url)
        response2 = self.notClient.get(game_keeper_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response2.status_code, 302)

    def test_create_building_view(self):
        create_building = reverse('game_keeper:create')
        response = self.client.get(create_building)
        response2 = self.notClient.get(create_building)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response2.status_code, 302)

    def test_detail_building_view(self):
        detail_url = reverse('game_keeper:detail', kwargs={'slug': 'streatham'})
        response = self.client.get(detail_url)
        self.assertEquals(response.status_code, 200)


class TestForms(TestCase):

    def test_CreateBuildingFrom_data(self):
        form = CreateBuildingForm(data={
            'name': 'Forum',
            'latitude': '10.23333',
            'longitude': '30.2212',
        })
        self.assertTrue(form.is_valid())
    
    def test_CreateBuildingForm__no_data(self):
        form = CreateBuildingForm(data={})
        self.assertFalse(form.is_valid())
