from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.DO_NOTHING)
    birth = models.DateTimeField(blank=True, null=True, verbose_name='生日')
    phone = models.CharField(max_length=11, null=True, verbose_name='手机')

    class Meta:
        verbose_name = '用户扩展信息'
        verbose_name_plural = '用户扩展信息'

    def __str__(self):
        return 'user{}'.format(self.user.username)

