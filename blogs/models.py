from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify


status_selection = (
    ('Published', 'Published'),
    ('Draft', 'Draft'),
)


class Blog(models.Model):
    title = models.CharField(_('Title'), max_length=500, unique=True)
    slug = models.SlugField(_('Slug'), max_length=500, unique=True, allow_unicode=True)
    description = RichTextUploadingField(_('Message'))
    image = models.ImageField(_('Image'), upload_to='blog/%Y/%m/%d/', null=True)
    status = models.CharField(_('Status'), max_length=10, choices=status_selection, default='Published')
    views = models.IntegerField(_('Views'), default=0)
    submission_date = models.DateTimeField(_('Submission Date'), auto_now_add=True, editable=False)
    meta_title = models.CharField(_('Meta Title'), max_length=60, null=True, blank=True)
    meta_description = models.CharField(_('Meta Description'), max_length=160, null=True, blank=True)
    meta_keywords = models.CharField(_('Meta Keywords'), max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        db_table = 'blog-list'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) # set the slug explicitly
        super(Blog, self).save(*args, **kwargs) # call Django's save()

    def get_absolute_url(self):
        return reverse('listBlogs')


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    fullName = models.CharField(_('Full Name'), max_length=500)
    email = models.EmailField(_('Email'), max_length=500)
    message = models.TextField(_('Message'))
    ip = models.CharField(_('IP Address'), max_length=20, blank=True)
    status = models.BooleanField(_('Status'), default=True)
    submission_date = models.DateTimeField(_('Submission Date'), auto_now_add=True, editable=False)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        db_table = 'comment-list'

    def __str__(self):
        return self.fullName