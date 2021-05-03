from django.urls import path
from useraccounts.views import SignUpView

urlpatterns = [
	path('signup/', SignUpView.as_view(), name='signup'),
]