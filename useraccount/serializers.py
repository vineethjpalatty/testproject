from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import UserDetail, ActivityPeriod


class ActivityPeriodSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    activity_periods = SerializerMethodField()

    class Meta:
        model = UserDetail
        fields = ('user_id', 'username', 'timezone','activity_periods')

    def get_activity_periods(self,obj):
        return ActivityPeriodSerializer(obj.get_related_activity_period.all(), many=True).data