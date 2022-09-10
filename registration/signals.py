from django.dispatch import receiver
from django.contrib.auth import user_logged_in, user_logged_out
from django.utils import timezone
from .models import UserActivityLog
import pytz

@receiver(user_logged_in)
def register_user_login(sender, request, user, **kwargs):
    obj = UserActivityLog.objects.create( user = user, login_date = timezone.now())
    request.session['user_activity_log_id']= obj.id
    print( pytz.all_timezones)

@receiver(user_logged_out)
def register_user_logout(sender, request, user, **kwargs):
    UserActivityLog.objects.filter(id=request.session['user_activity_log_id']).update(logout_date=timezone.now())

