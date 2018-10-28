from django.shortcuts import render
from validate_email import validate_email
import re

import smtplib
import sendgrid
from sendgrid.helpers.mail import *
import os

from django.core.mail import send_mail
from smtplib import SMTPException

# Create your views here.


def mail_tester(request):
    return render(request, 'mail_tester.html')

def alive_mail(request):
    mail_list = request.GET['email_list']

    alive = []

    match = re.findall(r'[\w\.-]+@[\w\.-]+', mail_list)
    for i in match:
        is_exist = validate_email(i, verify=True)
        if is_exist:
            if i not in alive:
                alive.append(i)

    return render(request, 'alive_mail.html', {'alive_list': alive})
