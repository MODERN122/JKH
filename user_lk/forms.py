from django import forms

from main.models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'body',
            'image1',
            'image2',
            'image3',
        ]