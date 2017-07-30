from django.conf.urls import url
from . import views

app_name = 'users'

urlpatterns = [
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^create_profile/$', views.TraineeInfoCreateView.as_view(), name='create_profile'),
    url(r'^edit_profile/$', views.TraineeInfoUpdateView.as_view(), name='edit_profile'),
    url(r'^change_password/$', views.change_password, name='change_password'),
   ]