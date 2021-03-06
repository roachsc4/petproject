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
    url(r'^lessons/(?P<pk>\d+)/create_test$',                 views.TestCreateView.as_view(), name='create_test'),
    url(r'^tests/create$',                                    views.TestCreateView.as_view(), name='create_test_wo_pk'),
    url(r'^tests/create_ajax$',                               views.test_create, name='create_test_ajax'),
    url(r'^tests/(?P<pk>\d+)/test_detail$',                   views.TestDetailView.as_view(), name='test_detail'),
    url(r'^tests/(?P<pk>\d+)/update$',                        views.TestUpdateView.as_view(), name='update_test'),
    url(r'^tests/(?P<pk>\d+)/update_ajax$',                   views.test_update, name='update_test_ajax'),
    url(r'^tests/(?P<pk>\d+)/delete$',                        views.TestDeleteView.as_view(), name='delete_test'),
    url(r'^tests/(?P<pk>\d+)/delete_ajax$',                   views.test_delete, name='delete_test_ajax'),
    url(r'^tests/(?P<pk>\d+)/start$',                         views.test_start, name='start_test'),
    url(r'^tests/(?P<pk>\d+)/passing$',                       views.test_passing, name='pass_test'),
    url(r'^tests/$',                                          views.TestListView.as_view(), name='tests'),
    url(r'^tests/(?P<pk>\d+)/set$',                           views.TestSetView.as_view(), name='set_test'),
    url(r'^tests/(?P<pk>\d+)/set/create_question$', views.QuestionCreateView.as_view(), name='create_question'),
    url(r'^questions/(?P<pk>\d+)/update$',          views.QuestionUpdateView.as_view(), name='update_question'),
    url(r'^questions/(?P<pk>\d+)/delete$',          views.QuestionDeleteView.as_view(), name='delete_question'),
    url(r'^questions/(?P<pk>\d+)/set$',             views.QuestionSetView.as_view(), name='set_question'),
    url(r'^questions/(?P<pk>\d+)/set/create_answer$', views.AnswerCreateView.as_view(), name='create_answer'),
    url(r'^answers/(?P<pk>\d+)/update$', views.AnswerUpdateView.as_view(), name='update_answer'),
    url(r'^answers/(?P<pk>\d+)/delete$', views.AnswerDeleteView.as_view(), name='delete_answer'),

   ]
