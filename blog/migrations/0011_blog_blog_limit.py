# Generated by Django 2.0 on 2020-06-09 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200602_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_limit',
            field=models.IntegerField(default=0),
        ),
    ]
