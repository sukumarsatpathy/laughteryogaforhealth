from django import forms
from .models import category, service


class categoryForm(forms.ModelForm):
    class Meta:
        model = category
        fields = ('title', 'short_description', 'image', 'status')

    def __init__(self, *args, **kwargs):
        super(categoryForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['short_description'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-select'


class serviceForm(forms.ModelForm):
    class Meta:
        model = service
        fields = ('category', 'title', 'description', 'video_url', 'meta_title', 'meta_description', 'meta_keywords', 'status')

    def __init__(self, *args, **kwargs):
        super(serviceForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs['class'] = 'form-select'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['video_url'].widget.attrs['class'] = 'form-control'
        self.fields['meta_title'].widget.attrs['class'] = 'form-control'
        self.fields['meta_description'].widget.attrs['class'] = 'form-control'
        self.fields['meta_keywords'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-select'