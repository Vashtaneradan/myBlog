# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 11:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='usermame',
            new_name='username',
        ),
    ]
