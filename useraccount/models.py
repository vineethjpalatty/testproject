from django.contrib.auth.models import AbstractUser
from django.db import models
import pytz
# Create your models here.


class DateBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserDetail(AbstractUser,DateBaseModel):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    user_id = models.CharField(max_length=20,verbose_name="User ID", unique=True)
    timezone = models.CharField(max_length=50,verbose_name="Time Zone", choices=TIMEZONES, default='UTC')
    password = models.CharField(verbose_name="password", max_length=128, null=True, blank=True)

    def __str__(self):
        return self.username


class ActivityPeriod(DateBaseModel):
    user = models.ForeignKey('UserDetail',on_delete=models.CASCADE,related_name='get_related_activity_period')
    start_time = models.DateTimeField(verbose_name='Start Time')
    end_time = models.DateTimeField(verbose_name='End Time')

    def __str__(self):
        return self.user.username


