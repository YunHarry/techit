from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, CreateView

from articleapp.forms import ArticleForm
from articleapp.models import Article


# Create your views here.
class TempView(TemplateView):
    template_name = 'articleapp/temp.html'

@method_decorator(login_required,'get')
@method_decorator(login_required,'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articleapp/create.html'