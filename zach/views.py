from django.shortcuts import get_object_or_404, render

from stream.models import Channel
from zinnia.models import Entry


def index(request):
    channel = get_object_or_404(Channel, name='mic_feedback')
    if not channel.recently_updated():
        channel.update()
    latest_news = Entry.objects.order_by('-creation_date')[:5]
    return render(request, 'zach/new.html', {'channel': channel, 'latest_news': latest_news})
