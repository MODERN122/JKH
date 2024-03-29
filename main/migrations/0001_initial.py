# Generated by Django 2.2.3 on 2019-07-20 10:12

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('fullname', models.CharField(max_length=200, verbose_name='ФИО')),
                ('passport_id', models.CharField(blank=True, max_length=10, verbose_name='Номер паспорта')),
                ('passport_issued_by', models.CharField(blank=True, max_length=200, verbose_name='Кем и когда выдан')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ManagementCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=300, verbose_name='Название компании')),
                ('subject_rf', models.CharField(blank=True, max_length=200, verbose_name='Субъект РФ')),
                ('full_name', models.CharField(blank=True, max_length=200, verbose_name='Полное название')),
                ('name_employee', models.CharField(blank=True, max_length=200, verbose_name='ФИО директора')),
                ('inn', models.CharField(blank=True, max_length=200, verbose_name='ИНН')),
                ('ogrn', models.CharField(blank=True, max_length=200, verbose_name='ОГРН')),
                ('legal_address', models.CharField(blank=True, max_length=200, verbose_name='Юредический адрес')),
                ('actual_address', models.CharField(blank=True, max_length=200, verbose_name='Фактический адрес')),
                ('phone', models.CharField(blank=True, max_length=200, verbose_name='Телефон')),
                ('email', models.CharField(blank=True, max_length=200, verbose_name='Электронная почта')),
                ('site', models.CharField(blank=True, max_length=200, verbose_name='Сайт')),
            ],
            options={
                'db_table': 'management_company',
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название улицы')),
            ],
        ),
        migrations.CreateModel(
            name='Territory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('management_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='territories', to='main.ManagementCompany', verbose_name='Управляющая компания')),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(verbose_name='Номер дома')),
                ('street', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='houses', to='main.Street', verbose_name='Улица')),
                ('territory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='houses', to='main.Territory', verbose_name='Территория')),
            ],
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(verbose_name='Номер квартиры')),
                ('entrance', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Подъезд')),
                ('floor', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Этаж')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flats', to='main.House', verbose_name='Дом')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Текст обращения')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Время создания')),
                ('management_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.ManagementCompany')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Квартирант')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='flat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='main.Flat', verbose_name='Квартира'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
