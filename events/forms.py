from django import forms
from .models import Event
from ckeditor.widgets import CKEditorWidget


class DateInput(forms.DateInput):
    input_type = 'date'


class EventForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Event
        fields = ('title', 'description', 'organiser', 'email', 'contact_no', 'location',
                  'start_date', 'end_date', 'image', 'video', 'status', 'meta_title', 'meta_description', 'meta_keywords')
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs['class'] = 'form-select'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = 'Provide Details'