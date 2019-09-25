from django.shortcuts import render
from django.http import HttpResponse
from .models import Ticket
from .forms import Ticketform

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

# Create your views here.
def help(request):

    return render(request, 'help.html')
    # return HttpResponse('help')



