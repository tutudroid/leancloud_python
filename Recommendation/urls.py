# coding: utf-8

from django.conf.urls import url
from Recommendation import views


urlpatterns = [
    # everyday recommendation
    url(r'AllRecommendation/$', views.AllRecommendation, name='AllRecommendation'),
    url(r'AddRecommendation/$', views.AddRecommendation, name='AddRecommendation'),
    url(r'EditRecommendation/$', views.EditRecommendation, name='EditRecommendation'),
    url(r'ShowRecommendation/$', views.ShowRecommendation, name='ShowRecommendation'),
]
