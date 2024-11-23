from datetime import datetime

from apps.backend.home.models import Link
from apps.backend.profiles.models import Profile


def global_data(request):
    profile = Profile.objects.filter(status=True).first()
    links = Link.objects.filter(status=True)
    return {'profile': profile, 'links': links}
