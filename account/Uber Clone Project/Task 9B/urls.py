from django.urls import path
from .views import SubmitRideFeedbackView

urlpatterns = [
    path('api/ride/feedback/<int:ride_id>/', SubmitRideFeedbackView.as_view(), name='ride-feedback'),
]
