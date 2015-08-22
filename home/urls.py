from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='go_home'),

    url(r'test1/$', views.Test1View.as_view(), name='go_test1'),
    url(r'test2/$', views.Test2View.as_view(), name='go_test2'),

]