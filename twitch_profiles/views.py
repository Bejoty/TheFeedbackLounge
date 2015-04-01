from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User


def view(request, username):
	user = get_object_or_404(User, username=username)
	return render(request, 'twitch_profiles/view.html', {'user': user})

def session_test(request):
	if 'name' in request.session:
		name = request.session['name']
		user = get_object_or_404(User, username=name)
		return render(request, 'twitch_profiles/view.html', {'user': user})
	else:
		return HttpResponse("Not connected.")