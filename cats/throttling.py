from datetime import datetime

from rest_framework import throttling


class WorkingHoursThrottling(throttling.BaseThrottle):

    def allow_request(self, request, view):
        now = datetime.now().hour
        print(now)
        if now >= 19 and now < 21:
            return False
        return True
