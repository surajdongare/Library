from django import http
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from .forms import Subscribe
# s = Subscribe()

from django.conf import settings
from django.core.mail import send_mail, send_mass_mail, EmailMessage

# Create your views here.
def subscribe_email(request): # fbv  - Function Based Views
    print("in subscribe_email")
    sub = Subscribe()
    if request.method == 'POST':
        sub = Subscribe(request.POST)  # email
        subject1 = 'Welcome to DataFlair'
        message1 = 'Hope you are enjoying your Django Tutorials'
        recepient = request.POST["email"].strip()  #  [v@gmail.com,test@gmail.com]
        final_rec_list = None
        if ";" in recepient:
            final_rec_list = recepient.split(";")
        else:
            final_rec_list = [recepient]
        # print(final_rec_list, "final_rec_list")
        if final_rec_list:
            # Msg = EmailMessage(subject=subject1, body=message1, from_email=settings.EMAIL_HOST_USER, to=final_rec_list)
            # Msg.attach_file("C:\\Users\\Admin\\Desktop\\ht1.txt")
            # Msg.send(fail_silently=False)
            send_mail(subject=subject1, message=message1, from_email=settings.EMAIL_HOST_USER, recipient_list=final_rec_list)
        return render(request, 'success.html', {'recepient': recepient})
    return render(request, 'index.html', context={'form1': sub})

# print(s)

# print("abcd")

# json