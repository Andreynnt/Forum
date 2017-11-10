# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView

from django.http import HttpResponse


class AboutView(TemplateView):
    template_name = "index.html"

# Create your views here.
