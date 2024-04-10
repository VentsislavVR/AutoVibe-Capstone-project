from datetime import date

from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Profile

UserModel = get_user_model()


class AutoVibeUserCreationForm(auth_forms.UserCreationForm):
    user = None
    confirm_age = forms.BooleanField(label='I confirm that I am 14 years or older')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Paassword'
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("The two password fields didn't match."))
        confirm_age = cleaned_data.get('confirm_age')
        if not confirm_age:
            raise forms.ValidationError("You must confirm that you are 14 years or older to register.")

        date_of_birth = cleaned_data.get('date_of_birth')
        if date_of_birth:
            today = date.today()
            age = today.year - date_of_birth.year - (
                        (today.month, today.day) < (date_of_birth.month, date_of_birth.day))
            if age < 14:
                raise forms.ValidationError("You must be at least 14 years old to register.")

        return cleaned_data

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email', 'password1', 'password2', 'confirm_age')

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
        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'date_of_birth': _('Date of Birth'),
            'profile_picture': _('Profile Picture'),
            'telephone_number': _('Telephone Number'),
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name'}),
            'date_of_birth': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'profile_picture': forms.FileInput(attrs={'accept': 'image/*'}),
            'telephone_number': forms.TextInput(attrs={'placeholder': 'Enter your telephone number'}),
        }
    def clean_profile_picture(self):
        profile_picture = self.cleaned_data.get('profile_picture')
        user = self.instance.user

        # Check if the user already has a profile picture
        if user.profile.profile_picture and profile_picture:
            raise forms.ValidationError("You can only upload one profile picture.")

        return profile_picture
    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth:
            today = date.today()
            age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
            if age < 14:
                raise forms.ValidationError("If you are less than 14 years old you will not be able to use AutoVibe.")
        return date_of_birth
class ProfileUpdateForm(ProfileBaseForm):
    pass

