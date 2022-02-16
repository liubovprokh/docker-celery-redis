from django.urls import path, include

from server.apps.service_api.views import get_user_data
from server.apps.service_import.views import run_task_import
from server.apps.service_data.urls import router as weight_router

urlpatterns = [
    path('external-fake-api/', get_user_data),
    path('run-import-task/', run_task_import),
    path('data_api/', include('server.apps.service_data.urls')),
    path('data_api/', include(weight_router.urls)),
]
