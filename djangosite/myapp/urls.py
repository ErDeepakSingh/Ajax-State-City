from django.conf.urls import url
from .views import (home,
                    add_student,
                    login_student,HomeView,StudentApiView)

urlpatterns = [
    url(r'^$', home, name='app_home'),
    url(r'^add-student/$', add_student, name='app_add_student'),
    url(r'^login-student/$', login_student, name='app_login-student'),
    url(r'^home/$', HomeView.as_view()),
    url(r'^api/$', StudentApiView.as_view()),
]
