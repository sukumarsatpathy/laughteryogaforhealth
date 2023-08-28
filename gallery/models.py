from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from django.urls import reverse
from embed_video.fields import EmbedVideoField


status_selection = (
    ('Published', 'Published'),
    ('Draft', 'Draft'),
)


class imgCategory(models.Model):
    title = models.CharField(_('Title'), max_length=500, unique=True, null=True)
    slug = models.SlugField(_('Slug'), max_length=500, unique=True, null=True)
    image = models.ImageField(_('Image'), upload_to='gallery/category/%Y/%m/%d/', null=True, help_text='Image Size: 500x500')
    status = models.CharField(_('Status'), max_length=10, choices=status_selection, default='Published')
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False)

    class Meta:
        verbose_name = 'List Photo Category'
        verbose_name_plural = 'List Photo Categories'
        db_table = 'picture-list'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pcatList')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) # set the slug explicitly
        super(imgCategory, self).save(*args, **kwargs) # call Django's save()


class imgGallery(models.Model):
    category = models.ForeignKey(imgCategory, on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=500, null=True)
    image = models.ImageField(_('Image'), upload_to='gallery/image/%Y/%m/%d/', null=True)
    status = models.CharField(_('Status'), max_length=10, choices=status_selection, default='Published')
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False)

    class Meta:
        verbose_name = 'List Photos'
        verbose_name_plural = 'List Photos'
        db_table = 'image-list'

    def __str__(self):
        return self.title


class vdoCategory(models.Model):
    title = models.CharField(_('Title'), max_length=500, unique=True, null=True)
    slug = models.SlugField(_('Slug'), max_length=500, unique=True, null=True)
    image = models.ImageField(_('Image'), upload_to='gallery/video/%Y/%m/%d/', null=True, help_text='Image Size: 500x500')
    status = models.CharField(_('Status'), max_length=10, choices=status_selection, default='Published')
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False)

    class Meta:
        verbose_name = 'List Video Category'
        verbose_name_plural = 'List Video Categories'
        db_table = 'video-list'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) # set the slug explicitly
        super(vdoCategory, self).save(*args, **kwargs) # call Django's save()


class vdoGallery(models.Model):
    category = models.ForeignKey(vdoCategory, on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=500, null=True)
    video_url = EmbedVideoField(null=True)
    status = models.CharField(_('Status'), max_length=10, choices=status_selection, default='Published')
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False)

    class Meta:
        verbose_name = 'List Videos'
        verbose_name_plural = 'List Videos'
        db_table = 'video-url-list'

    def __str__(self):
        return self.title