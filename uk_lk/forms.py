from django import forms

from main.models import User, ActiveWork, ManagementCompany


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'temp_password',
            'fullname',
            'flat',
            'passport_id',
            'passport_issued_by',
            'phone',
            'email',
        ]


class ActiveWorkForm(forms.ModelForm):
    class Meta:
        model = ActiveWork
        fields = [
            'description',
            'start_date',
            'end_date',
        ]


class ManagementCompanyForm(forms.ModelForm):
    class Meta:
        model = ManagementCompany
        exclude = [
            'pk',
        ]