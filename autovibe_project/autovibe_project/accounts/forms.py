from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms
from .models import Profile

UserModel = get_user_model()


class AutoVibeUserCreationForm(auth_forms.UserCreationForm):
    user = None

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class AutoVibeChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'date_of_birth', 'profile_picture', 'telephone_number']

    def clean_profile_picture(self):
        profile_picture = self.cleaned_data.get('profile_picture')
        user = self.instance.user

        # Check if the user already has a profile picture
        if user.profile.profile_picture and profile_picture:
            raise forms.ValidationError("You can only upload one profile picture.")

        return profile_picture
