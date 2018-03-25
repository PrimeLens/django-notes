# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.PositiveIntegerField(default=0)),
                ('link_or_text', models.CharField(max_length=4)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField(default=b'', null=True, blank=True)),
                ('linkout', models.CharField(default=b'', max_length=200, null=True, blank=True)),
                ('num_of_replies', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
