from django.shortcuts import render
from .forms import ContactForm


def home(request):
    return render(request,'main/main.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    form = ContactForm()
    return render(request, 'main/contact.html', {'form':form})
