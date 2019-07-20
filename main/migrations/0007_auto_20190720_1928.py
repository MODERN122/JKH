# Generated by Django 2.2.3 on 2019-07-20 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190720_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='management_company',
        ),
        migrations.AddField(
            model_name='application',
            name='territory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='applications', to='main.Territory'),
        ),
        migrations.AddField(
            model_name='applicationcomment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='application_comments', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
            preserve_default=False,
        ),
    ]