from django.shortcuts import render, redirect, get_object_or_404
import datetime
from django.utils.safestring import mark_safe
import markdown
from .models import Blog, Subscriber
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .forms import SubscriptionForm
from django.http import HttpResponse
from django.urls import reverse

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

def blog_list(request):
    blogs = Blog.objects.prefetch_related('editors').all()
    for blog in blogs:
        blog.rendered_text = mark_safe(markdown.markdown(blog.text))
    return render(request, 'blog_list.html', {'blogs': blogs})

def subscribe(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        if not email:
            messages.error(request, 'Please enter a valid email address.')
            return redirect('subscribe')
        if 'unsubscribe' in request.POST:
            deleted, _ = Subscriber.objects.filter(email=email).delete()
            if deleted:
                messages.success(request, f'{email} has been unsubscribed.')
            else:
                messages.info(request, f'{email} was not found in our list.')
            return redirect('subscribe')
        if Subscriber.objects.filter(email=email).exists():
            messages.error(request, 'You are already subscribed.')
            context['existing_email'] = email  # Enables unsubscribe button
        else:
            Subscriber.objects.create(email=email)
            messages.success(request, 'Thank you for subscribing!')
            return redirect('subscribe')
    return render(request, 'subscribe.html', context)

def subscribe(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        if not email:
            messages.error(request, 'Please enter a valid email address.')
            return redirect('subscribe')
        if 'unsubscribe' in request.POST:
            deleted, _ = Subscriber.objects.filter(email=email).delete()
            if deleted:
                messages.success(request, f'{email} has been unsubscribed.')
            else:
                messages.info(request, f'{email} was not found in our list.')
            return redirect('subscribe')
        if Subscriber.objects.filter(email=email).exists():
            messages.error(request, 'You are already subscribed.')
            context['existing_email'] = email  # Enables unsubscribe button
        else:
            Subscriber.objects.create(email=email)
            messages.success(request, 'Thank you for subscribing!')
            return redirect('subscribe')
    return render(request, 'subscribe.html', context)