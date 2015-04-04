from django.shortcuts import render


def index(request):
  return render(request, 'stream/index.html')

def new(request):
  return render(request, 'stream/new.html')

def test(request):
  return render(request, 'stream/test.html')