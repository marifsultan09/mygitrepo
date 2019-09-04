from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home(request):

    return render(request, 'home.html')
    # return HttpResponse('Home')


# Create your views here.
def about(request):
    return render(request, 'about.html')
    # return HttpResponse('About')


def dashboard(request):
    return render(request, 'dashboard.html')
    # return HttpResponse('About')


# Create your views here.
def help(request):

    return render(request, 'help.html')
    # return HttpResponse('help')



