# Generated by Django 2.1.7 on 2019-02-20 23:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogarticles',
            options={'ordering': ('-publish',), 'verbose_name': '博客内容', 'verbose_name_plural': '博客内容'},
        ),
        migrations.AlterField(
            model_name='blogarticles',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='blog_posts', to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='blogarticles',
            name='body',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='blogarticles',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='提交时间'),
        ),
    ]