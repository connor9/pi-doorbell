# Generated by Django 2.2.7 on 2019-11-27 13:22

from django.db import migrations


def create_sounds(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Sound = apps.get_model('doorbell', 'Sound')

    Sound(name="Chime", protected=True).save()
    Sound(name="Siren", protected=True).save()

class Migration(migrations.Migration):

    dependencies = [
        ('doorbell', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_sounds),
    ]
