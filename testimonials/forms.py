from django import forms
from .models import Testimonial
from ckeditor.widgets import CKEditorWidget


class TestimonialForm(forms.ModelForm):
    message = forms.CharField(widget=CKEditorWidget(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Testimonial
        fields = ('fullName', 'designation', 'message', 'image', 'status')

    def __init__(self, *args, **kwargs):
        super(TestimonialForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs['class'] = 'form-select'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = 'Provide Details'