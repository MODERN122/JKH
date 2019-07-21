# Generated by Django 2.2.3 on 2019-07-20 21:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20190720_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='duration',
        ),
        migrations.AddField(
            model_name='vote',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время окончания сбора голосов'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vote',
            name='is_moderated',
            field=models.BooleanField(default=False, verbose_name='Отмодерировано'),
        ),
    ]