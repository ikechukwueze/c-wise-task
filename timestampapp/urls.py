from django.urls import path
from . import views



urlpatterns = [
    path("", views.uuid_timestamp_view),
]