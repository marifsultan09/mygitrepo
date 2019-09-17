from django import forms
from .models import Ticket


class Ticketform(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["Pax_Name", "F_H_Name", "Route", "Company_Name", "Travel_agency", "price", "profit_percent", "myshare"]

