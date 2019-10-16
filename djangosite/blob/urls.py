from django.conf.urls import url
from . import views as blob_views


urlpatterns=[
    url(r'^$', blob_views.blob_home),

# http://127.0.0.1:8000/blob/1/
    url(r'^(?P<post_id>\d+)/$', blob_views.blob_post)
]