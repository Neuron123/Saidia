from django.forms import ModelForm
from .models import ClientTicket



class ClientTicketForm(ModelForm):
    class Meta:
        model = ClientTicket
        exclude = ('current_uid','created_date',)