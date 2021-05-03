from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class ClientTicket(models.Model):
	#current_uid = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	current_uid = models.CharField(max_length=10,null=True)
	ticket_title = models.CharField(max_length=1000)
	ticket_content = models.TextField(max_length=2000)
	created_date = models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		return self.current_uid

class CreateTicket(models.Model):
	clientemail = models.CharField(max_length=1000)
	ticket_title = models.CharField(max_length=500)
	ticket_content = models.CharField(max_length=1000)
	created_date = models.DateTimeField(default=timezone.now)