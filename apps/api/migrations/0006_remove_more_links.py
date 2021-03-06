# Generated by Django 3.2.3 on 2021-05-14 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_tables'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContentType',
        ),
        migrations.AlterUniqueTogether(
            name='module',
            unique_together=None,
        ),
        migrations.AlterUniqueTogether(
            name='notificationemailnotificationtargetlink',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='notificationemailnotificationtargetlink',
            name='email_notification_target',
        ),
        migrations.RemoveField(
            model_name='notificationemailnotificationtargetlink',
            name='notification',
        ),
        migrations.AlterUniqueTogether(
            name='runsetaliaslink',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='runsetaliaslink',
            name='alias',
        ),
        migrations.RemoveField(
            model_name='runsetaliaslink',
            name='run_set',
        ),
        migrations.RemoveField(
            model_name='runsetjoblink',
            name='run_set',
        ),
        migrations.AlterUniqueTogether(
            name='runsetnotificationlink',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='runsetnotificationlink',
            name='notification',
        ),
        migrations.RemoveField(
            model_name='runsetnotificationlink',
            name='run_set',
        ),
        migrations.RemoveField(
            model_name='runsetresultjoblink',
            name='run_set_result',
        ),
        migrations.AlterUniqueTogether(
            name='runsettestcaselink',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='runsettestcaselink',
            name='driver_pack',
        ),
        migrations.RemoveField(
            model_name='runsettestcaselink',
            name='ref_run_set',
        ),
        migrations.RemoveField(
            model_name='runsettestcaselink',
            name='run_set',
        ),
        migrations.RemoveField(
            model_name='runsettestcaselink',
            name='system_requirement_pack',
        ),
        migrations.RemoveField(
            model_name='runsettestcaselink',
            name='test_case',
        ),
        migrations.RemoveField(
            model_name='runsettestcaselink',
            name='test_case_overwrite',
        ),
        migrations.RemoveField(
            model_name='runtasklink',
            name='run',
        ),
        migrations.AlterUniqueTogether(
            name='systemrequirementpacksystemrequirementlink',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='systemrequirementpacksystemrequirementlink',
            name='system_requirement',
        ),
        migrations.RemoveField(
            model_name='systemrequirementpacksystemrequirementlink',
            name='system_requirement_pack',
        ),
        migrations.AlterUniqueTogether(
            name='testcasemodulelink',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='testcasemodulelink',
            name='module',
        ),
        migrations.RemoveField(
            model_name='testcasemodulelink',
            name='test_case',
        ),
        migrations.RemoveField(
            model_name='testcasetasklink',
            name='test_case',
        ),
        migrations.RemoveField(
            model_name='run',
            name='run_set_test_case_link_id',
        ),
        migrations.RemoveField(
            model_name='runset',
            name='aliases',
        ),
        migrations.AddField(
            model_name='instructionaction',
            name='Instruction_actions',
            field=models.ManyToManyField(to='api.InstructionAction'),
        ),
        migrations.AddField(
            model_name='notification',
            name='email_notification_targets',
            field=models.ManyToManyField(to='api.EmailNotificationTarget'),
        ),
        migrations.AddField(
            model_name='runset',
            name='alias',
            field=models.ManyToManyField(to='api.Alias'),
        ),
        migrations.AddField(
            model_name='runset',
            name='notifications',
            field=models.ManyToManyField(to='api.Notification'),
        ),
        migrations.AddField(
            model_name='runset',
            name='test_cases',
            field=models.ManyToManyField(to='api.TestCase'),
        ),
        migrations.AddField(
            model_name='systemrequirementpack',
            name='system_requirements',
            field=models.ManyToManyField(to='api.SystemRequirement'),
        ),
        migrations.DeleteModel(
            name='InstructionActionInstructionOptionLink',
        ),
        migrations.DeleteModel(
            name='Module',
        ),
        migrations.DeleteModel(
            name='NotificationEmailNotificationTargetLink',
        ),
        migrations.DeleteModel(
            name='RunSetAliasLink',
        ),
        migrations.DeleteModel(
            name='RunSetJobLink',
        ),
        migrations.DeleteModel(
            name='RunSetNotificationLink',
        ),
        migrations.DeleteModel(
            name='RunSetResultJobLink',
        ),
        migrations.DeleteModel(
            name='RunSetTestCaseLink',
        ),
        migrations.DeleteModel(
            name='RunTaskLink',
        ),
        migrations.DeleteModel(
            name='SystemRequirementPackSystemRequirementLink',
        ),
        migrations.DeleteModel(
            name='TestCaseModuleLink',
        ),
        migrations.DeleteModel(
            name='TestCaseTaskLink',
        ),
    ]
