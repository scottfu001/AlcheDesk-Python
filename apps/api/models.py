from django.db import models
from .choices import Status, LogLevel, ProjectType, RunType, RunSetType, StepLogType, TestCaseType, SystemRequirementType, InstructionColor
from .common import SoftDeleteModel


class Alias(models.Model, SoftDeleteModel):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    comment = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'alias'


class Application(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    parameter = models.JSONField(default=dict)
    version = models.CharField(max_length=255, blank=False,
                               null=False, unique=True)
    project = models.ForeignKey(
        'Project', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'application'
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_name'),
            models.UniqueConstraint(
                fields=['name', 'project'], name='unique_project_application'),
        ]


class Driver(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    comment = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    is_default = models.BooleanField()
    driver_type = models.CharField(max_length=255, blank=False,
                                   null=False, unique=True)
    parameter = models.JSONField(default=dict)
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    version = models.CharField(max_length=255, blank=False,
                               null=False, unique=True)
    property = models.JSONField()
    execution_count = models.BigIntegerField()
    resource_md5 = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        db_table = 'driver'


class DriverPack(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    execution_count = models.BigIntegerField()
    drivers = models.ManyToManyField(Driver)
    comment = models.TextField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_default = models.BooleanField()
    driver_types = models.JSONField(default=list)
    alias = models.JSONField(default=list)

    class Meta:
        db_table = 'driver_pack'


class Element(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    comment = models.TextField(blank=True, null=True)
    locator_value = models.CharField(max_length=260, blank=False,
                                     null=False, unique=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    element_type = models.ForeignKey(
        'ElementType', models.DO_NOTHING, blank=False, null=False)
    element_locator = models.ForeignKey(
        'ElementLocator', models.DO_NOTHING, null=False, blank=False)
    color = models.CharField(max_length=3, blank=False, null=False,
                             choices=InstructionColor.choices, default=InstructionColor.WHITE)
    parameter = models.JSONField(default=dict)
    is_driver = models.BooleanField()
    project = models.ForeignKey(
        'Project', models.DO_NOTHING, blank=True, null=True)
    section = models.ForeignKey(
        'Section', models.DO_NOTHING, blank=True, null=True)
    application = models.ForeignKey(
        Application, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'element'
        constraints = [
            models.UniqueConstraint(
                fields=['name'], name='unique_element_name'),
            models.UniqueConstraint(
                fields=['name', 'section'], name='unique_element_section'),
        ]


class ElementLocator(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)

    class Meta:
        db_table = 'element_locator'


class ElementType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    is_driver = models.BooleanField()
    element_locators = models.ForeignKey(
        ElementLocator, models.DO_NOTHING, null=False, blank=False)

    class Meta:
        db_table = 'element_type'


class EmailNotificationTarget(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    email_address = models.EmailField(max_length=254)
    comment = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)

    class Meta:
        db_table = 'email_notification_target'


class Instruction(models.Model):
    comment = models.TextField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    input = models.TextField(blank=True, null=True)
    element = models.ForeignKey(
        Element, models.DO_NOTHING, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    project = models.ForeignKey(
        'Project', models.DO_NOTHING, blank=True, null=True)
    application = models.ForeignKey(
        Application, models.DO_NOTHING, blank=True, null=True)
    section = models.ForeignKey(
        'Section', models.DO_NOTHING, blank=True, null=True)
    order_index = models.BigIntegerField()
    data = models.JSONField(default=dict)
    color = models.CharField(max_length=3, blank=False, null=False,
                             choices=InstructionColor.choices, default=InstructionColor.WHITE)
    instruction_type = models.ForeignKey('InstructionType', models.DO_NOTHING)
    step_description = models.TextField(blank=True, null=True)
    expected_description = models.TextField(blank=True, null=True)
    test_case = models.ForeignKey(
        'TestCase', models.DO_NOTHING, related_name='test_case')
    ref_test_case = models.ForeignKey(
        'TestCase', models.DO_NOTHING, blank=True, null=True, related_name='ref_test_case')
    instruction_action = models.ForeignKey(
        'InstructionAction', models.DO_NOTHING, blank=True, null=True)
    is_driver = models.BooleanField()
    parameter = models.JSONField(default=dict)
    expected_value = models.TextField(blank=True, null=True)
    resource_md5 = models.CharField(max_length=32, blank=True, null=True)
    element_type = models.ForeignKey(
        ElementType, models.DO_NOTHING, blank=True, null=True)
    driver_type = models.CharField(max_length=255, blank=False,
                                   null=False, unique=True)
    ref_test_case_overwrite = models.ForeignKey(
        'TestCaseOverwrite', models.DO_NOTHING, blank=True, null=True, related_name='ref_test_case_overwrite')
    test_case_share_folder_id = models.BigIntegerField(blank=True, null=True)
    target = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'instruction'


class InstructionAction(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    Instruction_actions = models.ManyToManyField('InstructionAction')

    class Meta:
        db_table = 'instruction_action'


class InstructionOption(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    is_value_required = models.BooleanField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'instruction_option'


class InstructionOverwrite(models.Model):
    id = models.BigAutoField(primary_key=True)
    test_case_overwrite = models.ForeignKey(
        'TestCaseOverwrite', models.DO_NOTHING)
    test_case_id = models.BigIntegerField(blank=True, null=True)
    instruction_id = models.ForeignKey(Instruction, models.DO_NOTHING)
    element = models.ForeignKey(
        Element, models.DO_NOTHING, blank=True, null=True)
    overwrite_fields = models.ForeignKey(
        'InstructionType', models.DO_NOTHING, db_column='overwrite_fields', blank=True, null=True, related_name='overwrite_fields')
    data = models.JSONField(default=dict)
    instruction_type = models.ForeignKey(
        'InstructionType', models.DO_NOTHING, related_name='instruction_type')

    class Meta:
        db_table = 'instruction_overwrite'
        constraints = [
            models.UniqueConstraint(fields=['test_case_overwrite', 'test_case_id',
                                    'instruction_id'], name='unique_overwrite_tes_case_instruction'),
        ]


class InstructionType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    is_driver = models.BooleanField()
    driver_type = models.CharField(max_length=255, blank=False,
                                   null=False, unique=True)
    is_element_required = models.BooleanField()
    virtual_element = models.ForeignKey(
        Element, models.DO_NOTHING, blank=True, null=True)
    overridable_fields = models.TextField(blank=True, null=True)
    element_types = models.ManyToManyField(ElementType)
    instruction_actions = models.ManyToManyField(InstructionAction)

    class Meta:
        db_table = 'instruction_type'


class Notification(models.Model):
    id = models.BigAutoField(primary_key=True)
    subject = models.CharField(max_length=255, blank=False,
                               null=False, unique=True)
    messages = models.TextField(blank=True, null=True)
    attachments = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    deleted_at = models.DateTimeField(blank=True, null=True)
    email_notification_targets = models.ManyToManyField(
        EmailNotificationTarget)

    class Meta:
        db_table = 'notification'


class ExecutionLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    message = models.TextField()
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    log_level = models.CharField(
        max_length=5, blank=False, null=False, choices=LogLevel.choices, default=LogLevel.INFO)
    instruction_result = models.ForeignKey(
        'InstructionResult', models.DO_NOTHING)
    run = models.ForeignKey('Run', models.DO_NOTHING)

    class Meta:
        db_table = 'execution_log'


class File(models.Model):
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    uuid = models.UUIDField()
    parameter = models.JSONField(default=dict)
    type = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    instruction_result = models.ForeignKey(
        'InstructionResult', models.DO_NOTHING, blank=True, null=True)
    uri = models.TextField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    run = models.ForeignKey('Run', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'file'


class InstructionResult(models.Model):
    id = models.BigAutoField(primary_key=True)
    action = models.CharField(max_length=255, blank=False,
                              null=False, unique=True)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    status = models.CharField(max_length=5,
                              blank=False, null=False, choices=Status.choices, default=Status.NEW)
    is_finished = models.BooleanField()
    instruction = models.JSONField(default=dict)
    data = models.JSONField(default=dict)
    run = models.ForeignKey('Run', models.DO_NOTHING)
    start_at = models.DateTimeField(blank=True, null=True)
    end_at = models.DateTimeField(blank=True, null=True)
    logical_order_index = models.CharField(
        max_length=20, blank=True, null=True)
    input_data = models.TextField(blank=True, null=True)
    input_type = models.CharField(max_length=50, blank=True, null=True)
    input_parameter = models.JSONField(default=dict)
    output_data = models.TextField(blank=True, null=True)
    output_type = models.CharField(max_length=50, blank=True, null=True)
    output_parameter = models.JSONField(default=dict)
    expected_value = models.TextField(blank=True, null=True)
    return_value = models.TextField(blank=True, null=True)
    is_overwrite = models.BooleanField(blank=True, null=True)
    target = models.TextField(blank=True, null=True)
    instruction_options = models.ManyToManyField(InstructionOption)
    instruction_option_log = models.TextField(blank=True, null=True)
    result_overwritten = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'instruction_result'


class StepLog(models.Model):
    message = models.TextField()
    id = models.BigAutoField(primary_key=True)
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    instruction_result = models.ForeignKey(
        InstructionResult, models.DO_NOTHING)
    step_log_type = models.CharField(max_length=7,
                                     blank=False, null=False, choices=StepLogType.choices, default=StepLogType.INSTRUCTION)

    class Meta:
        db_table = 'step_log'


class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    project_type = models.CharField(max_length=5,
                                    blank=False, null=False, choices=ProjectType.choices, default=ProjectType.GROUP)
    version = models.CharField(max_length=255, blank=False,
                               null=False, unique=True)

    class Meta:
        db_table = 'project'
        constraints = [
            models.UniqueConstraint(
                fields=['name'], name='unique_project_name'),
            models.UniqueConstraint(
                fields=['name', 'version'], name='unique_name_version'),
        ]


class ProjectExecutionInfo(models.Model):
    project = models.OneToOneField(
        Project, models.DO_NOTHING, primary_key=True)
    project_name = models.CharField(max_length=255, blank=False,
                                    null=False, unique=True)
    project_created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    project_updated_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    active_test_case_number = models.IntegerField()
    executed_test_case_number = models.IntegerField()
    active_test_case_ids = models.JSONField(default=list)
    executed_test_case_ids = models.JSONField(default=list)
    passed_test_case_ids = models.JSONField(default=list)
    passed_test_case_number = models.IntegerField()
    total_test_case_number = models.IntegerField()
    test_case_ids = models.JSONField(default=list)
    project_deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'project_execution_info'


class ProjectReportInfo(models.Model):
    project = models.OneToOneField(
        Project, models.DO_NOTHING, primary_key=True)
    project_name = models.CharField(max_length=255, blank=False,
                                    null=False, unique=True)
    project_created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    active_test_case_number = models.IntegerField()
    total_run_number = models.BigIntegerField()
    total_execution_time = models.BigIntegerField()
    executed_test_case_number = models.IntegerField()
    failed_test_case_number = models.IntegerField()
    passed_test_case_number = models.IntegerField()
    pass_rate = models.DecimalField(max_digits=5, decimal_places=2)
    fail_rate = models.DecimalField(max_digits=5, decimal_places=2)
    total_test_case_number = models.IntegerField()

    class Meta:
        db_table = 'project_report_info'


class Run(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)

    status = models.CharField(max_length=5,
                              blank=False, null=False, choices=Status.choices, default=Status.NEW)
    is_finished = models.BooleanField()
    test_case = models.JSONField(default=dict)
    parameter = models.JSONField(default=dict)
    start_at = models.DateTimeField(blank=True, null=True)
    end_at = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField()
    timeout = models.IntegerField()
    run_set_result = models.ForeignKey(
        'RunSetResult', models.DO_NOTHING, blank=True, null=True, related_name='run_set_result')
    driver_pack = models.JSONField(blank=True, null=True)
    driver_pack_id = models.BigIntegerField(blank=True, null=True)
    is_recorded = models.BigIntegerField(blank=True, null=True)
    test_case_overwrite = models.JSONField(blank=True, null=True)
    test_case_overwrite_id = models.BigIntegerField(blank=True, null=True)
    trigger_source = models.GenericIPAddressField(
        protocol='both', unpack_ipv4=True)
    drivers = models.JSONField(blank=True, null=True)
    uuid = models.UUIDField()
    test_case_uuid = models.UUIDField(blank=True, null=True)
    singleton = models.BooleanField()
    executable_instruction_number = models.BigIntegerField(
        blank=True, null=True)
    system_requirements = models.JSONField(blank=True, null=True)
    system_requirement_pack = models.JSONField(
        db_column='system_requirement_pack', blank=True, null=True)
    result_overwritten = models.IntegerField()
    project = models.ForeignKey(Project, models.DO_NOTHING)

    class Meta:
        db_table = 'run'


class RunExecutionInfo(models.Model):
    run = models.OneToOneField(Run, models.DO_NOTHING, primary_key=True)
    run_type = models.CharField(max_length=3,
                                blank=False, null=False, choices=RunType.choices, default=RunType.PRODUCTION)
    status = models.CharField(max_length=5,
                              blank=False, null=False, choices=Status.choices, default=Status.NEW)
    run_created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    run_updated_at = models.DateTimeField(blank=True, null=True)
    test_case_id = models.BigIntegerField()
    run_set_result_id = models.BigIntegerField(blank=True, null=True)
    executable_instruction_number = models.IntegerField()
    instruction_executed_count = models.BigIntegerField()
    instruction_pass_count = models.BigIntegerField()
    trigger_source = models.GenericIPAddressField(
        protocol='both', unpack_ipv4=True)
    driver_pack_md5 = models.UUIDField(blank=True, null=True)
    test_case_overwrite_md5 = models.UUIDField(blank=True, null=True)
    test_case_md5 = models.UUIDField(blank=True, null=True)
    run_priority = models.BigIntegerField(blank=True, null=True)
    run_result_overwritten = models.IntegerField()
    run_project = models.ForeignKey(Project, models.DO_NOTHING)
    instruction_fail_count = models.IntegerField()
    is_finished = models.BooleanField()
    run_start_at = models.DateTimeField(blank=True, null=True)
    run_end_at = models.DateTimeField(blank=True, null=True)
    duration = models.BigIntegerField()

    class Meta:
        db_table = 'run_execution_info'


class RunSet(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    run_set_type = models.CharField(max_length=3,
                                    blank=False, null=False, choices=RunSetType.choices, default=RunSetType.INTERNAL)
    priority = models.IntegerField()
    uuid = models.UUIDField()
    test_cases = models.ManyToManyField('TestCase')
    alias = models.JSONField(default=list)
    notifications = models.ManyToManyField(Notification)

    class Meta:
        db_table = 'run_set'
        unique_together = (('id', 'uuid'),)


class RunSetResult(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    start_at = models.DateTimeField(blank=True, null=True)
    end_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=5,
                              blank=False, null=False, choices=Status.choices, default=Status.NEW)
    run_set_type = models.BigIntegerField(
        blank=False, null=False, choices=RunSetType.choices, default=RunSetType.INTERNAL)
    run_set = models.ForeignKey(
        RunSet, models.DO_NOTHING, blank=True, null=True)
    is_finished = models.BooleanField()
    comment = models.TextField(blank=True, null=True)
    run = models.JSONField(blank=True, null=True)
    uuid = models.UUIDField()
    total_run_number = models.IntegerField()
    passed_run_number = models.IntegerField()
    failed_run_number = models.IntegerField()
    run_ids = models.JSONField(default=list)
    passed_run_ids = models.JSONField(default=list)
    failed_run_ids = models.JSONField(default=list)

    class Meta:
        db_table = 'run_set_result'


class Section(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    application = models.ForeignKey(Application, models.DO_NOTHING)
    project = models.ForeignKey(Project, models.DO_NOTHING)

    class Meta:
        db_table = 'section'
        constraints = [
            models.UniqueConstraint(
                fields=['name'], name='unique_section_name'),
            models.UniqueConstraint(
                fields=['name', 'application'], name='unique_name_application'),
        ]


class SystemRequirement(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    comment = models.TextField(blank=True, null=True)
    system_requirement_type = models.CharField(max_length=4,
                                               blank=False, null=False, choices=SystemRequirementType.choices, default=SystemRequirementType.CORE)
    value = models.BigIntegerField()

    class Meta:
        db_table = 'system_requirement'
        unique_together = (('id', 'system_requirement_type'),)


class SystemRequirementPack(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    execution_count = models.BigIntegerField()
    comment = models.TextField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_default = models.BooleanField()
    system_requirements = models.ManyToManyField(SystemRequirement)

    class Meta:
        db_table = 'system_requirement_pack'


class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    comment = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)

    class Meta:
        db_table = 'tag'


class Template(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    type = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    content = models.TextField()
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'template'


class TestCase(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    is_flagged = models.BooleanField()
    comment = models.TextField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField()
    test_case_type = models.CharField(max_length=5,
                                      blank=False, null=False, choices=TestCaseType.choices, default=TestCaseType.JSON)
    project = models.ForeignKey(Project, models.DO_NOTHING)
    timeout = models.IntegerField()
    ref_run_set = models.ForeignKey(
        RunSet, models.DO_NOTHING, blank=True, null=True)
    resource_md5 = models.CharField(max_length=32, blank=True, null=True)
    parameter = models.JSONField(default=dict)
    uuid = models.UUIDField()
    singleton = models.BooleanField()
    project_name = models.CharField(max_length=255, blank=False,
                                    null=False, unique=True)
    tags = models.JSONField(default=list)
    alias = models.JSONField(default=list)
    driver_types = models.JSONField(default=list)

    class Meta:
        db_table = 'test_case'
        constraints = [
            models.UniqueConstraint(
                fields=['name'], name='unique_test_case_name'),
            models.UniqueConstraint(
                fields=['name', 'project'], name='unique_name_project'),
        ]


class TestCaseExecutionInfo(models.Model):
    test_case_id = models.BigIntegerField(primary_key=True)
    test_case_name = models.CharField(max_length=255, blank=False,
                                      null=False, unique=True)
    test_case_created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    total_run_count = models.BigIntegerField()
    latest_run_status_id = models.CharField(max_length=5,
                                            blank=False, null=False, choices=Status.choices, default=Status.NEW)
    latest_run_updated_at = models.DateTimeField(blank=True, null=True)
    latest_run_instruction_executed_count = models.BigIntegerField(
        blank=True, null=True)
    latest_run_instruction_pass_count = models.BigIntegerField(
        blank=True, null=True)
    latest_run_trigger_source = models.BigIntegerField(blank=True, null=True)
    latest_run_created_at = models.DateTimeField(blank=True, null=True)
    latest_run = models.ForeignKey(
        Run, models.DO_NOTHING, blank=True, null=True, related_name='latest_run')
    latest_run_executable_instruction_number = models.BigIntegerField(
        blank=True, null=True)
    latest_run_instruction_fail_count = models.IntegerField()
    test_case_deleted_at = models.DateTimeField(blank=True, null=True)
    test_case_project_id = models.BigIntegerField()

    class Meta:
        db_table = 'test_case_execution_info'


class TestCaseOption(models.Model):
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    id = models.BigAutoField(primary_key=True)
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    comment = models.TextField(blank=True, null=True)
    is_value_required = models.BooleanField()

    class Meta:
        db_table = 'test_case_option'


class TestCaseOverwrite(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    test_case = models.ForeignKey(TestCase, models.DO_NOTHING)
    deleted_at = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'test_case_overwrite'
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'test_case'], name='unique_name_test_case'),
        ]


class TestCaseShareFolder(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    description = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    deleted_at = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    test_cases = models.ForeignKey(TestCase, models.DO_NOTHING)

    class Meta:
        db_table = 'test_case_share_folder'
        constraints = [
            models.UniqueConstraint(
                fields=['name'], name='unique_test_case_share_folder_name'),
        ]
