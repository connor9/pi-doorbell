from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from pidoorbell.doorbell.models import Sound, VirtualDevice
from rest_framework import viewsets
from pidoorbell.doorbell.serializers import UserSerializer, GroupSerializer, SoundSerializer, VirtualDeviceSerializer


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

class SoundViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Sound.objects.all()
    serializer_class = SoundSerializer

class VirtualDeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = VirtualDevice.objects.all()
    serializer_class = VirtualDeviceSerializer

    @action(methods=['post'], detail=True)
    def send_the_mail(self, request):
        print("yo")
