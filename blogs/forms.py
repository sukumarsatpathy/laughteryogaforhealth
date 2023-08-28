from django import forms
from .models import Blog
from ckeditor.widgets import CKEditorWidget


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title','description', 'image', 'status', 'meta_title', 'meta_description', 'meta_keywords')

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['meta_title'].widget.attrs['class'] = 'form-control'
        self.fields['meta_description'].widget.attrs['class'] = 'form-control'
        self.fields['meta_keywords'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-select'
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = 'Provide Detail'