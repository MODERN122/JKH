# Generated by Django 2.2.3 on 2019-07-20 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_votecomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Время создания'),
        ),
    ]
