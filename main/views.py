from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context: dict[str, str] = {
        "title": "Home",
        "content": "This is the home page"
}

    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse("About Page")
