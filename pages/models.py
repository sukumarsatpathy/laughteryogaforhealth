from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from accounts.models import Account


adBlock_type = (
    ('Home', 'Home'),
    ('General', 'General'),
)

status_selection = (
    ('Published', 'Published'),
    ('Draft', 'Draft'),
)


class adBlock(models.Model):
    type = models.CharField(_('Type'), max_length=10, choices=adBlock_type, null=True)
    title = models.CharField(_('Title'), max_length=500, unique=True, null=True)
    image = models.ImageField(_('Image'), upload_to='adBlock/%Y/%m/%d/', null=True)
    url = models.URLField('URL', null=True, blank=True)
    status = models.CharField(_('Status'), max_length=10, choices=status_selection, default='Published')
    submission_date = models.DateTimeField(_('Submission Date'), auto_now_add=True, editable=False)

    class Meta:
        verbose_name = 'adBlock'
        verbose_name_plural = 'adBlocks'
        db_table = 'adBlock-list'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('adblockList')


class lyJournals(models.Model):
    title = models.CharField(_('Title'), max_length=500, unique=True, null=True)
    image = models.ImageField(_('Image'), upload_to='journals/%Y/%m/%d/', null=True)
    status = models.CharField(_('Status'), max_length=10, choices=status_selection, default='Published')
    submission_date = models.DateTimeField(_('Submission Date'), auto_now_add=True, editable=False)

    class Meta:
        verbose_name = 'Journal'
        verbose_name_plural = 'Journals'
        db_table = 'journal-list'

    def __str__(self):
        return self.title


class banner(models.Model):
    title = models.CharField(_('Title'), max_length=500, unique=True, null=True)
    txt1 = models.CharField(_('Small Text 1'), max_length=500, unique=True, null=True)
    txt2 = models.CharField(_('Small Text 2'), max_length=500, unique=True, null=True)
    description = models.CharField(_('Description'), max_length=500, null=True, blank=True)
    btn_txt = models.CharField(_('Button Text'), max_length=50, null=True)
    btn_url = models.URLField(_('Button URL'), max_length=500, null=True)
    status = models.CharField(_('Status'), max_length=10, choices=status_selection, default='Published')
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banner'
        db_table = 'banner-list'

    def __str__(self):
        return self.title


class bannerImage(models.Model):
    banner = models.ForeignKey(banner, on_delete=models.CASCADE)
    image = models.ImageField(_('Image'), upload_to='banner/%Y/%m/%d/', null=True)
    status = models.CharField(_('Status'), max_length=10, choices=status_selection, default='Published')
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Banner Image'
        verbose_name_plural = 'Banner Image'
        db_table = 'banner-image-list'

    def __str__(self):
        return self.banner.title


class ContactPage(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    title = models.CharField(_('Title'), max_length=50, null=True)
    address = models.CharField(_('Address'), max_length=500, null=True)
    phone = models.CharField(_('Phone'), max_length=500, null=True)
    email = models.EmailField(_('Email'), null=True)
    map_url = models.TextField(_('Map URL'), null=True)
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Contact Page'
        verbose_name_plural = 'Contact Page'
        db_table = 'contact-page-list'

    def __str__(self):
        return self.title


class Copyright(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    symbol = models.CharField(_('Symbol'), max_length=10, null=True)
    startYear = models.CharField(_('Start Year'), max_length=6, null=True)
    title = models.CharField(_('Copyright Text'), max_length=50, null=True)
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Copyright'
        verbose_name_plural = 'Copyright'
        db_table = 'copyright-list'

    def __str__(self):
        return self.title


class webSettings(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    title = models.CharField(_('Title'), max_length=100, null=True)
    slogan = models.CharField(_('Slogan'), max_length=100, null=True)
    logo = models.ImageField(_('Logo'), upload_to='settings/logo/%Y/%m/%d/', null=True)
    logo_white = models.ImageField(_('White Logo'), upload_to='settings/logo/%Y/%m/%d/', null=True)
    logo_round = models.ImageField(_('Round Logo'), upload_to='settings/logo/%Y/%m/%d/', null=True)
    favicon = models.ImageField(_('Round Logo'), upload_to='settings/logo/%Y/%m/%d/', null=True)
    fb_url = models.URLField(_('Facebook'), blank=True, max_length=100, null=True)
    tw_url = models.URLField(_('Twitter'), blank=True, max_length=100, null=True)
    ig_url = models.URLField(_('Instagram'), blank=True, max_length=100, null=True)
    li_url = models.URLField(_('Instagram'), blank=True, max_length=100, null=True)
    keywords = models.CharField(_('Keywords'), max_length=500, null=True, blank=True)
    description = models.TextField(_('Description'), max_length=500, null=True, blank=True)
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Front-end Settings'
        verbose_name_plural = 'Front-end Settings'
        db_table = 'front-end-settings-list'

    def __str__(self):
        return self.title


class TermPages(models.Model):
    title = models.CharField(_('Title'), max_length=100, null=True)
    slug = models.SlugField(_('Slug'), max_length=100, null=True)
    description = RichTextUploadingField(_('Description'), null=True)
    status = models.CharField(_('Status'), max_length=100, choices=status_selection, default='Published')
    updated_on = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Term Page'
        verbose_name_plural = 'Term Page'
        db_table = 'term-page-list'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ListTermPage')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TermPages, self).save(*args, **kwargs)


class pageCategory(models.Model):
    title = models.CharField(_('Title'), max_length=500, unique=True)
    slug = models.SlugField(_('Slug'), max_length=500, unique=True, allow_unicode=True)
    short_description = models.CharField(_('Page Short Description'), max_length=500, null=True)
    status = models.CharField(_('Status'), max_length=10, choices=status_selection, default='Published')
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False)

    class Meta:
        verbose_name = 'List About Page Category'
        verbose_name_plural = 'List About Page Categories'
        db_table = 'page-category-list'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) # set the slug explicitly
        super(pageCategory, self).save(*args, **kwargs) # call Django's save()


class AboutPage(models.Model):
    category = models.ForeignKey(pageCategory, on_delete=models.CASCADE, null=True)
    title = models.CharField(_('Page Title'), max_length=500)
    description = RichTextUploadingField(_('Description'))
    status = models.CharField(_('Status'), max_length=100, choices=status_selection, default='Published')
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False)
    meta_title = models.CharField(_('Meta Title'), max_length=60, null=True, blank=True)
    meta_description = models.CharField(_('Meta Description'), max_length=160, null=True, blank=True)
    meta_keywords = models.CharField(_('Meta Keywords'), max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'List About Page'
        verbose_name_plural = 'List About Page'
        db_table = 'about-page-list'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(AboutPage, self).save(*args, **kwargs)
