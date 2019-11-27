from django.db import models
import uuid



class Sound(models.Model):
    guid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    protected = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, default='', unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

# class Config(models.Model):
#     default_chime = models.ForeignKey(Sound, on_delete=models.SET_NULL, null=True)
#     default_siren = models.ForeignKey(Sound, on_delete=models.SET_NULL, null=True)


class VirtualDevice(models.Model):
    STATE_OFF = 'off'
    STATE_PLAYING = 'chime'
    STATE_SIREN = 'siren'
    DEVICE_STATES = [
        (STATE_OFF, 'Off'),
        (STATE_PLAYING, 'Chime'),
        (STATE_PLAYING, 'Siren Alert'),
    ]

    STATE_ON_NOTHING = 'nothing'
    STATE_ON_ACTIONS = [
        (STATE_ON_NOTHING, 'Do Nothing'),
        ('chime', 'Play Default Chime'),
        ('siren', 'Play Siren'),
        ('custom', 'Play custom sound'),
    ]

    guid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, default='', unique=True)

    state_on_action = models.CharField(
        max_length=8,
        choices=STATE_ON_ACTIONS,
        default=STATE_ON_NOTHING,
    )

    # Current State
    state = models.CharField(
        max_length=8,
        choices=DEVICE_STATES,
        default=STATE_OFF,
    )
    state_updated = models.DateTimeField(auto_now_add=True)

    # Device Config
    repeat = models.IntegerField(default=0)
    repeat_count = models.IntegerField(default=1)
    volume = models.IntegerField(default=100)
    custom_sound = models.ForeignKey(Sound, on_delete=models.SET_NULL, null=True)

    def __str(self):
        return self.name + " (" + self.state_on_action + ")"

    class Meta:
        ordering = ['name']

