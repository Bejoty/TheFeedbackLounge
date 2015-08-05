from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.contrib.auth.models import User, UserManager
from twitch_profiles.models import Profile
import urllib
import json
from zach.secret import TWITCH_ID, TWITCH_SECRET


def connect(request):
    # User is already connected
    if 'name' in request.session:
        return HttpResponseRedirect(reverse('index'))

    # URL for Twitch authentication, with query parameteres
    auth_url = (
        'https://api.twitch.tv/kraken/oauth2/authorize'
    '?response_type=code'
    '&client_id=' + TWITCH_ID +
    '&redirect_uri=http://' + request.get_host() + reverse('authenticate') +
    '&scope=user_read'
  )

    # Append query parameter for post-authentication URL redirect
    if 'HTTP_REFERER' in request.META:
        auth_url += '&state=' + request.META['HTTP_REFERER']

    return HttpResponseRedirect(auth_url)


def auth(request):
    # Capture authorization code, scope, and pre-authorized website state
    code = request.GET['code']
    scope = request.GET['scope']
    if 'state' in request.GET:
        state = request.GET['state']
    else:
        state = reverse('index')
    
    # Request access token from Twitch
    data = urllib.parse.urlencode({
        'client_id': TWITCH_ID,
        'client_secret': TWITCH_SECRET,
        'grant_type': 'authorization_code',
        'redirect_uri': 'http://' + request.get_host() + reverse('authenticate'),
        'code': code
        })
    data = data.encode('utf-8')
    token_req = urllib.request.Request('https://api.twitch.tv/kraken/oauth2/token')
    token_req.add_header('Content-Type', 'application/x-www-form-urlencoded;charset=utf-8')
    token_res = urllib.request.urlopen(token_req, data)

    # Acquire access token
    token_data = json.loads(token_res.read().decode('utf-8'))
    access_token = token_data['access_token']

    # Request Twitch user information
    user_req = urllib.request.Request('https://api.twitch.tv/kraken/user')
    user_req.add_header('Authorization', 'OAuth ' + access_token)
    user_res = urllib.request.urlopen(user_req)

    # Acquire user information
    user_data = json.loads(user_res.read().decode('utf-8'))
    name = user_data['name']
    display_name = user_data['display_name']
    bio = user_data['bio']
    logo_url = user_data['logo']
    email = user_data['email']

    # Create new user if applicable
    if not User.objects.filter(username=name).exists():
        user = User.objects.create_user(username=name, email=email)
        p = Profile(user=user)
        p.save()

    # Update user profile
    user = User.objects.get(username=name)
    p = Profile.objects.get(user=user)
    p.display_name = display_name
    p.logo_url = logo_url
    p.bio = bio
    p.access_token = access_token
    p.save()

    # Save session (log in)
    request.session['name'] = name

    return HttpResponseRedirect(state)


def logout_user(request):
    logout(request)
    if 'HTTP_REFERER' in request.META:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    return HttpResponseRedirect(reverse('index'))

def test(request):
    if 'name' in request.session:
        name = request.session['name']
        user = get_object_or_404(User, username=name)
        return render(request, 'twitch_profiles/test.html', {'user': user})
    else:
        return HttpResponse("Not connected.")
