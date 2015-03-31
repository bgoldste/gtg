# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150331_0447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True, editable=False),
            preserve_default=True,
        ),
    ]
