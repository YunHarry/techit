from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False,
                             related_name='owner')
    target_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False,
                                    related_name='target')

    class Meta:
        unique_together = ('user', 'target_user')