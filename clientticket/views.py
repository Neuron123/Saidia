from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
# Create your views here.

# Create your views here.
class AboutView(TemplateView):
	template_name = 'client_index.html'