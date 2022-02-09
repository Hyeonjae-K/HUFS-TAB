from django import forms

from tab.models import Post, Application


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['subject', 'content']


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'studentnumber', 'phonenumber', 'file_path']
