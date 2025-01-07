from gettext import translation

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from twisted.conch.ssh.connection import messages
from django.contrib import messages

from course.models import Course, Subject, Tutor
from .models import Setting, ContactForm, ContactMessage


# Create your views here.

def index(request):
    setting = Setting.objects.get()
    course = Course.objects.all()
    course_cr = Course.objects.all().order_by('id')[:4]
    subject_cr = Subject.objects.all().order_by('id')[:3]
    tutor_cr = Tutor.objects.all().order_by('id')[:3]
    context = {'setting':setting,
               'course_cr':course_cr,
               'subject_cr':subject_cr,
               'tutor_cr':tutor_cr,}

    return render(request,'index.html',context)


def about(request):
    settings = Setting.objects.get()
    context = {'setting': settings}
    return render(request,'about.html',context)


TELEGRAM_BOT_TOKEN='7654721096:AAEgP6u-GAhSskVg_zuswc3FYXUFwS5TpTo'
TLEGRAM_CHANNEL ='@zayavkasharq'
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name=request.POST['name']
            phone = request.POST['phone']
            subject = request.POST['subject']
            message = request.POST['message']
            message_text=f'New message:\n\nName: {name} \nPhone:{phone} \nSubject: {subject} \nMessage: {message}'
            telegram_api_url=f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/send Message"
            telegram_params = {'chat_id'}
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.phone = form.cleaned_data['phone']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Thanks, " + data.name + "We received your message and will respond shortly... ")
            return HttpResponseRedirect('/contact')

    setting = Setting.objects.get()
    form = ContactForm
    context = {'setting': setting}
    return render(request,'contact.html',context)


def tutors(request):
    tutor = Tutor.objects.all()
    tutor_cr = Tutor.objects.all().order_by('id')[:3]
    setting = Setting.objects.get()
    context = {
               'tutor_cr' : tutor_cr,
               'tutor' : tutor,
               'setting' : setting,
    }
    return render(request, 'tutors.html', context)

def selectlanguage(request):
    if request.method == 'POST':

        lang = request.POST['language']
        translation.activate(lang)
        request.session(settings.LANGUAGE_COOKIE_NAME)=lang
        return HttpResponseRedirect('/'+lang)
