from django.urls import path
from clientticket.views import AboutView

urlpatterns = [
	path('tickets/',AboutView.as_view(), name='clienttickets')
]