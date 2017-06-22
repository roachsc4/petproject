from django import forms
from specs.models import Lesson


class LessonCreateForm(forms.ModelForm):
    class Meta:
        model = Lesson
        exclude = ['trainee']