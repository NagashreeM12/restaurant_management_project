from django.shortcuts import render
from django.http import Http404
# Create your views here.
def test_404_view(request):
    raise Http404("This page does not exist")
