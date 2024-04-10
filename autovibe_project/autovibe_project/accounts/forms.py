from datetime import date

from django.contrib.auth import forms as auth_forms, get_user_model, password_validation
from django import forms
from django.core.exceptions import ValidationError
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

    def clean_password1(self):
        password = self.cleaned_data["password1"]

        # Custom validation (e.g., minimum uppercase/lowercase characters)
        if not any(char.isupper() for char in password):
            raise ValidationError(_("Password must contain at least one uppercase letter."))
        if not any(char.islower() for char in password):
            raise ValidationError(_("Password must contain at least one lowercase letter."))
        if not any(char.isdigit() for char in password):
            raise ValidationError(_("Password must contain at least one digit."))
        if len(password) < 8:
            raise ValidationError(_("Password must be at least 8 characters long."))
        if len(password) > 64:
            raise ValidationError(_("Password must be at most 64 characters long."))

        errors = password_validation.validate_password(password)
        if errors:
            raise ValidationError(errors)

        return password

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

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth:
            today = date.today()
            age = today.year - date_of_birth.year - (
                        (today.month, today.day) < (date_of_birth.month, date_of_birth.day))
            if age < 14:
                raise forms.ValidationError("If you are less than 14 years old you will not be able to use AutoVibe.")
        return date_of_birth


class ProfileUpdateForm(ProfileBaseForm):
    pass
