# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import CreateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
import os
import copy

from django.http import JsonResponse
from celery.result import AsyncResult

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin, MultiTableMixin

from gfiles.models import GenericFile, TrackTasks
from gfiles.forms import GFileForm
from django.shortcuts import render
from django.views.generic import View

from gfiles.filter import GFileFilter, TrackTasksFilter
from gfiles.tables import GFileTableWithCheck, TrackTasksTable

from django_tables2.export.views import ExportMixin
from django.urls import reverse_lazy


class GFileCreateView(LoginRequiredMixin, CreateView):
    """ Class to create a save a generic file using the GenericFile model.

    Inherits the CreateView class and uses the LoginRequiredMixin
    """
    model = GenericFile
    success_msg = "File uploaded"
    success_url = reverse_lazy('success')
    form_class = GFileForm
    template_name = 'gfiles/gfile_form.html'

    def update_form(self, form):
        ofn = self.request.FILES['data_file'].name
        form.instance.original_filename = ofn
        form.instance.user = self.request.user
        return form

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        form = self.update_form(form)
        return super(GFileCreateView, self).form_valid(form)


class GFileListView(ExportMixin, SingleTableMixin, FilterView):
    """ Class to view a table and filter all of the currently saved GenericFiles

    Inherits the FilterView class and uses the SingleTableMixin for viewing the django-tables2 table and
    uses the ExportMixin so that the table can be exported as a csv file
    """
    table_class = GFileTableWithCheck
    model = GenericFile
    template_name = 'gfiles/gfile_summary.html'
    filterset_class = GFileFilter


class TrackTasksListView(LoginRequiredMixin, SingleTableMixin, FilterView):
    """ Class to view a table and filter all of the currently saved GenericFiles

    Inherits the FilterView class and uses the SingleTableMixin for viewing the django-tables2 table and
    uses the ExportMixin so that the table can be exported as a csv file
    """
    table_class = TrackTasksTable
    model = TrackTasks
    template_name = 'gfiles/tracktask_summary.html'
    filterset_class = TrackTasksFilter


class TrackTasksProgressView(LoginRequiredMixin, View):
    """
    """
    def get(self, request, *args, **kwargs):

        tt = TrackTasks.objects.get(pk=self.kwargs['pk'])

        request.session['result'] = tt.taskid

        return render(request, 'gfiles/status.html', {'s': 0, 'progress': 0})



def async_task_progress(id):
    # https://blog.miguelgrinberg.com/post/using-celery-with-flask
    task = AsyncResult(id)

    # Task has finished and information has been remove (i think)
    try:
        print(task.state)
    except KeyError as e:
        print(e)
        print(task.info)
        response = {
            'state': 'REMOVED',
            'current': 0,
            'total': 0,
            'status': '',
        }
        return JsonResponse(response)

    info = copy.deepcopy(task.info)  # incase things change or rabbit/redis deletes message

    if task.state == 'PENDING':
        print('pending')
        # job did not start yet
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        print('processing')
        response = {
            'state': task.state,
            'current': info['current'],
            'total': info['total'],
            'status': info['status'],
        }
        # if 'result' in info:
        #     response['result'] = info
    else:
        # something went wrong in the background job
        response = {
            'state': task.state,
            'current': 0,
            'total': 0,
            'status': 'FAILURE (unknown)',
        }


    if response['state']=='FAILURE-KNOWN':
        response['state'] = 'FAILURE'


    if task.info:
        response['progress'] = (float(response['current']) / float(response['total'])) * 100.0
    else:
        response['progress'] = 0

    return response

def status_update(request):
    """ Updates for tracking status of long processes via celery
    """

    id = request.session['result']
    response = async_task_progress(id)

    return JsonResponse(response)


def index(request):
    """ basic index view
    """
    return render(request, 'gfiles/index.html')


def success(request):
    """ basic success view
    """
    return render(request, 'gfiles/success.html')