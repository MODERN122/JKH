# Generated by Django 2.2.3 on 2019-07-20 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190720_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('context', models.TextField(verbose_name='Вопрос на голосование')),
                ('image1', models.ImageField(blank=True, upload_to='Votes')),
                ('image2', models.ImageField(blank=True, upload_to='Votes')),
                ('image3', models.ImageField(blank=True, upload_to='Votes')),
                ('duration', models.DurationField()),
                ('agree', models.ManyToManyField(related_name='agree_votes', to=settings.AUTH_USER_MODEL, verbose_name='Согласные пользователи')),
                ('disagree', models.ManyToManyField(related_name='disagree_votes', to=settings.AUTH_USER_MODEL, verbose_name='Несогласные пользователи')),
                ('management_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Votes', to='main.ManagementCompany', verbose_name='УК')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Votes', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
