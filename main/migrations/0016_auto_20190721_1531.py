# Generated by Django 2.2.3 on 2019-07-21 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20190721_0200'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='coordinates1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='application',
            name='coordinates2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='votes', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
