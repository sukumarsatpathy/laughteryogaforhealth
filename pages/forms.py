from django import forms
from .models import adBlock, lyJournals, banner, bannerImage, ContactPage, Copyright, webSettings, TermPages


class adBlockForm(forms.ModelForm):
    class Meta:
        model = adBlock
        fields = ('type','title', 'image', 'url', 'status')

    def __init__(self, *args, **kwargs):
        super(adBlockForm, self).__init__(*args, **kwargs)
        self.fields['type'].widget.attrs['class'] = 'form-select'
        self.fields['status'].widget.attrs['class'] = 'form-select'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = 'Provide Details'


class journalForm(forms.ModelForm):
    class Meta:
        model = lyJournals
        fields = ('title', 'image', 'status')

    def __init__(self, *args, **kwargs):
        super(journalForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs['class'] = 'form-select'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = 'Provide Details'


class bannerForm(forms.ModelForm):
    class Meta:
        model = banner
        fields = ('title', 'txt1', 'txt2', 'description', 'btn_txt', 'btn_url', 'status')

    def __init__(self, *args, **kwargs):
        super(bannerForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs['class'] = 'form-select'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = 'Provide Details'


class bannerImageForm(forms.ModelForm):
    class Meta:
        model = bannerImage
        fields = ('banner', 'image', 'status')

    def __init__(self, *args, **kwargs):
        super(bannerImageForm, self).__init__(*args, **kwargs)
        self.fields['banner'].widget.attrs['class'] = 'form-select'
        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-select'
        # for field in self.fields:
        #     self.fields[field].widget.attrs['class'] = 'form-control'
        #     self.fields[field].widget.attrs['placeholder'] = 'Provide Details'


class ContactPageForm(forms.ModelForm):
    class Meta:
        model = ContactPage
        fields = ('title', 'address', 'phone', 'email', 'map_url')

    def __init__(self, *args, **kwargs):
        super(ContactPageForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = 'Provide Details'


class CopyrightPageForm(forms.ModelForm):
    class Meta:
        model = Copyright
        fields = ('symbol', 'startYear', 'title')

    def __init__(self, *args, **kwargs):
        super(CopyrightPageForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['placeholder'] = 'Provide Details'


class webSettingsForm(forms.ModelForm):
    class Meta:
        model = webSettings
        fields = ('title', 'slogan', 'logo', 'logo_white', 'logo_round', 'fb_url', 'tw_url', 'ig_url', 'li_url', 'keywords', 'description')

    def __init__(self, *args, **kwargs):
        super(webSettingsForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['slogan'].widget.attrs['class'] = 'form-control'
        self.fields['fb_url'].widget.attrs['class'] = 'form-control'
        self.fields['tw_url'].widget.attrs['class'] = 'form-control'
        self.fields['ig_url'].widget.attrs['class'] = 'form-control'
        self.fields['li_url'].widget.attrs['class'] = 'form-control'
        self.fields['keywords'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'


class termPageForm(forms.ModelForm):
    class Meta:
        model = TermPages
        fields = ('title', 'description', 'status')

    def __init__(self, *args, **kwargs):
        super(termPageForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-select'