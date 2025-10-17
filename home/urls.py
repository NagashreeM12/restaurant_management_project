# urls.py
# home/urls.py
from django.urls import path
from .views import ContactFormSubmissionView

urlpatterns = [
    path('contact/', ContactFormSubmissionView.as_view(), name='contact-form'),
]
