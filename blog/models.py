from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class BlogArticles(models.Model):
    title = models.CharField(max_length=300, verbose_name="标题")
    author = models.ForeignKey(User, related_name="blog_posts", on_delete=models.DO_NOTHING, verbose_name="作者")
    body = models.TextField(verbose_name="内容")
    icon = models.CharField(max_length=300, verbose_name="图片", blank=True)
    publish = models.DateTimeField(default=timezone.now, verbose_name="提交时间")

    class Meta:
        ordering = ("-publish",)
        verbose_name = "博客内容"
        verbose_name_plural = "博客内容"

    def __str__(self):
        return self.title

