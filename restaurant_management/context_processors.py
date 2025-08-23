from django.conf import settings
def restaurant_name(request):
    return {
        "restaurant_name":settings.RESTAURANT_NAME
        
    }