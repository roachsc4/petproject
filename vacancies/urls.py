from django.conf.urls import url
from vacancies import views

app_name = 'vacancies'

urlpatterns = [
    url(r'^vacancies/$', views.VacancyListView.as_view(), name='vacancies'),
    url(r'^vacancies/create$', views.VacancyCreateView.as_view(), name='create'),
    url(r'^vacancies/(?P<pk>\d+)/update$', views.VacancyUpdateView.as_view(), name='update'),
    url(r'^vacancies/(?P<pk>\d+)/delete$', views.VacancyDeleteView.as_view(), name='delete'),
   ]