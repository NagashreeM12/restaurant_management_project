from django.shortcuts import render
from django.http import HttpResponse
from django.db import DatabaseError
def reservations(request):
    try:
        #If you later fetch data from DB,put it here
        #Example:reservations_list=Reservation.objects.all()
        return render(request,'home/reservations.html')
    except DatabaseError as db_err:
        #Handles any DB-related issues
        return HttpResponse(f"Database error occured:{db_err}",status=500)
        #Handles unexpected errors
        return HttpResponse(f"An unexpected error occured:{e}",status=500)

