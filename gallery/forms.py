from django import forms
from .models import imgCategory, imgGallery, vdoCategory, vdoGallery
from ckeditor.widgets import CKEditorWidget


class imgCategoryForm(forms.ModelForm):
    class Meta:
        model = imgCategory
        fields = ('title', 'image', 'status')

    def __init__(self, *args, **kwargs):
        super(imgCategoryForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs['class'] = 'form-select'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = 'Provide Details'


class imgGalleryForm(forms.ModelForm):
    class Meta:
        model = imgGallery
        fields = ('category', 'title', 'image', 'status')

    def __init__(self, *args, **kwargs):
        super(imgGalleryForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs['class'] = 'form-select'
        self.fields['status'].widget.attrs['class'] = 'form-select'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = 'Provide Details'


class vdoCategoryForm(forms.ModelForm):
    class Meta:
        model = vdoCategory
        fields = ('title', 'image', 'status')

    def __init__(self, *args, **kwargs):
        super(vdoCategoryForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs['class'] = 'form-select'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = 'Provide Details'


class vdoGalleryForm(forms.ModelForm):
    class Meta:
        model = vdoGallery
        fields = ('category', 'title', 'video_url', 'status')

    def __init__(self, *args, **kwargs):
        super(vdoGalleryForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs['class'] = 'form-select'
        self.fields['status'].widget.attrs['class'] = 'form-select'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = 'Provide Details'