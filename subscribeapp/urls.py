from django.urls import path

from subscribeapp.views import SubscribeView

app_name = 'subscribeapp'

urlpatterns = [
    path("sub/<int:pk>", SubscribeView.as_view(), name="sub"),
]