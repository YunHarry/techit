from django.urls import path

from articleapp.views import TempView, ArticleCreateView

app_name = "articleapp"

urlpatterns = [
    path("temp/", TempView.as_view(), name="temp"),
    path("create/", ArticleCreateView.as_view(), name="create"),
]