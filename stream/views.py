from django.shortcuts import get_object_or_404, render

from .models import Channel


def index(request):
  return render(request, 'stream/index.html')

def new(request):
  return render(request, 'stream/new.html')

def test(request):
  channel = get_object_or_404(Channel, name='mic_feedback')
  if not channel.recently_updated():
    channel.update()
  return render(request, 'stream/test.html', {'channel': channel})
