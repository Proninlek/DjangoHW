import logging

from django.shortcuts import render
from django.http import HttpResponse


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Log')
    return render(request, 'index.html')

def about(request):
    logger.info('Log')
    return render(request, 'about.html')
