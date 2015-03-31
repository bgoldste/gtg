# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_song_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False),
            preserve_default=True,
        ),
    ]
