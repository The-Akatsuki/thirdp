from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^book$', views.BookRide.as_view(), name='book'),
    url(r'^bookaride$', views.BookRide.as_view(), name='bookaride'),
    url(r'^cancelRide$', views.cancelRide.as_view(), name='cancelRide'),
]
