from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

status_selection = (
    ('Published', 'Published'),
    ('Draft', 'Draft'),
)


class Testimonial(models.Model):
    fullName = models.CharField(_('Full Name'), max_length=500, unique=True)
    designation = models.CharField(_('Designation'), max_length=500)
    message = RichTextUploadingField(_('Message'))
    image = models.ImageField(_('Image'), upload_to='testimonial/%Y/%m/%d/', null=True)
    status = models.CharField(_('Status'), max_length=10, choices=status_selection, default='Published')
    submission_date = models.DateTimeField(_('Submission Date'), auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        db_table = 'testimonials_list'

    def __str__(self):
        return self.fullName