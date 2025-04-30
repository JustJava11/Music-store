from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from profiles.models import UserProfile


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=128)
    last_name = forms.CharField(max_length=128)
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email', 'password1', 'password2',
        ]

        def save(self, commit=True):
            user = super().save(commit=False)
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', "avatar"]

        widgets = {
            'bio': forms.TextInput(
                attrs={
                    "placeholder": 'Описание',
                    'class': 'form-control',
                }
            ),
            "avatar": forms.ClearableFileInput(
                attrs={
                    "class": "form-control"
                }
            )
        }


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)
        exclude = ('password',)
