from django.conf.urls import url
from vacancies import views

app_name = 'vacancies'

urlpatterns = [
    url(r'^vacancies/$', views.VacancyListView.as_view(), name='vacancies'),
    url(r'^vacancies/create$', views.VacancyCreateView.as_view(), name='create'),

   ]