from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from embed_video.fields import EmbedVideoField

status_selection = (
    ('Published', 'Published'),
    ('Draft', 'Draft'),
)


class category(models.Model):
    title = models.CharField(_('Title'), max_length=500, unique=True)
    slug = models.SlugField(_('Slug'), max_length=500, unique=True, allow_unicode=True)
    short_description = models.CharField(_('Page Short Description'), max_length=500, null=True)
    image = models.ImageField(_('Image'), upload_to='services/%Y/%m/%d/')
    status = models.CharField(_('Status'), max_length=10, choices=status_selection, default='Published')
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False)

    class Meta:
        verbose_name = 'List Category'
        verbose_name_plural = 'List Categories'
        db_table = 'service-category-list'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) # set the slug explicitly
        super(category, self).save(*args, **kwargs) # call Django's save()


class service(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    title = models.CharField(_('Page Title'), max_length=500)
    description = RichTextUploadingField(_('Description'))
    video_url = EmbedVideoField(null=True, blank=True)
    status = models.CharField(_('Status'), max_length=10, choices=status_selection, default='Published')
    meta_title = models.CharField(_('Meta Title'), max_length=60, null=True, blank=True)
    meta_description = models.CharField(_('Meta Description'), max_length=160, null=True, blank=True)
    meta_keywords = models.CharField(_('Meta Keywords'), max_length=200, null=True, blank=True)
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False)

    class Meta:
        verbose_name = 'List Services'
        verbose_name_plural = 'List Services'
        db_table = 'service-list'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('serviceList')