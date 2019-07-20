# Generated by Django 2.2.3 on 2019-07-20 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190720_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.TextField(verbose_name='Комментарий')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Время создания')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.Application', verbose_name='Заявка')),
            ],
        ),
    ]
