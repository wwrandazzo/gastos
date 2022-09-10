from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    login_date = models.DateTimeField(null=True)
    logout_date = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
