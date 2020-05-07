from django.db import models
from django.forms.models import model_to_dict
from django.utils.translation import ugettext_lazy as _
from model_utils.fields import AutoCreatedField, AutoLastModifiedField


class AbstractBaseModel(models.Model):
    created_at = AutoCreatedField(verbose_name="criado em")
    updated_at = AutoLastModifiedField(verbose_name="atualizado em")

    class Meta:
        abstract = True

    def serialize_to_dict(self):
        return model_to_dict(self, fields=[field.name for field in self._meta.fields])