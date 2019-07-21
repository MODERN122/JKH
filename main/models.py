from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class ManagementCompany(models.Model):
    company_name = models.CharField('Название компании', max_length=300)
    subject_rf = models.CharField('Субъект РФ', max_length=200, blank=True)
    full_name = models.CharField('Полное название', max_length=200, blank=True)
    name_employee = models.CharField('ФИО директора', max_length=200, blank=True)
    inn = models.CharField('ИНН', max_length=200, blank=True)
    ogrn = models.CharField('ОГРН', max_length=200, blank=True)
    legal_address = models.CharField('Юредический адрес', max_length=200, blank=True)
    actual_address = models.CharField('Фактический адрес', max_length=200, blank=True)
    phone = models.CharField('Телефон', max_length=200, blank=True)
    email = models.CharField('Электронная почта', max_length=200, blank=True)
    site = models.CharField('Сайт', max_length=200, blank=True)

    def __str__(self):
        return self.company_name

    class Meta:
        db_table = 'management_company'


class Territory(models.Model):
    name = models.CharField('Название территории', max_length=100, blank=True)
    housing_department = models.CharField('ЖЭК', max_length=100, blank=True)
    management_company = models.ForeignKey(ManagementCompany, related_name='territories', verbose_name='Управляющая компания',on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name if self.name else str(self.pk)


class Street(models.Model):
    name = models.CharField('Название улицы', max_length=100)

    def __str__(self):
        return self.name


class House(models.Model):
    territory = models.ForeignKey(Territory, related_name='houses', verbose_name='Территория', on_delete=models.SET_NULL, blank=True, null=True)
    number = models.PositiveSmallIntegerField('Номер дома')
    street = models.ForeignKey(Street, related_name='houses', verbose_name='Улица', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'ул. {self.street.name}, д. {self.number}'


class Flat(models.Model):
    house = models.ForeignKey(House, related_name='flats', verbose_name='Дом', on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField('Номер квартиры')
    entrance = models.PositiveSmallIntegerField('Подъезд', blank=True, null=True)
    floor = models.PositiveSmallIntegerField('Этаж', blank=True, null=True)

    def __str__(self):
        return f'{str(self.house)}, кв. {self.number}'


class User(AbstractUser):
    fullname = models.CharField('ФИО', max_length=200)
    flat = models.ForeignKey(Flat, related_name='users', verbose_name='Квартира', on_delete=models.SET_NULL, blank=True, null=True)
    passport_id = models.CharField('Номер паспорта', max_length=10, blank=True)
    passport_issued_by = models.CharField('Кем и когда выдан', max_length=200, blank=True)
    mc_manager = models.ForeignKey(ManagementCompany, related_name='managers', verbose_name='Управляемая УК', blank=True, null=True, on_delete=models.SET_NULL)
    phone = models.CharField('Телефон', max_length=20, blank=True)
    create_date = models.DateTimeField('Время создания', auto_now_add=True)
    temp_password = models.CharField('Временный пароль', max_length=128, blank=True)

    def get_absolute_url(self):
        return reverse('edit_user', kwargs={'pk': self.pk})


class Status(models.Model):
    name = models.CharField('Статус', max_length=100)
    description = models.CharField('Описание', max_length=200, blank=True)

    def __str__(self):
        return self.name


class Application(models.Model):
    body = models.TextField('Текст обращения')
    status = models.ForeignKey(Status, related_name='applications', verbose_name='Статус', on_delete=models.CASCADE)  # TODO: Продумать удаление
    date = models.DateTimeField('Время создания', auto_now=True)
    user = models.ForeignKey(User, related_name='applications', on_delete=models.CASCADE, verbose_name='Квартирант')
    territory = models.ForeignKey(Territory, related_name='applications', on_delete=models.SET_NULL, blank=True, null=True)
    image1 = models.ImageField(upload_to='applications', blank=True)
    image2 = models.ImageField(upload_to='applications', blank=True)
    image3 = models.ImageField(upload_to='applications', blank=True)

    def get_absolute_url(self):
        return reverse('application_page', kwargs={'pk': self.pk})

    def __str__(self):
        return self.body


class ApplicationComment(models.Model):
    application = models.ForeignKey(Application, related_name='comments', verbose_name='Заявка', on_delete=models.CASCADE)
    context = models.TextField('Комментарий')
    date = models.DateTimeField('Время создания', auto_now=True)
    user = models.ForeignKey(User, related_name='application_comments', verbose_name='Пользователь', on_delete=models.CASCADE)


class Vote(models.Model):
    title = models.CharField('Название', max_length=200)
    context = models.TextField('Вопрос на голосование')
    image1 = models.ImageField(upload_to='Votes', blank=True)
    image2 = models.ImageField(upload_to='Votes', blank=True)
    image3 = models.ImageField(upload_to='Votes', blank=True)
    user = models.ForeignKey(User, related_name='votes', verbose_name='Пользователь', on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateTimeField('Время создания', auto_now=True)
    end_date = models.DateTimeField('Время окончания сбора голосов')
    agree = models.ManyToManyField(User, related_name='agree_votes', verbose_name='Согласные пользователи')
    disagree = models.ManyToManyField(User, related_name='disagree_votes', verbose_name='Несогласные пользователи')
    is_moderated = models.BooleanField('Отмодерировано', default=False)
    # management_company = models.ForeignKey(ManagementCompany, related_name='Votes', verbose_name='УК', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('vote_page', kwargs={'pk': self.pk})


class VoteComment(models.Model):
    context = models.TextField('Комментарий')
    date = models.DateTimeField("Время создания", auto_now=True)
    user = models.ForeignKey(User, related_name='vote_comments', verbose_name='Пользователь', on_delete=models.CASCADE)
    vote = models.ForeignKey(Vote, related_name='comments', verbose_name='Голосование', on_delete=models.CASCADE)


class ActiveWork(models.Model):
    description = models.TextField('Описание')
    start_date = models.DateTimeField('Время начала')
    end_date = models.DateTimeField('Время окончания')
    management_company = models.ForeignKey(ManagementCompany, related_name='active_works', verbose_name='УК', on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('active_work', kwargs={'pk': self.pk})

