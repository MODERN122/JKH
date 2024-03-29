# Generated by Django 2.2.3 on 2019-07-20 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_vote_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание')),
                ('start_date', models.DateTimeField(verbose_name='Время начала')),
                ('end_date', models.DateTimeField(verbose_name='Время окончания')),
                ('management_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='active_works', to='main.ManagementCompany', verbose_name='УК')),
            ],
        ),
    ]
