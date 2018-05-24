# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
import os


from django.http import JsonResponse
from celery.result import AsyncResult

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin, MultiTableMixin

from gfiles.models import GenericFile
from gfiles.forms import GFileForm
from django.shortcuts import render

from gfiles.filter import GFileFilter
from gfiles.tables import GFileTableWithCheck

from django_tables2.export.views import ExportMixin

class GFileCreateView(LoginRequiredMixin, CreateView):
    model = GenericFile
    success_msg = "Experimental metabolomics file uploaded"
    success_url = '/misa/success'
    # fields = '__all__'
    # fields = ['run', 'data_file']
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


class GFileListView(SingleTableMixin, FilterView):
    table_class = GFileTableWithCheck
    model = GenericFile
    template_name = 'gfiles/gfile_summary.html'

    filterset_class = GFileFilter


def status_update(request):
    id = request.session['result']

    result = AsyncResult(id)

    status = result.status

    if status == 'FAILURE':
        progress = 0
    elif status == 'SUCCESS':
        progress = 100
    elif result.info:
        progress = (float(result.info['current'])/float(result.info['total']))*100.0
    else:
        progress = 0

    return JsonResponse({'s': status, 'progress':progress, 'info':str(result.info)})
