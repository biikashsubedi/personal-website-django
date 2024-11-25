import requests
from django.core.management.base import BaseCommand
import schedule
import time

from apps.system.analyticData.models import *


def update_geo_data(api_object):
    try:
        api_url = f'https://get.geojs.io/v1/ip/geo/{api_object.ip_address}.json'
        response = requests.get(api_url)
        data = response.json()
        api_object.city = data.get('city', 'Unknown')
        api_object.region = data.get('region', 'Unknown')
        api_object.country = data.get('country', 'Unknown')
        api_object.country_code = data.get('country_code', None)
        api_object.latitude = data.get('latitude', None)
        api_object.longitude = data.get('longitude', None)
        api_object.internet_provider = data.get('organization_name', None)
        api_object.timezone = data.get('timezone', None)
        api_object.location_accuracy = data.get('accuracy', None)
        api_object.completed = bool(data.get('city', None) or data.get('region', None) or data.get('country', None))
        api_object.save()

    except Exception as e:
        pass


class Command(BaseCommand):
    help = 'This command is for getting location from ip address'
    print('Working On queue')

    def handle(self, *args, **options):
        schedule.every(120).seconds.do(get_location_from_ip)

        while True:
            schedule.run_pending()
            time.sleep(1)



def get_location_from_ip():
    try:
        print('Working On Api Analytics')
        api_analytics = IPAnalytic.objects.filter(completed=False)
        for api in api_analytics:
            update_geo_data(api)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
