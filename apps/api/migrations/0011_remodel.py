# Generated by Django 3.2.3 on 2021-05-16 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='runsetaliasnamemap',
            name='run_set',
        ),
        migrations.RemoveField(
            model_name='testcasedriveraliasmap',
            name='test_case',
        ),
        migrations.RemoveField(
            model_name='testcasedrivertypemap',
            name='test_case',
        ),
        migrations.RemoveField(
            model_name='testcaseinstructiontypemap',
            name='test_case',
        ),
        migrations.RemoveField(
            model_name='instruction',
            name='driver_alias',
        ),
        migrations.AddField(
            model_name='driverpack',
            name='alias',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='testcase',
            name='alias',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='testcase',
            name='driver_types',
            field=models.JSONField(default=list),
        ),
        migrations.RemoveField(
            model_name='runset',
            name='alias',
        ),
        migrations.AddField(
            model_name='runset',
            name='alias',
            field=models.JSONField(default=list),
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='tags',
        ),
        migrations.AddField(
            model_name='testcase',
            name='tags',
            field=models.JSONField(default=list),
        ),
        migrations.DeleteModel(
            name='DriverPackDriverAliasMap',
        ),
        migrations.DeleteModel(
            name='RunSetAliasNameMap',
        ),
        migrations.DeleteModel(
            name='TestCaseDriverAliasMap',
        ),
        migrations.DeleteModel(
            name='TestCaseDriverTypeMap',
        ),
        migrations.DeleteModel(
            name='TestCaseInstructionTypeMap',
        ),
    ]
