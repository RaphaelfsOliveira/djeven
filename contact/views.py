from django.shortcuts import render

from contact.models import Contact
from contact.forms import ContactForm

# Create your views here.
def contact_form(request):
    return render(request, 'contact/contact.html')

def base_page(request):
    return render(request, 'contact/base.html')

def index_page(request):
    return render(request, 'contact/index.html')
