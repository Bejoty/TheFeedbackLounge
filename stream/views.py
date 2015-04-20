from django.shortcuts import render
from django.http import Http404

from .models import Channel


def index(request):
  return render(request, 'stream/index.html')

def new(request):
  return render(request, 'stream/new.html')

def test(request):
  try:
    channel = Channel.objects.get(pk=1)
  except Channel.DoesNotExist:
    raise Http404("Channel information missing")
  return render(request, 'stream/test.html', {'channel': channel})
