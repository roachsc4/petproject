from django.conf.urls import url
from specs import views

app_name = 'specs'

urlpatterns = [
    url(r'^create_spec_type/$', views.SpecTypeCreateView.as_view(), name='create_spec_type'),
    url(r'^create_spec/$', views.SpecCreateView.as_view(), name='create_spec'),
   ]