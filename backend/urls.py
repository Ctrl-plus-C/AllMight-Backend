from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Command.as_view(), name="home"),
]