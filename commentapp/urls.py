from django.urls import path

from commentapp.views import CommentCreateView, CommentUpdateView, CommentDeleteView

app_name = 'commentapp'

urlpatterns = [
    path("create/", CommentCreateView.as_view(), name="create"),
    path("update/<int:pk>/", CommentUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", CommentDeleteView.as_view(), name="delete"),
]