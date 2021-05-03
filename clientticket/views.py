from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from keycloak import KeycloakAdmin
from keycloak.exceptions import KeycloakAuthenticationError, KeycloakGetError
from keycloak import KeycloakOpenID
from time import gmtime, strftime
from clientticket.forms import ClientTicketForm
from clientticket.models import ClientTicket
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

#get current time
showtime = strftime("%Y-%m-%dT%H:%M:%S", gmtime())
# Create your views here.
@method_decorator(login_required, name='dispatch')
class AboutView(TemplateView):
		
	template_name = 'client_index.html'

@method_decorator(login_required, name='dispatch')
class CreateTicketView(CreateView):
	template_name = 'client_ticket.html'
	form_class = ClientTicketForm
	model = ClientTicket
	success_url = 'tickets'

def not_in_customer_group(user):
	if user.groups.filter(name='customer').exists():
		return True
	else:
		return False

@login_required
@user_passes_test(not_in_customer_group,login_url='/tickets/')
def create_ticket(request):
	if request.method == 'POST':
		form = ClientTicketForm(request.POST)
		if form.is_valid():
			current_uid = request.user.id
			ticket_title = form.cleaned_data['ticket_title']
			ticket_content = form.cleaned_data['ticket_content']
			created_date = showtime
			creation_ticket = ClientTicket(current_uid=current_uid, ticket_title=ticket_title, ticket_content=ticket_content, created_date=created_date)
			creation_ticket.save()
			return HttpResponseRedirect('tickets/')
	else:
	    form = ClientTicketForm()
	return render(request,'client_ticket.html',{'form':form}) 

@login_required
def list_tickets(request):
	current_uid = request.user.id
	print("id="+ str(current_uid))
	tickets = ClientTicket.objects.filter(current_uid = current_uid);
	#tickets = ClientTicket.objects.all();
	return render(request,'client_index.html',{'ticket_list':tickets})

