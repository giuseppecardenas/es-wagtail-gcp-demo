import os
import sys
import six
from django.urls import get_callable
from django.conf import settings
from django.shortcuts import render, redirect

import logging
logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'static_generation/admin/index.html', {})

def generate(request):

    for view_str in settings.BAKERY_VIEWS:
        logger.debug("Building %s" % view_str)
        view = get_callable(view_str)
        view().build_method()

    return render(request, 'static_generation/admin/generation_started.html', {})