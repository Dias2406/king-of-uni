from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from group.views import group_view, join_group_view, leave_group_view
from account.models import Account
from group.forms import CreateGroupForm


__author__ = "Edward Calonghi"


class TestUrls (SimpleTestCase):

    def test_info_url_is_resolved(self):
        url = reverse('group:group_info')
        self.assertEquals(resolve(url).func, group_view)
    
    def test_join_url_is_resolved(self):
        url = reverse('group:join_group')
        self.assertEquals(resolve(url).func, join_group_view)
    
    def test_leave_url_is_resolved(self):
        url = reverse('group:leave_group')
        self.assertEquals(resolve(url).func, leave_group_view)


class TestViews (TestCase):

    def setUp(self):
        self.client = Client()
        self.notClient = Client()
        user = Account.objects.create(email='test@exeter.ac.uk', username='test',password='12345')
        self.client.force_login(user)

    def test_group_view(self):
        group_url = reverse('group:group_info')
        response = self.client.get( group_url)
        response2 = self.notClient.get( group_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response2.status_code, 302)

    def test_group_join_view(self):
        group_url = reverse('group:join_group')
        response = self.client.get( group_url)
        response2 = self.notClient.get( group_url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response2.status_code, 302)

    def test_group_leave_view(self):
        group_url = reverse('group:leave_group')
        response = self.client.get( group_url)
        self.assertEquals(response.status_code, 302)


class TestForms(TestCase):

    def test_CreateGroupForm_data(self):
        form = CreateGroupForm(data={
            'name': 'team fantastic',
        })
        self.assertTrue(form.is_valid())
    
    def test_CreateGroupForm_no_data(self):
        form = CreateGroupForm(data={})
        self.assertFalse(form.is_valid())
