from django.test import TestCase
from django.contrib.auth import get_user_model
from autovibe_project.accounts.forms import AutoVibeUserCreationForm, ProfileBaseForm

UserModel = get_user_model()


class TestAutoVibeUserCreationForm(TestCase):
    def test_clean_passwords_match(self):
        form_data = {
            'email': 'test@example.com',
            'password1': 'password',
            'password2': 'not_the_same_password',
        }
        form = AutoVibeUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_clean_passwords_match_success(self):
        form_data = {
            'email': 'test@example.com',
            'password1': 'password',
            'password2': 'password',
        }
        form = AutoVibeUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())


class TestProfileBaseForm(TestCase):
    def test_clean_profile_picture(self):
        user = UserModel.objects.create_user(email='test@example.com', password='password')
        user.profile.profile_picture = 'existing_picture.jpg'
        user.profile.save()

        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'date_of_birth': '1990-01-01',
            'telephone_number': '123456789',
            'profile_picture': 'new_picture.jpg',
        }
        form = ProfileBaseForm(data=form_data, instance=user.profile)
        self.assertFalse(form.is_valid())
        self.assertIn("You can only upload one profile picture.", form.errors['profile_picture'])

    def test_clean_profile_picture_no_existing_picture(self):
        user = UserModel.objects.create_user(email='test@example.com', password='password')

        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'date_of_birth': '1990-01-01',
            'telephone_number': '123456789',
            'profile_picture': 'new_picture.jpg',
        }
        form = ProfileBaseForm(data=form_data, instance=user.profile)
        self.assertTrue(form.is_valid())
