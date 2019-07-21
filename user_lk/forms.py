from django import forms

from main.models import Application, ApplicationComment, Vote, VoteComment, User


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'body',
            'image1',
            'image2',
            'image3',
        ]


class ApplicationCommentForm(forms.ModelForm):
    class Meta:
        model = ApplicationComment
        fields = [
            'context'
        ]


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = [
            'title',
            'context',
            'image1',
            'image2',
            'image3',
            'end_date',
        ]


class VoteCommentForm(forms.ModelForm):
    class Meta:
        model = VoteComment
        fields = [
            'context'
        ]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
            'phone',
        ]