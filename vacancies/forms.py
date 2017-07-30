from django import forms
from vacancies.models import Vacancy


class VacancyCreateForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        exclude = ['user', 'trainee']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(VacancyCreateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        vacancy = super(VacancyCreateForm, self).save(commit=False)
        vacancy.user = self.request.user
        if commit:
            vacancy.save()
        return vacancy


class VacancyUpdateForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        exclude = ['user', 'trainee']