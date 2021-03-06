# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-05 06:39
from __future__ import unicode_literals

from django.db import migrations, models
from external_services.models import LTIService as _LTIService
LTI_ACCESS = _LTIService.LTI_ACCESS

def forwards_autoselect(apps, schema_editor):
    LTIService = apps.get_model('external_services', 'LTIService')
    for service in LTIService.objects.all():
        service.access_settings = LTI_ACCESS.PUBLIC_API_YES if service.enable_api_access else LTI_ACCESS.PUBLIC_API_NO
        service.save()

def backwards_autoselect(apps, schema_editor):
    LTIService = apps.get_model('external_services', 'LTIService')
    for service in LTIService.objects.all():
        service.enable_api_access = service.api_access
        service.save()

class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('external_services', '0006_ltiservice_enable_api_access'),
    ]

    operations = [
        migrations.AddField(
            model_name='ltiservice',
            name='access_settings',
            field=models.IntegerField(choices=[(0, 'Anonymous service, no API access'), (5, 'Public service, no API access'), (10, 'Public service, allow API access')], default=0, help_text="Select whether to pass pseudonymised user data to the LTI service.</br>Public services can also enable sharing the user's API token and course API URL in the LTI launch request. This grants the LTI tool API access with the user's privileges."),
        ),
        migrations.RunPython(forwards_autoselect, backwards_autoselect),
        migrations.RemoveField(
            model_name='ltiservice',
            name='enable_api_access',
        ),
    ]
