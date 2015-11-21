# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visualization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vis_name', models.CharField(max_length=256)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('last_edit', models.DateTimeField(verbose_name=b'last edited')),
                ('short_description', models.CharField(max_length=256)),
                ('description', models.TextField()),
            ],
        ),
    ]
