from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AdvertisingsConfig(AppConfig):
    name = 'advertising'
    verbose_name = _('Ads Management System')
