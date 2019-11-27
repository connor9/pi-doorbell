from django.contrib.auth.models import User, Group
from pidoorbell.doorbell.models import Sound, VirtualDevice
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class SoundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sound
        fields = ['guid', 'name', 'created', 'protected']
        read_only_fields = ('guid', 'created', 'protected')


class VirtualDeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VirtualDevice
        fields = ['guid', 'name', 'created', 'state_on_action', 'state', 'state_updated', 'repeat', 'repeat_count', 'volume', 'custom_sound']
        read_only_fields = ('guid', 'created', 'state', 'state_updated')
