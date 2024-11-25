from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin
from user_agents import parse
from apps.backend.analyticData.models import DeviceAnalytic, IPAnalytic


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/system/login/' and not request.user.is_authenticated:
            return self.get_response(request)
        if request.path == '/system/login/' and request.user.is_authenticated:
            return redirect(reverse('home:index'))
        if request.path.startswith('/system/') and not request.user.is_authenticated:
            return redirect(reverse('login'))
        return self.get_response(request)


class CaptureRequestInfoMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Capture IP address
        ip = request.META.get('HTTP_X_FORWARDED_FOR')
        if ip:
            ip = ip.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        # Capture User-Agent info
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        device_info = parse(user_agent)
        device = device_info.device.family
        browser = device_info.browser.family
        browser_version = device_info.browser.version_string
        os = device_info.os.family
        os_version = device_info.os.version_string

        # Set values for later use
        request.ip_address = ip
        request.device_info = {
            'device': device,
            'browser': browser,
            'browser_version': browser_version,
            'os': os,
            'os_version': os_version,
            'user_agent': user_agent
        }

    def process_response(self, request, response):
        if response.status_code == 200:
            device_info = request.device_info
            device = device_info['device']
            os = device_info['os']
            os_version = device_info['os_version']
            browser = device_info['browser']
            browser_version = device_info['browser_version']
            user_agent = device_info['user_agent']
            route_name = request.path

            if not route_name.startswith('/system/') and not route_name.startswith(
                    '/media/') and not route_name.startswith('/cached-route/'):
                checkExists = DeviceAnalytic.objects.filter(
                    device=device,
                    os=os,
                    os_version=os_version,
                    browser=browser,
                    browser_version=browser_version
                ).first()

                if checkExists:
                    checkExists.hits += 1
                    checkExists.last_hit_at = timezone.now()
                    checkExists.save()
                else:
                    DeviceAnalytic.objects.create(
                        device=device,
                        os=os,
                        os_version=os_version,
                        browser=browser,
                        browser_version=browser_version,
                        hits=1,
                        last_hit_at=timezone.now(),
                        user_agent=user_agent
                    )

                # Capture IP address
                clear_route = 'home' if route_name == '/' else route_name.replace('/', '').replace('\\', '')
                checkIpExists = IPAnalytic.objects.filter(ip_address=request.ip_address, api=clear_route).first()

                if checkIpExists:
                    checkIpExists.hits += 1
                    checkIpExists.last_hit_at = timezone.now()
                    checkIpExists.save()
                else:
                    IPAnalytic.objects.create(
                        ip_address=request.ip_address,
                        api=clear_route,
                        hits=1,
                        last_hit_at=timezone.now(),
                    )

        return response
