# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import os


def data_file_store(instance, filename):
    now = datetime.now()
    return os.path.join('data', 'files', now.strftime("%Y_%m_%d_%H%M%S"), filename)


class GenericFile(models.Model):
    data_file = models.FileField(upload_to=data_file_store, blank=False, null=False, max_length=500)
    original_filename = models.CharField(max_length=500, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):  # __unicode__ on Python 2
        return self.original_filename
