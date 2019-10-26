from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Ticket
from .forms import Ticketform


# CREAT     make new    POST
# RETREIVE  get         GET
# UPDATE    edit        PUT/PATCH
# DELETE    delete      

# Create your views here.
def home(request):
    return render(request, 'home.html')
    # return HttpResponse('Home')


# Create your views here.
def about(request):
    return render(request, 'about.html')
    # return HttpResponse('About')


def dashboard(request):
    tickets = Ticket.objects.all()
    return render(request, 'dashboard.html', {'tickets': tickets})
    # return HttpResponse('About')

def create_ticket(request):
    form = Ticketform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/dashboard')
    return render(request, 'add_ticket.html', {'form': form})

def edit_ticket(request):
    tickets = Ticket.objects.all()
    return HttpResponse('Edit Ticket')
    # form = Ticketform(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     return redirect('/dashboard')
    # return render(request, 'add_ticket.html', {'form': form})

def remove_ticket(request):
    return HttpResponse('Ticket Removed')

# Create your views here.
def help(request):

    return render(request, 'help.html')
    # return HttpResponse('help')



