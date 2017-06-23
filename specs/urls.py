from django.conf.urls import url
from specs import views

app_name = 'specs'

urlpatterns = [
    url(r'^create_spec_type/$',          views.SpecTypeCreateView.as_view(), name='create_spec_type'),
    url(r'^create_spec/$',               views.SpecCreateView.as_view(), name='create_spec'),
    url(r'^lessons/$',                   views.LessonListView.as_view(), name='lessons'),
    url(r'^lessons/create$',             views.LessonCreateView.as_view(), name='create_lesson'),
    url(r'^lessons/(?P<pk>\d+)/detail$', views.LessonDetailView.as_view(), name='lesson_detail'),
    url(r'^lessons/(?P<pk>\d+)/update$', views.LessonUpdateView.as_view(), name='update_lesson'),
    url(r'^lessons/(?P<pk>\d+)/delete$', views.LessonDeleteView.as_view(), name='delete_lesson'),
    url(r'^lessons/(?P<pk>\d+)/pass$',   views.LessonPassView.as_view(), name='pass_lesson'),
   ]