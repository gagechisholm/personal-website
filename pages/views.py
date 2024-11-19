from django.shortcuts import render
from django.http import HttpResponse

def home_page_view(request):
    return HttpResponse("Homepage")

def about_page_views(request):
    context = {
        "age": 23,
        "name": "Gage"
        }
    return render(request, "pages/about.html", context)