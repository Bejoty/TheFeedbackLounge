from django.shortcuts import get_object_or_404, render

from .models import Channel
from zinnia.models import Entry


def index(request):
    channel = get_object_or_404(Channel, name='mic_feedback')
    if not channel.recently_updated():
        channel.update()
    latest_news = Entry.objects.order_by('-creation_date')[:5]
    return render(request, 'stream/index.html', {'channel': channel, 'latest_news': latest_news})

def new(request):
    return render(request, 'stream/new.html')

def old(request):
    return render(request, 'stream/old.html')

def test(request):
    channel = get_object_or_404(Channel, name='mic_feedback')
    if not channel.recently_updated():
        channel.update()
    return render(request, 'stream/test.html', {'channel': channel})
