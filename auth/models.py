from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class InviteCode(models.Model):
    code = models.CharField(max_length=10, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} - {self.code}'
