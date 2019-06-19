from rest_framework import viewsets
from Radomir_Climbing.api.serializers import UserSerializer, GroupSerializer, RouteSerializer
from django.contrib.auth.models import User, Group
from Radomir_Climbing.api.models import Route

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class RouteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

