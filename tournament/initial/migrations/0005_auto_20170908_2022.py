# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-08 20:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('initial', '0004_season'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('win', models.IntegerField()),
                ('drawn', models.IntegerField()),
                ('lost', models.IntegerField()),
                ('goals_for', models.IntegerField()),
                ('goals_against', models.IntegerField()),
                ('goal_difference', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='initial.Season')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='initial.Team')),
            ],
        ),
        migrations.AddField(
            model_name='club',
            name='logo',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/'),
        ),
    ]