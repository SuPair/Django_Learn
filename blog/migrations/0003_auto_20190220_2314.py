# Generated by Django 2.1.7 on 2019-02-20 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190220_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticles',
            name='icon',
            field=models.CharField(blank=True, max_length=300, verbose_name='图片'),
        ),
    ]
