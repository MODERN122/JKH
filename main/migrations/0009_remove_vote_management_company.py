# Generated by Django 2.2.3 on 2019-07-20 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='management_company',
        ),
    ]
