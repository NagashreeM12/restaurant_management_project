from django.shortcuts import render,redirect
from.form import FeedbackForm
from.models import FeedbackForm
#View to handle feedback form submission
def feedback_view(request):
    if request.method=="POST":
        form=Feedbak