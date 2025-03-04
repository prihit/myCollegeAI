from django.shortcuts import render

from tracker.models import Tracker
from tracker.utilities import get_client_ip

def log_to_tracker(request, curr_page):
    if request.user.is_authenticated:
        try:
            profile = request.user.profile
            ip = get_client_ip(request)
            obj = Tracker.objects.create(profile = profile,ip_address = ip, curr_page=curr_page)
            obj.save()
        except BaseException:
            print('Failed to log to database!')