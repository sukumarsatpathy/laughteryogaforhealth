from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from embed_video.fields import EmbedVideoField


status_selection = (
    ('Published', 'Published'),
    ('Draft', 'Draft'),
)


class Event(models.Model):
    title = models.CharField(_('Title'), max_length=500, unique=True)
    slug = models.SlugField(_('Slug'), max_length=500, unique=True)
    description = RichTextUploadingField(_('Description'))
    organiser = models.CharField(_('Organiser Name'), max_length=200)
    email = models.EmailField(_('Email'), max_length=200)
    contact_no = models.CharField(_('Contact No'), max_length=15, blank=True, null=True)
    location = models.CharField(_('Location'), max_length=200)
    start_date = models.DateTimeField(_('Start Date'), editable=True)
    end_date = models.DateTimeField(_('End Date'), editable=True)
    image = models.ImageField(_('Event Image 1'), upload_to='events/%Y/%m/%d/', null=True)
    video = EmbedVideoField(_('Event Video 1'), blank=True, null=True)
    views = models.IntegerField(_('Views'), default=0)
    status = models.CharField(_('Status'), max_length=10, choices=status_selection, default='Published')
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False)

    meta_title = models.CharField(_('Meta Title'), max_length=60, null=True, blank=True)
    meta_description = models.CharField(_('Meta Description'), max_length=160, null=True, blank=True)
    meta_keywords = models.CharField(_('Meta Keywords'), max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        db_table = 'events'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('listEvents')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) # set the slug explicitly
        super(Event, self).save(*args, **kwargs) # call Django's save()