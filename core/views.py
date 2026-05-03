# core/views.py

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .forms import ContactForm
from .models import ContactMessage


def home(request):
    return render(request, 'core/home.html')


def services(request):
    return render(request, 'core/services.html')


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message,
            )

            admin_html = render_to_string('emails/admin_notification.html', {
                'name': name,
                'email': email,
                'message': message,
            })

            admin_email = EmailMultiAlternatives(
                subject=f'Mesaj nou de pe site - {name}',
                body=strip_tags(admin_html),
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.CONTACT_RECEIVER_EMAIL],
                reply_to=[email],
            )
            admin_email.attach_alternative(admin_html, 'text/html')
            admin_email.send(fail_silently=False)

            confirmation_html = render_to_string('emails/confirmation.html', {
                'name': name,
            })

            confirmation_email = EmailMultiAlternatives(
                subject='Am primit mesajul tău',
                body=strip_tags(confirmation_html),
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[email],
            )
            confirmation_email.attach_alternative(confirmation_html, 'text/html')
            confirmation_email.send(fail_silently=False)

            return redirect('/?sent=1')
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {
        'form': form,
    })