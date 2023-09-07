from django.forms import models, ModelForm

from articleapp.models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = [
            'image',
            'title',
            'content',
        ]
