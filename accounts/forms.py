from django import forms
from django.utils.translation import pgettext, ugettext_lazy as _, ugettext

from allauth.account.forms import LoginForm, SignupForm
from allauth.account.forms import BaseSignupForm, SetPasswordField, PasswordField
from allauth.account import app_settings
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'type': 'email', 'class': 'form-control input-lg',
                                                             'autofocus': 'autofocus', 'tabindex': '1',
                                                             'required': 'true', 'placeholder': 'Email Address (*)', })
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control input-lg', 'tabindex': '2',
                                                                    'required': 'true', 'placeholder': 'Password (*)',
                                                                    })


class SignupForm(BaseSignupForm):

    first_name = forms.CharField(max_length=30, label='First name')
    last_name = forms.CharField(max_length=30, label='Last name')
    password1 = SetPasswordField(label=_("Password"))
    password2 = PasswordField(label=_("Password (again)"))
    terms = forms.BooleanField(required=True, label=_("Terms of use"))
    confirmation_key = forms.CharField(max_length=40, required=False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        if not app_settings.SIGNUP_PASSWORD_VERIFICATION:
            del self.fields["password2"]

    def clean(self):
        super(SignupForm, self).clean()
        if app_settings.SIGNUP_PASSWORD_VERIFICATION \
                and "password1" in self.cleaned_data \
                and "password2" in self.cleaned_data:
            if self.cleaned_data["password1"] \
                    != self.cleaned_data["password2"]:
                raise forms.ValidationError(_("You must type the same password"
                                              " each time."))
        return self.cleaned_data

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        # TODO: Move into adapter `save_user` ?
        setup_user_email(request, user, [])
        return user


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget = forms.TextInput(attrs={'type': 'input', 'class': 'form-control input-lg',
                                                                  'autofocus': 'autofocus', 'tabindex': '1',
                                                                  'required': 'true', 'placeholder': 'First Name (*)',
                                                                  })
        self.fields['last_name'].widget = forms.TextInput(attrs={'type': 'input', 'class': 'form-control input-lg',
                                                                 'autofocus': 'autofocus', 'tabindex': '2',
                                                                 'required': 'true', 'placeholder': 'Last Name (*)', })
        self.fields['email'].widget = forms.TextInput(attrs={'type': 'email', 'class': 'form-control input-lg',
                                                             'autofocus': 'autofocus', 'tabindex': '3',
                                                             'required': 'true', 'placeholder': 'Email Address (*)', })
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control input-lg', 'tabindex': '4',
                                                                     'required': 'true', 'placeholder': 'Password (*)',
                                                                     })
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control input-lg', 'tabindex': '5',
                                                                     'required': 'true', 'placeholder':
                                                                         'Confirm Password (*)', })
        self.fields['terms'].widget = forms.CheckboxInput(attrs={'class': 'hidden', })

