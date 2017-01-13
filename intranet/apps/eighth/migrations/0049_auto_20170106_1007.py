# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-06 15:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import intranet.utils.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eighth', '0048_auto_20161006_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='EighthWaitlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified_time', models.DateTimeField(auto_now=True, null=True)),
                ('time', models.DateTimeField(auto_now=True)),
                ('scheduled_activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                         related_name='eighthwaitlist_set', to='eighth.EighthScheduledActivity')),
                ('user', models.ForeignKey(on_delete=intranet.utils.deletion.set_historical_user, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='eighthscheduledactivity',
            name='waitlist',
            field=models.ManyToManyField(related_name='eighthscheduledactivity_scheduledactivity_set',
                                         through='eighth.EighthWaitlist', to=settings.AUTH_USER_MODEL),
        ),
    ]