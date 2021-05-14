# Generated by Django 3.2.3 on 2021-05-14 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devfile',
            name='file_type',
        ),
        migrations.RemoveField(
            model_name='devfile',
            name='instruction_result',
        ),
        migrations.RemoveField(
            model_name='devfile',
            name='run',
        ),
        migrations.RemoveField(
            model_name='devfile',
            name='run_type',
        ),
        migrations.RemoveField(
            model_name='devinstructionresult',
            name='instruction_0',
        ),
        migrations.RemoveField(
            model_name='devinstructionresult',
            name='run',
        ),
        migrations.RemoveField(
            model_name='devinstructionresult',
            name='run_type',
        ),
        migrations.RemoveField(
            model_name='devinstructionresult',
            name='status',
        ),
        migrations.RemoveField(
            model_name='devsteplog',
            name='instruction_result',
        ),
        migrations.RemoveField(
            model_name='devsteplog',
            name='run_type',
        ),
        migrations.RemoveField(
            model_name='devsteplog',
            name='step_log_type',
        ),
        migrations.RemoveField(
            model_name='testcaseexecutioninfo',
            name='latest_dev_run',
        ),
        migrations.RemoveField(
            model_name='testcaseexecutioninfo',
            name='latest_dev_run_created_at',
        ),
        migrations.RemoveField(
            model_name='testcaseexecutioninfo',
            name='latest_dev_run_executable_instruction_number',
        ),
        migrations.RemoveField(
            model_name='testcaseexecutioninfo',
            name='latest_dev_run_instruction_executed_count',
        ),
        migrations.RemoveField(
            model_name='testcaseexecutioninfo',
            name='latest_dev_run_instruction_pass_count',
        ),
        migrations.RemoveField(
            model_name='testcaseexecutioninfo',
            name='latest_dev_run_status_id',
        ),
        migrations.RemoveField(
            model_name='testcaseexecutioninfo',
            name='latest_dev_run_trigger_source',
        ),
        migrations.RemoveField(
            model_name='testcaseexecutioninfo',
            name='latest_dev_run_updated_at',
        ),
        migrations.RemoveField(
            model_name='testcaseexecutioninfo',
            name='total_dev_run_count',
        ),
        migrations.DeleteModel(
            name='DevExecutionLog',
        ),
        migrations.DeleteModel(
            name='DevFile',
        ),
        migrations.DeleteModel(
            name='DevInstructionResult',
        ),
        migrations.DeleteModel(
            name='DevStepLog',
        ),
    ]