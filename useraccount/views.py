from rest_framework import viewsets
from useraccount.models import UserDetail
from useraccount.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = UserSerializer
    queryset = UserDetail.objects.all()