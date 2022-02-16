from rest_framework.decorators import api_view
from rest_framework.response import Response
from server.apps.tasks import run_import


@api_view(['GET'])
def run_task_import(request):

    run_import.delay()

    return Response({'SUCCESS': True},  status=200)
