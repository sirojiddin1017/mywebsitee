from django.shortcuts import render
from django.http import HttpResponse

from home.models import Setting


# Create your views here.
def index(request):
    setting = Setting.objects.get()
    context = {'setting':setting}
    return render(request,'index.html',context)


def about (request):
    return render(request, 'about.html')


def contact (request):
    return render(request, 'contact.html')


def selectlanguage():
    return None