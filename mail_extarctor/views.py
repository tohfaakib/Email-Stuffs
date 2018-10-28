from django.shortcuts import render

from .models import Extractor

import re #for regex

# Create your views here.

def home(request):
    return render(request, 'mail_extractor/home.html')




def collector(request):
    return render(request, 'mail_extractor/mail_collector.html')

def extractor(request):
    fulltext = request.GET['fulltext']
    mail_list = []


    # line = "why people don't know what regex are? let me know asdfal2@als.com., Users1@gmail.de. " \
    #        "Dariush@dasd-asasdsa.com.lo,Dariush.lastName@someDomain.com"
    match = re.findall(r'[\w\.-]+@[\w\.-]+', fulltext)
    for i in match:
        if i[-1] == '.':
            i = i.replace(i[len(i) - 1], '')

            if i[-3:] == 'com' or i[-3:] == 'net' or i[-3:] == 'org' or i[-3:] == 'edu' and i[-4] != '.':
                i = list(i)
                i.insert(-3, '.')
                i = ''.join(i)

        #valid = re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', i, re.I)
        valid = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', i)


        if valid:
            if i not in mail_list:
                i = i.lstrip("%&*-+)(^$#@")
                i = i.lower()
                mail_list.append(i)

    total_email = len(mail_list)
    mail_list.sort()


    e = Extractor(email_list=mail_list)
    e.save()


    return render(request, 'mail_extractor/extractor.html', {'total_email': total_email, 'email_list':mail_list})
