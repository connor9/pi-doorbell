from django.contrib import admin
from pidoorbell.doorbell.models import Sound, VirtualDevice

# Register your models here.
admin.site.register(Sound)
admin.site.register(VirtualDevice)