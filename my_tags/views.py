from django.shortcuts import render
import datetime

# Create your views here.
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {"x": "Welcome to django"})

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def filter_demo(request):
    context = {
        "my_string": "Hello World",
        "my_date": datetime.date(2025, 6, 18),
        "long_string": "This is a long string to be displayed entirely",
        "string_length": "django programming",
        "optional_value": None,
        "text_with_breaks": "Hello\nWorld\nThis is Django"


    }
    return render(request, 'filters.html', context)
def login(request):
    return render(request, 'login.html')