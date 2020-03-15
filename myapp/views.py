import json
import logging

from .forms import ContactForm
from .models import ContactMessage, Project

from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    context = {
        'form':ContactForm(),
        'projects':Project.objects.all().order_by('sort_order'),
    }
    return render(request, 'index.html', context)

def contact(request):
    if request.method == "POST":
        cf = ContactForm(request.POST)

        # Set default fail message
        message = 'Failed... Try again later.'
        if(cf.is_valid()):
            # Create actual object
            cm = ContactMessage()
            cm.name = cf.cleaned_data['name']
            cm.email = cf.cleaned_data['email']
            cm.message = cf.cleaned_data['message']
            cm.save()

            # Log message
            logger.info('New contact message: %s', request.build_absolute_uri(reverse('admin:myapp_contactmessage_change', args=(cm.id,))))

            # Success Message
            message = "Sent!"

        return HttpResponse(message)
