import os

from django.db import models
from django.utils.translation import gettext_lazy as _

from .validators import valid_extension


class Advertising(models.Model):

    id_advertising = models.CharField(_("ID"), unique=True, max_length=10)
    name = models.CharField(_("Name"), max_length=80)
    timeout = models.PositiveIntegerField(_("Timeout"),
        default=0, help_text=_("The input value is in seconds")
    )

    class Meta(object):
        ordering = ['id_advertising']
        verbose_name = _("Advertising")
        verbose_name_plural = _("Advertising")

    def __str__(self):
        return self.name


class ImageAdvertising(models.Model):

    def generate_path(instance, filename):
        folder = "campaign_" + str(instance.advertising.id)
        return os.path.join("campaigns", folder, filename)

    advertising = models.ForeignKey(Advertising, verbose_name=_("Advertising"),
                                    on_delete=models.CASCADE, related_name='images')
    title = models.CharField(_("Title"), max_length=80)
    url = models.URLField(_("Url"), max_length=450)
    photo = models.FileField(_("Photo"), blank=False, null=False,
                             upload_to=generate_path,
                             validators=[valid_extension])

    class Meta(object):
        verbose_name = _("Image Advertisement")
        verbose_name_plural = _("Image Advertisements")

    def __str__(self):
        return self.advertising.name
