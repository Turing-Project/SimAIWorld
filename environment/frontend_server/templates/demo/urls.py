from django.template.defaulttags import url
from django.urls import path

from environment.frontend_server.translator import views

urlpatterns = [
    url(r'^$', views.demo, name='demo'),
    path('my-ajax-test/', views.testcall),
]