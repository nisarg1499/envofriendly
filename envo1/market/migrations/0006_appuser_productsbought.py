# Generated by Django 3.0.3 on 2020-02-09 01:11

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_remove_appuser_productsbought'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='productsBought',
            field=django.contrib.postgres.fields.jsonb.JSONField(default='{}'),
        ),
    ]