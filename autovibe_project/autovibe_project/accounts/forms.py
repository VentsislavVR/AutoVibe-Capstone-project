from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms
from .models import Profile

UserModel = get_user_model()


class AutoVibeUserCreationForm(auth_forms.UserCreationForm):
    user = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Paassword'
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email', 'password1', 'password2')

        # widgets = {
        #     'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        #     'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        #     'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        # }



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
