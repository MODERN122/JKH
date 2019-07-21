# Generated by Django 2.2.3 on 2019-07-20 18:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20190720_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Время создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='temp_password',
            field=models.CharField(blank=True, max_length=128, verbose_name='Временный пароль'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
