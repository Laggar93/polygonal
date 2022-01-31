from django.shortcuts import render, HttpResponse
from .models import contact_main, contact_form
from .forms import form_contact
import re
from django.core.mail import EmailMessage
from django.conf import settings

template_part_1 = '<body style="margin:0;padding:0;background:#E6E6E6"><table width="100%" border="0" cellspacing="0" cellpadding="0" style="margin:0 auto"><tr><td><table width="600px" border="0" cellspacing="0" cellpadding="0" style="margin:64px auto;background:#FFFFFF"><tr><td style="margin:32px;padding:32px">'
template_part_2 = '</td></tr></table></td></tr></table></body>'



def send_message(name, email, phone, comment):
    name = re.sub('<[^<]+?>', '', name)
    email = re.sub('<[^<]+?>', '', email)
    phone = re.sub('<[^<]+?>', '', phone)
    comment = re.sub('<[^<]+?>', '', comment)
    message = template_part_1 + '<p style="font-family:Tahoma,Verdana,sans-serif;font-size:16px;line-height:27px"><b>' + name + '</p><p style="font-family:Tahoma,Verdana,sans-serif;font-size:16px;line-height:27px"><b>' + ':</b> <a href="mailto:' + email + '" style="color:#1F7147;text-decoration:none">'  + email + '<br>' + phone + '<br>' + comment
    send_msg = EmailMessage('Сообщение от сайта polygonalpaper.com', message, settings.EMAIL_HOST_USER, ['ulikfr1d@gmail.com'])
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