from django import forms
from specs.models import Lesson, Test, Question


class LessonCreateForm(forms.ModelForm):
    class Meta:
        model = Lesson
        exclude = ['trainee']


class TestCreateForm(forms.ModelForm):
    class Meta:
        model = Test
        exclude = ['trainee', 'created', 'updated']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(TestCreateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        test = super(TestCreateForm, self).save(commit=False)
        test.user = self.request.user
        if commit:
            test.save()
        return test


class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['created', 'updated']
