# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
import os

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __str__(self):  # __unicode__ on Python 2
        return self.email


def data_file_store(instance, filename):
    now = datetime.now()
    return os.path.join('data', 'files', now.strftime("%Y_%m_%d_%H%M%S"), filename)


class GenericFile(models.Model):
    """ Model for managing generic files. Files can either be saved as symlink or copied to the data file store
    based on what has been set in the settings file MEDIA_ROOT parameter
    """
    data_file = models.FileField(upload_to=data_file_store, blank=True, null=True, max_length=500)
    original_filename = models.CharField(max_length=500, null=False, blank=False,
                                         help_text='If a file with the same filename is uploaded at the same time'
                                                   'a duplicate is saved with a unique name. This field is used'
                                                   'to keep track of the original name')
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='The user who uploaded the file', null=True,
                             blank=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.original_filename


class TrackTasks(models.Model):
    """ Model for tracking Celery tasks to users. If django-db is being used for the Celery backend then the
    taskid is already stored in the Django database. However this will not record the user, also this database table
    will be missing if redis or rabbitmq is used for the backend.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='The user who uploaded the file', null=True,
                             blank=True)
    taskid = models.CharField(max_length=500, null=False, blank=False)

    state = models.CharField(max_length=500, null=True, blank=True)

    name = models.CharField(max_length=500, null=True, blank=True)

    result = models.URLField(null=True, blank=True)

    def __str__(self):  # __unicode__ on Python 2
        return '{}'.format(self.name)

