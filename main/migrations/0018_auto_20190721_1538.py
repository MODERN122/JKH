# Generated by Django 2.2.3 on 2019-07-21 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20190721_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='lat1',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='long1',
            new_name='long',
        ),
    ]