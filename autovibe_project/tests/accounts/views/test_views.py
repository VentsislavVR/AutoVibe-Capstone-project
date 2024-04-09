from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from autovibe_project.accounts.models import Profile

UserModel = get_user_model()
class TestRegisterUserView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_view(self):
        response = self.client.get(reverse('register_user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register_user.html')

    def test_register_form_submission(self):
        data = {'email': 'test@example.com', 'password1': 'password', 'password2': 'password'}
        response = self.client.post(reverse('register_user'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(UserModel.objects.filter(email='test@example.com').exists())



class TestLoginUserView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_view(self):
        response = self.client.get(reverse('login_user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login_user.html')



class TestLogoutUserView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_logout_view(self):
        response = self.client.get(reverse('logout_user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/logout_user.html')


class TestProfileDetailsView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(email='test@example.com', password='password')
        self.user.profile.first_name = 'Test'
        self.user.profile.last_name = 'User'
        self.user.profile.save()

    def test_profile_details_view(self):
        self.client.login(email='test@example.com', password='password')
        response = self.client.get(reverse('profile_details', kwargs={'pk': self.user.profile.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/details_profile.html')


class TestProfileUpdateView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(email='test@example.com', password='password')
        self.user.profile.first_name = 'Test'
        self.user.profile.last_name = 'User'
        self.user.profile.save()

    def test_profile_update_view(self):
        self.client.login(email='test@example.com', password='password')
        response = self.client.get(reverse('profile_update', kwargs={'pk': self.user.profile.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/edit_profile.html')

    def test_profile_update_form_submission(self):
        self.client.login(email='test@example.com', password='password')
        data = {'first_name': 'Updated First Name', 'last_name': 'Updated Last Name'}
        response = self.client.post(reverse('profile_update', kwargs={'pk': self.user.profile.pk}), data)
        self.assertEqual(response.status_code, 302)
        self.user.profile.refresh_from_db()
        self.assertEqual(self.user.profile.first_name, 'Updated First Name')
        self.assertEqual(self.user.profile.last_name, 'Updated Last Name')



class TestProfileDeleteView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(email='test@example.com', password='password')
        self.user.profile.first_name = 'Test'
        self.user.profile.last_name = 'User'
        self.user.profile.save()

    def test_profile_delete_view(self):
        self.client.login(email='test@example.com', password='password')
        response = self.client.get(reverse('profile_delete', kwargs={'pk': self.user.profile.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/delete_profile.html')

    def test_profile_delete_confirmation(self):
        self.client.login(email='test@example.com', password='password')
        response = self.client.post(reverse('profile_delete', kwargs={'pk': self.user.profile.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Profile.objects.filter(user=self.user).exists())