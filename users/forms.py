from django import forms
from django.utils import timezone
from users.models import User, TraineeInfo
from django.forms.widgets import DateInput
from django.contrib.admin import widgets


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.created_date = timezone.now()
        if commit:
            user.save()
        return user


class CustomDateInput(forms.DateInput):
    input_type = 'date'


class TraineeInfoForm(forms.ModelForm):
    class Meta:
        model = TraineeInfo
        exclude = ['user']
        widgets = {
            'birth_date': CustomDateInput(),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(TraineeInfoForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        trainee_info = super(TraineeInfoForm, self).save(commit=False)
        trainee_info.user = self.request.user
        if commit:
            trainee_info.save()
        return trainee_info
