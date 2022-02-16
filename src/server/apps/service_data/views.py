from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from server.apps.service_data.models import UserWeight
from server.apps.service_data.serializers import UserWeightSerializer
from server.apps.tasks import save_user_weight
from rest_framework.response import Response


@api_view(['POST'])
def save_data(request, *args, **kwargs):
    save_user_weight.delay(request.data['key'])

    return Response({'SUCCESS': True}, status=200)


class UserWeightView(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UserWeightSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = UserWeight.objects.filter(user_id=user_id).order_by('day')
        else:
            queryset = UserWeight.objects.order_by('day')
        return queryset
