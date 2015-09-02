# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('label', models.CharField(unique=True, max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('value', models.TextField(blank=True)),
                ('value_boolean', models.NullBooleanField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('code', models.CharField(unique=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('question', models.TextField()),
                ('kind', models.IntegerField(choices=[(0, 'text field'), (1, 'textarea'), (2, 'radio choices'), (3, 'checkbox field (can select multiple answers'), (4, 'boolean field')])),
                ('help_text', models.TextField(blank=True)),
                ('ordinal', models.IntegerField(blank=True)),
                ('required', models.BooleanField(default=False)),
                ('survey', models.ForeignKey(to='waitinglist.Survey', related_name='questions')),
            ],
            options={
                'ordering': ['ordinal'],
            },
        ),
        migrations.CreateModel(
            name='SurveyQuestionChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('question', models.ForeignKey(to='waitinglist.SurveyQuestion', related_name='choices')),
            ],
        ),
        migrations.CreateModel(
            name='WaitingListEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='email address')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
            ],
            options={
                'verbose_name_plural': 'waiting list entries',
                'verbose_name': 'waiting list entry',
            },
        ),
        migrations.AddField(
            model_name='surveyinstance',
            name='entry',
            field=models.OneToOneField(to='waitinglist.WaitingListEntry'),
        ),
        migrations.AddField(
            model_name='surveyinstance',
            name='survey',
            field=models.ForeignKey(to='waitinglist.Survey', related_name='instances'),
        ),
        migrations.AddField(
            model_name='surveyanswer',
            name='instance',
            field=models.ForeignKey(to='waitinglist.SurveyInstance', related_name='answers'),
        ),
        migrations.AddField(
            model_name='surveyanswer',
            name='question',
            field=models.ForeignKey(to='waitinglist.SurveyQuestion', related_name='answers'),
        ),
        migrations.AlterUniqueTogether(
            name='surveyquestion',
            unique_together=set([('survey', 'question')]),
        ),
    ]
