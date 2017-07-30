from django.contrib import admin
from specs.models import Spec, SpecType, Lesson, Test, Question, Answer

admin.site.register(Spec)
admin.site.register(SpecType)

admin.site.register(Lesson)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)



