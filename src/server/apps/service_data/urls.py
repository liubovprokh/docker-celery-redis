from django.urls import path
from rest_framework.routers import DefaultRouter

from server.apps.service_data.views import save_data, UserWeightView

urlpatterns = [
    path('save/', save_data),
]

router = DefaultRouter()
router.register('weight', UserWeightView, basename='user-weight')
