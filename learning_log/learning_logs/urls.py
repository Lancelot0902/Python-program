""" define url_model of learning_logs """

from django.conf.urls import url

from . import views

urlpatterns = [
    # main page
    url(r'^$',views.index,name='index'),

    # show topics
    url(r'^topics/$',views.topics,name='topics'),

    # show one topic page
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),

    # add new topic url
    url(r'^new_topic/$',views.new_topic,name='new_topic'),

    # add new entry url
    url(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),

    # edit entry url
    url(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,name='edit_entry'),
]