from django.conf import settings

def vite_dev_url(request):
    return {'VITE_DEV_SERVER_URL': settings.VITE_DEV_SERVER_URL}