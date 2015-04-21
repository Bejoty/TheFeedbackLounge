from django.shortcuts import render


def viewers(request):
  return render(request, 'modtools/viewers.html')