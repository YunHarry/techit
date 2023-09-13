from django.urls import path

from subscribeapp.views import SubscribeView, SubscriptionListView

app_name = 'subscribeapp'

urlpatterns = [
    path("sub/<int:pk>", SubscribeView.as_view(), name="sub"),
    path("list/>", SubscriptionListView.as_view(), name="list"),
]