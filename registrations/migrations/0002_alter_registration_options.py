# Generated by Django 4.0.4 on 2022-05-10 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registration',
            options={'ordering': ['-timestamp']},
        ),
    ]