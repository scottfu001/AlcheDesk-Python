# Generated by Django 3.2.3 on 2021-05-16 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_remodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Property',
        ),
        migrations.DeleteModel(
            name='Resource',
        ),
    ]
