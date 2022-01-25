from django import forms

from tab.models import Contents


class ContentsForm(forms.ModelForm):
    class Meta:
        model = Contents
        fields = ['subject', 'content']
