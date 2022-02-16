from rest_framework import serializers

from server.apps.service_data.models import UserWeight


class UserWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWeight
        fields = (
            'user_id',
            'day',
            'weight',
        )

