# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-01 08:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('committees', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='legislator_committees',
            unique_together=set([('legislator', 'committee', 'ad', 'session')]),
        ),
    ]
