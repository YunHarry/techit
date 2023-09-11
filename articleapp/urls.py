from django.urls import path

from articleapp.views import TempView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView

app_name = "articleapp"

urlpatterns = [
    path("temp/", TempView.as_view(), name="temp"),
    path("create/", ArticleCreateView.as_view(), name="create"),
    path("detail/<int:pk>/", ArticleDetailView.as_view(), name="detail"),
    path("update/<int:pk>/", ArticleUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", ArticleDeleteView.as_view(), name="delete"),
]