from django.conf.urls import url
from django.views import generic
from . import views


urlpatterns=[
    url(r'^$',views.GenerateRandomUserView.as_view())
]