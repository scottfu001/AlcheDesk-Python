# Generated by Django 3.2.3 on 2021-05-17 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_chaneg_properties_of_updated_at_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='log',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='log',
        ),
        migrations.RemoveField(
            model_name='driverpack',
            name='log',
        ),
        migrations.RemoveField(
            model_name='element',
            name='html_position_x',
        ),
        migrations.RemoveField(
            model_name='element',
            name='html_position_y',
        ),
        migrations.RemoveField(
            model_name='element',
            name='log',
        ),
        migrations.RemoveField(
            model_name='instruction',
            name='log',
        ),
        migrations.RemoveField(
            model_name='instructionoverwrite',
            name='log',
        ),
        migrations.RemoveField(
            model_name='instructionresult',
            name='log',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='log',
        ),
        migrations.RemoveField(
            model_name='project',
            name='log',
        ),
        migrations.RemoveField(
            model_name='run',
            name='log',
        ),
        migrations.RemoveField(
            model_name='runexecutioninfo',
            name='driver_pack_name',
        ),
        migrations.RemoveField(
            model_name='runexecutioninfo',
            name='run_name',
        ),
        migrations.RemoveField(
            model_name='runexecutioninfo',
            name='test_case_name',
        ),
        migrations.RemoveField(
            model_name='runexecutioninfo',
            name='test_case_overwrite_name',
        ),
        migrations.RemoveField(
            model_name='runset',
            name='log',
        ),
        migrations.RemoveField(
            model_name='runsetresult',
            name='log',
        ),
        migrations.RemoveField(
            model_name='section',
            name='log',
        ),
        migrations.RemoveField(
            model_name='systemrequirementpack',
            name='log',
        ),
        migrations.RemoveField(
            model_name='template',
            name='log',
        ),
        migrations.RemoveField(
            model_name='template',
            name='mode',
        ),
        migrations.RemoveField(
            model_name='testcase',
            name='log',
        ),
        migrations.RemoveField(
            model_name='testcaseoverwrite',
            name='log',
        ),
        migrations.RemoveField(
            model_name='testcasesharefolder',
            name='log',
        ),
        migrations.AlterField(
            model_name='application',
            name='version',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='driver_type',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='version',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='driverpack',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='locator_value',
            field=models.CharField(max_length=260, unique=True),
        ),
        migrations.AlterField(
            model_name='elementlocator',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='emailnotificationtarget',
            name='email_address',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='file',
            name='type',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='instruction',
            name='driver_type',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='instructionresult',
            name='action',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='instructiontype',
            name='driver_type',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='subject',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='version',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='run',
            name='trigger_source',
            field=models.GenericIPAddressField(unpack_ipv4=True),
        ),
        migrations.AlterField(
            model_name='runexecutioninfo',
            name='trigger_source',
            field=models.GenericIPAddressField(unpack_ipv4=True),
        ),
        migrations.AlterField(
            model_name='runset',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='runsetresult',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='template',
            name='type',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='project_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
