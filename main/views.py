from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories

def index(request):

    categories = Categories.objects.all()

    context: dict[str, str] = {
        "title": "Home - მთავარი",
        "content": "მაღაზია HOME",
        "categories": categories
}

    return render(request, 'main/index.html', context)

def about(request):
    context: dict[str, str] = {
        "title": "Home - ჩვენზე",
        "content": "ჩვენზე",
        "text_on_page": "ჩვენ მზად ვართ გავხადოთ თქვენი საცხოვრებელი ფართი მართლაც განსაკუთრებული."
}

    return render(request, 'main/about.html', context)

def contact(request):
    context: dict[str, str] = {
        "content": "ნომერი: 555555555"
}

    return render(request, 'main/contact.html', context)

def deliever(request):
    context: dict[str, str] = {
        "content": "მიტანის სერვისი"
}

    return render(request, 'main/deliever.html', context)
