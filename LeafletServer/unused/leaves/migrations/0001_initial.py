# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 00:53
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leaflets', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Leaf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaf_type', models.TextField(default='text', max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('content', django.contrib.postgres.fields.jsonb.JSONField()),
                ('leaflet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leaves', to='leaflets.Leaflet')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leaves', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]