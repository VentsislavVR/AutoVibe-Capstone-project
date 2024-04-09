from django.test import TestCase
from django.contrib.auth import get_user_model
from autovibe_project.accounts.models import Profile

UserModel = get_user_model()

class TestProfileModel(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(email='test@example.com', password='password')


    def test_full_name_property(self):
        self.user.profile.first_name = 'John'
        self.user.profile.last_name = 'Doe'
        self.user.profile.save()
        self.assertEqual(self.user.profile.full_name, 'John Doe')

    def test_full_name_property_only_first_name(self):
        self.user.profile.first_name = 'John'
        self.user.profile.save()
        self.assertEqual(self.user.profile.full_name, 'John')

    def test_full_name_property_only_last_name(self):
        self.user.profile.last_name = 'Doe'
        self.user.profile.save()
        self.assertEqual(self.user.profile.full_name, 'Doe')