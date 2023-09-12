from django.urls import path

from commentapp.views import CommentCreateView, CommentUpdateView

app_name = 'commentapp'

urlpatterns = [
    path("create/", CommentCreateView.as_view(), name="create"),
    path("update/<int:pk>/", CommentUpdateView.as_view(), name="update"),
]