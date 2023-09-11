from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView

from articleapp.decorators import article_ownership_required
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
    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail',
                       kwargs={'pk': self.object.pk})

class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articleapp/update.html'
    context_object_name = 'target_article'
    def get_success_url(self):
        return reverse('articleapp:detail',
                       kwargs={'pk': self.object.pk})

@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articleapp/delete.html'
    context_object_name = 'target_article'
    def get_success_url(self):
        return reverse('accountapp:hello_world')