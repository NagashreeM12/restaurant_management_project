from datetime import datetime
def get_current_year(request):
    return {'current_year':datetime.now().year}

