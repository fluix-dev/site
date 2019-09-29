from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from .forms import *
from .models import *
import json

# Create your views here.
def index(request):
    return render(request, 'index.html', {'form':ContactForm()})

def contact(request):
    if request.method == "POST":
        cf = ContactForm(request.POST)

        # Set default fail message
        message = 'An error occured, please try again later.'
        if(cf.is_valid()):
            # Create actual object
            cm = ContactMessage()
            cm.name = cf.cleaned_data['name']
            cm.email = cf.cleaned_data['email']
            cm.message = cf.cleaned_data['message']
            cm.save()

            # Success Message
            message = "Thanks for reaching out! I'll get back to you soon."

        return HttpResponse(message)
