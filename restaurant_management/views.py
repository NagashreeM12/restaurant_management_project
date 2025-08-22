from rest_framework.views import APIView
from rest_framework.response import Response
class MenuView(APIView):
    def get(self,request):
        #Hardcoded menu data
        menu=[
            {"name":"Margherita Pizza","description":"Classic cheese and tomato pizza","price":8.99},
            {"name":"Pasta Alfredo","description":"Creamy Pasta with Alfredo sauce","price":10.50},
            {"name":"Caesar Salad","description":"Fresh lettuce with Caesar dressing","price":6.75},
            {"name":"Grilled chicken","description":"Served with veggies and fries","price":12.00},
        ]
        return Response(menu)