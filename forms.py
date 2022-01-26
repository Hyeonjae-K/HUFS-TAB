from django import forms

from tab.models import Contents, Applications


class ContentsForm(forms.ModelForm):
    class Meta:
        model = Contents
        fields = ['subject', 'content']


class ApplicationsForm(forms.ModelForm):
    class Meta:
        model = Applications
        fields = ['name', 'studentnumber', 'phonenumber', 'path']
