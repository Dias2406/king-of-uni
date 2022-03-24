from datetime import datetime, timedelta
import time as t
from django.test import Client, TestCase, SimpleTestCase
from django.urls import resolve, reverse
from account.models import Account
from gameKeeper.models import Building
from territoryGame.views import territories_view, detail_territory_view
from territoryGame.forms import CreateTerritoryCaptureForm, UserLocationForm

__author__ = "Edward Calonghi"


class TestUrls (SimpleTestCase):

    def test_territories_url_is_resolved(self):
        url = reverse('territory_game:territories')
        self.assertEquals(resolve(url).func, territories_view)

    def test_detail_territory_url_is_resolved(self):
        url = reverse('territory_game:detail_territory', kwargs={'slug': 'into'})
        self.assertEquals(resolve(url).func, detail_territory_view)


class TestViews (TestCase):

    def setUp(self):
        self.client = Client()
        self.notClient = Client()
        user = Account.objects.create(email='test@exeter.ac.uk', username='test',password='12345')
        Building.objects.create(name='Into', latitude='12.2222', longitude='32.2333', is_active='True')
        self.client.force_login(user)

    def test_territories_view(self):
        territory_url = reverse('territory_game:territories')
        response = self.client.get(territory_url)
        response2 = self.notClient.get(territory_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response2.status_code, 302)

    def test_detail_view(self):
        territory_url = reverse('territory_game:detail_territory', kwargs={'slug': 'into'})
        response = self.client.get(territory_url)
        response2 = self.notClient.get(territory_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response2.status_code, 302)


class TestForms(TestCase):

    def test_CreateTerritoryCaptureForm_data(self):
        form = CreateTerritoryCaptureForm(data={
            'comment': 'I am the king',
        })
        self.assertTrue(form.is_valid())
    
    def test_CreateTerritoryCaptureForm_no_data(self):
        form = CreateTerritoryCaptureForm(data={})
        self.assertTrue(form.is_valid())

    def test_UserLocationForm_data(self):
        form = UserLocationForm(data={
            'latitude': 10.24123,
            'longitude': 12.486112,
        })
        self.assertTrue(form.is_valid())
    
    def test_UserLocationForm_no_data(self):
        form = UserLocationForm(data={})
        self.assertTrue(form.is_valid())
        

class testDateTime(SimpleTestCase):

    def test_example(self):
        capture = datetime.now()
        t.sleep(5)
        recapture = datetime.now()
        elapsed = recapture - capture
        cooldown = timedelta(seconds=10)
        if elapsed > cooldown:
            print ('capturable')
        else:
            print ('not capturable')