# blog/forms.py

from django import forms
from .models import Blog
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = ['title', 'cover', 'author', 'content']
