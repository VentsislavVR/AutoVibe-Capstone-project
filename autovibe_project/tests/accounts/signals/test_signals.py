from django.test import TestCase
from django.contrib.auth import get_user_model

from autovibe_project.accounts.models import Profile


UserModel = get_user_model()


class TestSignal(TestCase):
    def test_profile_creation_signal(self):
        user = UserModel.objects.create_user(email='test@example.com', password='password')
        profile_exists = Profile.objects.filter(user=user).exists()
        self.assertTrue(profile_exists)
