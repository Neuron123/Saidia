from django.urls import path
from clientticket.views import *

urlpatterns = [
	path('tickets/',list_tickets, name='clienttickets'),
	path('create_ticket', create_ticket, name='create_ticket'),
]