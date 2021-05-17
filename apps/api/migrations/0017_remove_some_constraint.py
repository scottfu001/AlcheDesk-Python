# Generated by Django 3.2.3 on 2021-05-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_set_now_to_dates'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='application',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='element',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='instruction',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='instructionoverwrite',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='instructiontype',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='run',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='runsetresult',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='section',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='testcase',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='testcaseoverwrite',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='testcasesharefolder',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='application',
            constraint=models.UniqueConstraint(
                fields=('name',), name='unique_name'),
        ),
        migrations.AddConstraint(
            model_name='application',
            constraint=models.UniqueConstraint(
                fields=('name', 'project'), name='unique_project_application'),
        ),
        migrations.AddConstraint(
            model_name='element',
            constraint=models.UniqueConstraint(
                fields=('name',), name='unique_element_name'),
        ),
        migrations.AddConstraint(
            model_name='element',
            constraint=models.UniqueConstraint(
                fields=('name', 'section'), name='unique_element_section'),
        ),
        migrations.AddConstraint(
            model_name='instructionoverwrite',
            constraint=models.UniqueConstraint(fields=(
                'test_case_overwrite', 'test_case_id', 'instruction_id'), name='unique_overwrite_tes_case_instruction'),
        ),
        migrations.AddConstraint(
            model_name='project',
            constraint=models.UniqueConstraint(
                fields=('name',), name='unique_project_name'),
        ),
        migrations.AddConstraint(
            model_name='project',
            constraint=models.UniqueConstraint(
                fields=('name', 'version'), name='unique_name_version'),
        ),
        migrations.AddConstraint(
            model_name='section',
            constraint=models.UniqueConstraint(
                fields=('name',), name='unique_section_name'),
        ),
        migrations.AddConstraint(
            model_name='section',
            constraint=models.UniqueConstraint(
                fields=('name', 'application'), name='unique_name_application'),
        ),
        migrations.AddConstraint(
            model_name='testcase',
            constraint=models.UniqueConstraint(
                fields=('name',), name='unique_test_case_name'),
        ),
        migrations.AddConstraint(
            model_name='testcase',
            constraint=models.UniqueConstraint(
                fields=('name', 'project'), name='unique_name_project'),
        ),
        migrations.AddConstraint(
            model_name='testcaseoverwrite',
            constraint=models.UniqueConstraint(
                fields=('name', 'test_case'), name='unique_name_test_case'),
        ),
        migrations.AddConstraint(
            model_name='testcasesharefolder',
            constraint=models.UniqueConstraint(
                fields=('name',), name='unique_test_case_share_folder_name'),
        ),
        migrations.RemoveField(
            model_name='run',
            name='test_case_0',
        ),
    ]
