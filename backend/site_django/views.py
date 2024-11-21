from django.shortcuts import render
def index(request):
    return render(request, 'site_django/index.html')