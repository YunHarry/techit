from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import RedirectView

from subscribeapp.models import Subscription


class SubscribeView(RedirectView):
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