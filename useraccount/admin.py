from django.contrib import admin

# Register your models here.
from useraccount.models import UserDetail, ActivityPeriod


class UserModelAdmin(admin.ModelAdmin):
    list_display = ['user_id','username','timezone']
    fields = ['user_id','username','timezone']


class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user','start_time','end_time']


admin.site.register(UserDetail, UserModelAdmin)
admin.site.register(ActivityPeriod, ActivityAdmin)