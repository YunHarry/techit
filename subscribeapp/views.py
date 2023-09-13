from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from subscribeapp.models import Subscription


class SubscribeView(RedirectView):
    # 구독 여부를 확인하고 삭제
    def get(self, request, *args, **kwargs):
        user = request.user
        target_user = User.objects.get(pk=self.kwargs['pk'])

        subs = Subscription.objects.filter(user=user,
                                           target_user=target_user)

        if subs:
            subs.delete()
        else:
            Subscription(user=user, target_user=target_user).save()

        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('accountapp:detail',
                       kwargs={'pk': self.kwargs['pk']})

class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 20

    def get_queryset(self):
        target_user_list = Subscription.objects.filter(user=self.request.user).values_list('target_user')
        article_list = Article.objects.filter(writer__in=target_user_list)
        return  article_list
