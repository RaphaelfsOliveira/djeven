# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Inscricao',
        ),
        migrations.RenameField(
            model_name='inscricao',
            old_name='text_area',
            new_name='text_contato',
        ),
    ]
