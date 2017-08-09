from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^book$', views.BookRide.as_view(), name='book'),
]
