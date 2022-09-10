from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.utils import timezone
from .models import UserActivityLog

@receiver(user_logged_in)
def register_user_login(sender, request, user, **kwargs):
    print("Aca abrio sesion")
    obj = UserActivityLog.objects.create(user = user, login_date = timezone.now())
    request.session['user_activity_log_id'] = obj.id

@receiver(user_logged_out)
def register_user_logout(sender, request, user, **kwargs):
    print("Aca cerro sesion")
    UserActivityLog.objects.filter(id = request.session['user_activity_log_id']).update(
        logout_date = timezone.now()
    )