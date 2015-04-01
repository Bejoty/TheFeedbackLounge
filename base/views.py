from django.shortcuts import render


def base(request):
	return render(request, 'base/base.html')

def test(request):
	return render(request, 'base/test.html')