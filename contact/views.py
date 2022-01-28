from django.shortcuts import render, HttpResponse
from .models import contact_main, contact_form
from .forms import form_contact
import re
from django.core.mail import EmailMessage
from django.conf import settings


def send_message(name, email, phone, comment):
    name = re.sub('<[^<]+?>', '', name)
    email = re.sub('<[^<]+?>', '', email)
    phone = re.sub('<[^<]+?>', '', phone)
    comment = re.sub('<[^<]+?>', '', comment)
    message = name + '<br>' + email + '<br>' + phone + '<br>' + comment
    send_msg = EmailMessage('Test', message, settings.EMAIL_HOST_USER, ['iamslamduck@gmail.com', 'ulikfr1d@gmail.com'])
    send_msg.content_subtype = "html"
    send_msg.send()
    return HttpResponse()


def contact_view(request):
    link_ru = '/ru/contacts/'
    link_en = '/en/contacts/'
    link_fr = '/fr/contacts/'

    context = {
        'show_language': True,
        'link_en': link_en,
        'link_fr': link_fr,
        'link_ru': link_ru,
        'contact_main': contact_main.objects.first(),
        'contact_form': contact_form.objects.first()

    }

    return render(request, 'contacts.html', context=context)

def form_view(request):
    if request.is_ajax() and request.POST:
        form = form_contact(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            comment = form.cleaned_data['comment']
            return send_message(name, email, phone, comment)