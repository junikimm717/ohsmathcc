# Generated by Django 4.0.4 on 2022-05-19 22:37

from django.db import migrations
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('times', '0002_alter_event_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': [django.db.models.expressions.OrderBy(django.db.models.expressions.F('date'), nulls_first=True)]},
        ),
    ]
