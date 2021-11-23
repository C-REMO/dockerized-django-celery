# Generated by Django 3.2 on 2021-11-22 22:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AAPL',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('permalink', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('symbol_type', models.PositiveSmallIntegerField(choices=[(1, 'AAPL Symbol Type'), (2, 'TWTR Symbol Type'), (3, 'GOLD Symbol Type'), (4, 'INTC Symbol Type')], default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GOLD',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('permalink', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('symbol_type', models.PositiveSmallIntegerField(choices=[(1, 'AAPL Symbol Type'), (2, 'TWTR Symbol Type'), (3, 'GOLD Symbol Type'), (4, 'INTC Symbol Type')], default=3)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='INTC',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('permalink', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('symbol_type', models.PositiveSmallIntegerField(choices=[(1, 'AAPL Symbol Type'), (2, 'TWTR Symbol Type'), (3, 'GOLD Symbol Type'), (4, 'INTC Symbol Type')], default=4)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TWTR',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_modified', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('permalink', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('symbol_type', models.PositiveSmallIntegerField(choices=[(1, 'AAPL Symbol Type'), (2, 'TWTR Symbol Type'), (3, 'GOLD Symbol Type'), (4, 'INTC Symbol Type')], default=2)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
