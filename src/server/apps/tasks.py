from celery import shared_task
import requests
import redis
import json

from server.apps.service_data.models import UserWeight
from server.settings import REDIS_HOST, REDIS_PORT, SERVICE_DATA_URL, SERVICE_API_URL


@shared_task
def run_import():
    response = requests.get(url=SERVICE_API_URL)
    data = response.json()
    data['weight'] = convert_weight(data['weight'], data['unit'])

    key = f'weight:{data["user_id"]}:{data["day"]}'
    redis_instance = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    store_data = json.dumps(data)
    redis_instance.set(key, store_data)

    requests.post(url=SERVICE_DATA_URL, data={'key': key})


def convert_weight(weight, unit):
    if unit == 'lb':
        weight *= 0.453592
    return int(weight + 0.5)


@shared_task
def save_user_weight(key):
    redis_instance = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    data = redis_instance.get(key)
    object_fields = json.loads(data)
    print('WEIGHT:', object_fields['weight'])
    if object_fields['weight'] % 2 == 0:
        UserWeight.objects.create(
            user_id=object_fields['user_id'],
            weight=object_fields['weight'],
            day=object_fields['day']
        )
    redis_instance.delete(key)
