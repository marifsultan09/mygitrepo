from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Ticket
from .forms import Ticketform

from django.contrib.auth import authenticate

# CREAT     make new    POST
# RETREIVE  get         GET
# UPDATE    edit        PUT/PATCH
# DELETE    delete      

# Create your views here.
def home(request):
    return render(request, 'home.html')
    # return HttpResponse('Home')

def login(request):
    return render(request, 'login.html')
    # return HttpResponse('Home')

# Create your views here.
def about(request):
    return render(request, 'about.html')
    # return HttpResponse('About')


def dashboard(request):
    tickets = Ticket.objects.all()
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
    # A backend authenticated the credentials
        print('recognised')
        return render(request, 'dashboard.html', {'tickets': tickets})
    else:
    # No backend authenticated the credentials
        print('not recognised')
        return HttpResponse('Wrong Username or password')
    # print('here')
    # return redirect('/dashboard',{'tickets': tickets})

    # return HttpResponse('About')

def create_ticket(request):
    form = Ticketform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/dashboard')
    return render(request, 'add_ticket.html', {'form': form})


def edit_ticket(request):
    # tickets = Ticket.objects.all()
    tkt = Ticket.objects.filter(id=1).first()
    print(tkt.Company_Name)
    if request.method == 'GET':
        print(request)
        print('get')
        # print(tickets.method.get())
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



