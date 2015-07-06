from django.conf.urls import include, url

from .views import ProfileView


urlpatterns = [
    url(r'^accounts/$', ProfileView.as_view(), name='go_a_profile'),
    url(r'^accounts/profile/$', ProfileView.as_view(), name='go_profile'),
]