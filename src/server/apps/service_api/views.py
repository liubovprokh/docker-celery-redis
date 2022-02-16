import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response
import random


@api_view(['GET'])
def get_user_data(request):

    weight = random.randint(0, 200)
    day = datetime.datetime.now().date()
    unit = random.choice(['kg', 'lb'])

    return Response({
        'day': day,
        'user_id': 12345,
        'weight': weight,
        'unit': unit
    })
