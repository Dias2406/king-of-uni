from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from account.views import registration_view, login_view, logout_view, account_view
from account.models import Account
from account.forms import RegistrationForm, AccountUpdateForm

# Create your tests here.
__author__ = "Dias Jakupov"


class TestUrls (SimpleTestCase):

    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, registration_view)
    
    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login_view)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout_view)

    def test_acccount_url_is_resolved(self):
        url = reverse('account')
        self.assertEquals(resolve(url).func, account_view)



class TestViews (TestCase):

    def setUp(self):
        self.client = Client()
        self.notClient = Client()
        user = Account.objects.create(email='test@exeter.ac.uk', username='test',password='12345')
        self.client.force_login(user)

    def test_registration_view(self):
        register_url = reverse('register')
        response = self.client.get(register_url)
        response2 = self.notClient.get(register_url)
        self.assertEquals(response.status_code, 200)
        

    def test_login_view(self):
        login_url = reverse('login')
        response = self.client.get(login_url)
        response2 = self.notClient.get(login_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response2.status_code, 200)

    def test_logout_view(self):
        logout_url = reverse('logout')
        response = self.client.get(logout_url)
        response2 = self.notClient.get(logout_url)
        self.assertEquals(response2.status_code, 302)

    def test_account_view(self):
        account_url = reverse('account')
        response = self.client.get(account_url)
        response2 = self.notClient.get(account_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response2.status_code, 302)

class TestForms(TestCase):

    def test_RegistrationForm_data(self):
        form = RegistrationForm(data={
            'email': 'test1111@exeter.ac.uk',
            'username': 'Test1111',
            'latitude': '32.222222',
            'longitude': '43.222222',
            'password1': 'Qqwerty1!',
            'password2': 'Qqwerty1!',
        })
        self.assertTrue(form.is_valid())
    
    def test_RegistrationForm_no_data(self):
        form = RegistrationForm(data={})
        self.assertFalse(form.is_valid())

    def test_AccountUpdateForm_data(self):
        form = AccountUpdateForm(data={
            'email': 'test1111@exeter.ac.uk',
            'username': 'Test1111',
        })
        self.assertTrue(form.is_valid())
    
    def test_AccountUpdateForm_one_data(self):
        form = AccountUpdateForm(data={
            'email': 'test1111@exeter.ac.uk',
        })
        self.assertFalse(form.is_valid())
