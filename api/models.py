# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models.deletion import DO_NOTHING
from .choices import Status, LogLevel, ProjectType, RunType, RunSetType, StepLogType, TestCaseType, SystemRequirementType


class Alias(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)
    comment = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    is_deleted = models.BooleanField()

    class Meta:
        db_table = 'alias'


class Application(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_deleted = models.BooleanField()
    log = models.TextField(blank=True, null=True)
    parameter = models.JSONField()
    version = models.TextField(blank=True, null=True)
    project = models.ForeignKey(
        'Project', models.DO_NOTHING, blank=True, null=True)
    copy_from_id = models.ForeignKey(
        'self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'application'
        unique_together = (('id', 'name'), ('id', 'project'),
                           ('name', 'project'),)


class Color(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)

    class Meta:
        db_table = 'color'


class Driver(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    comment = models.TextField(blank=True, null=True)
    is_active = models.BooleanField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    is_default = models.BooleanField()
    driver_type = models.ForeignKey('DriverType', models.DO_NOTHING)
    parameter = models.JSONField()
    vendor_name = models.ForeignKey(
        'DriverVendor', models.DO_NOTHING, db_column='vendor_name')
    version = models.TextField(blank=True, null=True)
    property = models.JSONField()
    is_predefined = models.BooleanField()
    execution_count = models.BigIntegerField()
    copy_from_id = models.ForeignKey(
        'self', models.DO_NOTHING, blank=True, null=True)
    log = models.TextField(blank=True, null=True)
    resource_md5 = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        db_table = 'driver'
    #     unique_together = (('driver_type', 'is_default'),)


class DriverPack(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    execution_count = models.BigIntegerField()
    drivers = models.ManyToManyField(Driver)
    comment = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField()
    log = models.TextField(blank=True, null=True)
    is_default = models.BooleanField()
    copy_from_id = models.ForeignKey(
        'self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'driver_pack'


class DriverPackDriverAliasMap(models.Model):
    id = models.BigAutoField(primary_key=True)
    driver_pack = models.OneToOneField(DriverPack, models.DO_NOTHING)
    driver_aliases = models.JSONField()

    class Meta:
        db_table = 'driver_pack_driver_alias_map'


class DriverPackDriverTypeMap(models.Model):
    id = models.BigAutoField(primary_key=True)
    driver_pack = models.OneToOneField(DriverPack, models.DO_NOTHING)
    driver_types = models.JSONField()

    class Meta:
        db_table = 'driver_pack_driver_type_map'


class DriverProperty(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    driver_vendor = models.ForeignKey('DriverVendor', models.DO_NOTHING)
    default_value = models.TextField()
    default_action = models.TextField()
    description = models.TextField()
    value_type = models.TextField()
    is_predefined_value_required = models.BooleanField()
    is_active = models.BooleanField()
    is_predefined = models.BooleanField()

    class Meta:
        db_table = 'driver_property'
        unique_together = (('name', 'driver_vendor'),)


class DriverPropertyPredefinedValue(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.TextField()
    driver_property = models.ForeignKey(DriverProperty, models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    is_prefered = models.BooleanField()

    class Meta:
        db_table = 'driver_property_predefined_value'
        unique_together = (('value', 'driver_property'),)


class DriverType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)
    is_multiselectable = models.BooleanField()
    is_active = models.BooleanField()
    is_predefined = models.BooleanField()
    instruction_types = models.ManyToManyField('InstructionType')

    class Meta:
        db_table = 'driver_type'


class DriverVendor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    driver_type = models.ForeignKey(DriverType, models.DO_NOTHING)
    version = models.TextField(blank=True, null=True)
    is_active = models.BooleanField()
    is_predefined = models.BooleanField()

    class Meta:
        db_table = 'driver_vendor'
        unique_together = (('name', 'driver_type', 'version'),)


class Element(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    comment = models.TextField(blank=True, null=True)
    locator_value = models.TextField(blank=True, null=True)
    html_position_x = models.TextField(blank=True, null=True)
    html_position_y = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    log = models.TextField(blank=True, null=True)
    element_type = models.ForeignKey(
        'ElementType', models.DO_NOTHING, blank=False, null=False)
    element_locator = models.ForeignKey(
        'ElementLocator', models.DO_NOTHING, null=False, blank=False)
    color = models.ForeignKey(Color, models.DO_NOTHING)
    parameter = models.JSONField()
    is_driver = models.BooleanField()
    project = models.ForeignKey(
        'Project', models.DO_NOTHING, blank=True, null=True)
    section = models.ForeignKey(
        'Section', models.DO_NOTHING, blank=True, null=True)
    copy_from_id = models.ForeignKey(
        'self', models.DO_NOTHING, blank=True, null=True)
    application = models.ForeignKey(
        Application, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'element'
        unique_together = (('id', 'element_type'),
                           ('id', 'name'), ('name', 'section'),)


class ElementLocator(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)
    is_active = models.BooleanField()
    is_predefined = models.BooleanField()

    class Meta:
        db_table = 'element_locator'


class ElementType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)
    is_active = models.BooleanField()
    is_driver = models.BooleanField()
    element_locators = models.ForeignKey(
        ElementLocator, models.DO_NOTHING, null=False, blank=False)

    class Meta:
        db_table = 'element_type'


class EmailNotificationTarget(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    email_address = models.TextField()
    comment = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'email_notification_target'


class FileType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)
    is_active = models.BooleanField()
    is_predefined = models.BooleanField()

    class Meta:
        db_table = 'file_type'


class Group(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)
    is_predefined = models.BooleanField()
    is_active = models.BooleanField()

    class Meta:
        db_table = 'group'


class Instruction(models.Model):
    comment = models.TextField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    input = models.TextField(blank=True, null=True)
    element = models.ForeignKey(
        Element, models.DO_NOTHING, blank=True, null=True)
    is_deleted = models.BooleanField()
    project = models.ForeignKey(
        'Project', models.DO_NOTHING, blank=True, null=True)
    application = models.ForeignKey(
        Application, models.DO_NOTHING, blank=True, null=True)
    section = models.ForeignKey(
        'Section', models.DO_NOTHING, blank=True, null=True)
    order_index = models.BigIntegerField()
    log = models.TextField(blank=True, null=True)
    data = models.JSONField()
    color = models.ForeignKey(Color, models.DO_NOTHING)
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
    parameter = models.JSONField()
    copy_from_id = models.ForeignKey(
        'self', models.DO_NOTHING, blank=True, null=True)
    expected_value = models.TextField(blank=True, null=True)
    resource_md5 = models.CharField(max_length=32, blank=True, null=True)
    element_type = models.ForeignKey(
        ElementType, models.DO_NOTHING, blank=True, null=True)
    driver_type = models.ForeignKey(
        DriverType, models.DO_NOTHING, blank=True, null=True)
    ref_test_case_overwrite = models.ForeignKey(
        'TestCaseOverwrite', models.DO_NOTHING, blank=True, null=True, related_name='ref_test_case_overwrite')
    test_case_share_folder_id = models.BigIntegerField(blank=True, null=True)
    driver_alias = models.TextField(blank=True, null=True)
    target = models.TextField(blank=True, null=True)
    ref_test_case_overwrite_name = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'instruction'
        unique_together = (('id', 'element', 'instruction_type', 'test_case'), ('id', 'ref_test_case'), ('id', 'test_case_share_folder_id'),
                           ('id', 'application'), ('id', 'section'), ('id', 'element'), ('id', 'ref_test_case_overwrite'),)


class InstructionAction(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)
    is_active = models.BooleanField()
    is_predefined = models.BooleanField()
    Instruction_actions = models.ManyToManyField('InstructionAction')

    class Meta:
        db_table = 'instruction_action'


class InstructionOption(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    is_predefined = models.BooleanField()
    is_value_required = models.BooleanField()
    comment = models.TextField(blank=True, null=True)
    is_active = models.BooleanField()

    class Meta:
        db_table = 'instruction_option'


class InstructionOptionMap(models.Model):
    instruction_option = models.OneToOneField(
        InstructionOption, models.DO_NOTHING, primary_key=True)
    instruction_action_ids = models.JSONField()
    element_type_ids = models.JSONField()

    class Meta:
        db_table = 'instruction_option_map'


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
    data = models.JSONField()
    instruction_type = models.ForeignKey(
        'InstructionType', models.DO_NOTHING, related_name='instruction_type')
    copy_from_id = models.ForeignKey(
        'self', models.DO_NOTHING, blank=True, null=True)
    log = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'instruction_overwrite'
        unique_together = (('test_case_overwrite', 'instruction_id',
                           'element'), ('test_case_overwrite', 'test_case_id', 'instruction_id'),)


class InstructionType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)
    is_active = models.BooleanField()
    is_predefined = models.BooleanField()
    is_driver = models.BooleanField()
    driver_type = models.ForeignKey(
        DriverType, models.DO_NOTHING, blank=True, null=True)
    is_element_required = models.BooleanField()
    virtual_element = models.ForeignKey(
        Element, models.DO_NOTHING, blank=True, null=True)
    overridable_fields = models.TextField(blank=True, null=True)
    element_types = models.ManyToManyField(ElementType)
    instruction_actions = models.ManyToManyField(InstructionAction)

    class Meta:
        db_table = 'instruction_type'
        unique_together = (('id', 'overridable_fields'), ('id', 'is_driver'),)


class Notification(models.Model):
    id = models.BigAutoField(primary_key=True)
    subject = models.TextField(blank=True, null=True)
    messages = models.TextField(blank=True, null=True)
    attachments = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    log = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    is_deleted = models.BooleanField()
    email_notification_targets = models.ManyToManyField(
        EmailNotificationTarget)

    class Meta:
        db_table = 'notification'


class ExecutionLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    message = models.TextField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    log_level = models.CharField(
        max_length=5, blank=False, null=False, choices=LogLevel.choices, default=LogLevel.INFO)
    instruction_result = models.ForeignKey(
        'InstructionResult', models.DO_NOTHING)
    run = models.ForeignKey('Run', models.DO_NOTHING)

    class Meta:
        db_table = 'execution_log'


class File(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField()
    parameter = models.JSONField()
    file_type = models.ForeignKey(FileType, models.DO_NOTHING)
    instruction_result = models.ForeignKey(
        'InstructionResult', models.DO_NOTHING, blank=True, null=True)
    uri = models.TextField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    run = models.ForeignKey('Run', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'file'


class InstructionResult(models.Model):
    id = models.BigAutoField(primary_key=True)
    action = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.CharField(max_length=5,
                              blank=False, null=False, choices=Status.choices, default=Status.NEW)
    log = models.TextField(blank=True, null=True)
    is_finished = models.BooleanField()
    instruction = models.JSONField()
    data = models.JSONField()
    run = models.ForeignKey('Run', models.DO_NOTHING)

    start_at = models.DateTimeField(blank=True, null=True)
    end_at = models.DateTimeField(blank=True, null=True)
    logical_order_index = models.CharField(
        max_length=20, blank=True, null=True)
    input_data = models.TextField(blank=True, null=True)
    input_type = models.CharField(max_length=50, blank=True, null=True)
    input_parameter = models.JSONField()
    output_data = models.TextField(blank=True, null=True)
    output_type = models.CharField(max_length=50, blank=True, null=True)
    output_parameter = models.JSONField()
    expected_value = models.TextField(blank=True, null=True)
    return_value = models.TextField(blank=True, null=True)
    is_overwrite = models.BooleanField(blank=True, null=True)
    target = models.TextField(blank=True, null=True)
    # This field type is a guess.
    instruction_options = models.TextField(blank=True, null=True)
    instruction_option_log = models.TextField(blank=True, null=True)
    result_overwritten = models.IntegerField()
    # Field renamed because of name conflict.
    instruction_0 = models.ForeignKey(
        Instruction, models.DO_NOTHING, db_column='instruction_id', blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'instruction_result'


class StepLog(models.Model):
    message = models.TextField()
    id = models.BigAutoField(primary_key=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    instruction_result = models.ForeignKey(
        InstructionResult, models.DO_NOTHING)
    step_log_type = models.CharField(max_length=7,
                                     blank=False, null=False, choices=StepLogType.choices, default=StepLogType.INSTRUCTION)

    class Meta:
        db_table = 'step_log'


class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    comment = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField()
    log = models.TextField(blank=True, null=True)
    project_type = models.CharField(max_length=5,
                                    blank=False, null=False, choices=ProjectType.choices, default=ProjectType.GROUP)
    version = models.TextField(blank=True, null=True)
    copy_from_id = models.ForeignKey(
        'self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'project'
        unique_together = (('id', 'name'), ('name', 'version'),)


class ProjectExecutionInfo(models.Model):
    project = models.OneToOneField(
        Project, models.DO_NOTHING, primary_key=True)
    project_name = models.TextField()
    project_created_at = models.DateTimeField()
    project_updated_at = models.DateTimeField()
    active_test_case_number = models.IntegerField()
    executed_test_case_number = models.IntegerField()
    active_test_case_ids = models.JSONField()
    executed_test_case_ids = models.JSONField()
    passed_test_case_ids = models.JSONField()
    passed_test_case_number = models.IntegerField()
    total_test_case_number = models.IntegerField()
    test_case_ids = models.JSONField()
    project_is_deleted = models.BooleanField()

    class Meta:
        db_table = 'project_execution_info'


class ProjectReportInfo(models.Model):
    project = models.OneToOneField(
        Project, models.DO_NOTHING, primary_key=True)
    project_name = models.TextField()
    project_created_at = models.DateTimeField()
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


class Property(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.TextField(unique=True)
    value = models.TextField()
    is_active = models.BooleanField()
    is_predefined = models.BooleanField()

    class Meta:
        db_table = 'property'


class Resource(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    path = models.TextField()
    description = models.TextField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    md5 = models.CharField(unique=True, max_length=32)

    class Meta:
        db_table = 'resource'


class Run(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    log = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=5,
                              blank=False, null=False, choices=Status.choices, default=Status.NEW)
    is_finished = models.BooleanField()
    test_case = models.JSONField()
    parameter = models.JSONField()
    # Field renamed because of name conflict.
    test_case_0 = models.ForeignKey(
        'TestCase', models.DO_NOTHING, db_column='test_case_id')

    start_at = models.DateTimeField(blank=True, null=True)
    end_at = models.DateTimeField(blank=True, null=True)
    group = models.ForeignKey(Group, models.DO_NOTHING)
    priority = models.IntegerField()
    timeout = models.IntegerField()
    run_set_result = models.ForeignKey(
        'RunSetResult', models.DO_NOTHING, blank=True, null=True, related_name='run_set_result')
    driver_pack = models.JSONField(blank=True, null=True)
    driver_pack_id = models.BigIntegerField(blank=True, null=True)
    is_recorded = models.BigIntegerField(blank=True, null=True)
    test_case_overwrite = models.JSONField(blank=True, null=True)
    test_case_overwrite_id = models.BigIntegerField(blank=True, null=True)
    trigger_source = models.TextField(blank=True, null=True)
    drivers = models.JSONField(blank=True, null=True)
    uuid = models.UUIDField()
    test_case_uuid = models.UUIDField(blank=True, null=True)
    singleton = models.BooleanField()
    executable_instruction_number = models.BigIntegerField(
        blank=True, null=True)
    system_requirement_pack = models.ForeignKey(
        'SystemRequirementPack', models.DO_NOTHING, blank=True, null=True)
    system_requirements = models.JSONField(blank=True, null=True)
    # Field renamed because of name conflict.
    system_requirement_pack_0 = models.JSONField(
        db_column='system_requirement_pack', blank=True, null=True)
    result_overwritten = models.IntegerField()
    project = models.ForeignKey(Project, models.DO_NOTHING)

    class Meta:
        db_table = 'run'
        unique_together = (('id', 'start_at', 'end_at'), ('id', 'uuid'), ('id', 'group'), (
            'id', 'test_case_0'), ('id', 'run_set_result'), ('id', 'priority'), ('id', 'is_finished'),)


class RunExecutionInfo(models.Model):
    run = models.OneToOneField(Run, models.DO_NOTHING, primary_key=True)
    run_name = models.TextField()
    run_type = models.CharField(max_length=3,
                                blank=False, null=False, choices=RunType.choices, default=RunType.PRODUCTION)
    status = models.CharField(max_length=5,
                              blank=False, null=False, choices=Status.choices, default=Status.NEW)
    run_created_at = models.DateTimeField()
    run_updated_at = models.DateTimeField(blank=True, null=True)
    test_case_id = models.BigIntegerField()
    run_set_result_id = models.BigIntegerField(blank=True, null=True)
    executable_instruction_number = models.IntegerField()
    instruction_executed_count = models.BigIntegerField()
    instruction_pass_count = models.BigIntegerField()
    trigger_source = models.TextField(blank=True, null=True)
    driver_pack_md5 = models.UUIDField(blank=True, null=True)
    test_case_overwrite_md5 = models.UUIDField(blank=True, null=True)
    test_case_md5 = models.UUIDField(blank=True, null=True)
    run_group_id = models.BigIntegerField()
    driver_pack_name = models.TextField(blank=True, null=True)
    test_case_overwrite_name = models.TextField(blank=True, null=True)
    test_case_name = models.TextField(blank=True, null=True)
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
    name = models.TextField(unique=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    comment = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField()
    log = models.TextField(blank=True, null=True)
    group = models.ForeignKey(Group, models.DO_NOTHING)
    run_set_type = models.CharField(max_length=3,
                                    blank=False, null=False, choices=RunSetType.choices, default=RunSetType.INTERNAL)
    priority = models.IntegerField()
    copy_from_id = models.ForeignKey(
        'self', models.DO_NOTHING, blank=True, null=True, related_name='+')
    parent_id = models.ForeignKey(
        'self', models.DO_NOTHING, blank=True, null=True, related_name='+')
    uuid = models.UUIDField()
    test_cases = models.ManyToManyField('TestCase')
    alias = models.ManyToManyField(Alias)
    notifications = models.ManyToManyField(Notification)

    class Meta:
        db_table = 'run_set'
        unique_together = (('id', 'uuid'),)


class RunSetAliasNameMap(models.Model):
    id = models.BigAutoField(primary_key=True)
    run_set = models.OneToOneField(RunSet, models.DO_NOTHING)
    alias_names = models.JSONField()

    class Meta:
        db_table = 'run_set_alias_name_map'


class RunSetResult(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    start_at = models.DateTimeField(blank=True, null=True)
    end_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=5,
                              blank=False, null=False, choices=Status.choices, default=Status.NEW)
    log = models.TextField()
    group = models.ForeignKey(Group, models.DO_NOTHING)
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
    run_ids = models.JSONField()
    passed_run_ids = models.JSONField()
    failed_run_ids = models.JSONField()

    class Meta:
        db_table = 'run_set_result'
        unique_together = (('id', 'uuid'),)


class Section(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_deleted = models.BooleanField()
    log = models.TextField(blank=True, null=True)
    application = models.ForeignKey(Application, models.DO_NOTHING)
    copy_from_id = models.ForeignKey(
        'self', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey(Project, models.DO_NOTHING)

    class Meta:
        db_table = 'section'
        unique_together = (('id', 'name'), ('name', 'application'),)


class SystemRequirement(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)
    comment = models.TextField(blank=True, null=True)
    is_predefined = models.BooleanField()
    system_requirement_type = models.CharField(max_length=4,
                                               blank=False, null=False, choices=SystemRequirementType.choices, default=SystemRequirementType.CORE)
    value = models.BigIntegerField()

    class Meta:
        db_table = 'system_requirement'
        unique_together = (('id', 'system_requirement_type'),)


class SystemRequirementPack(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    execution_count = models.BigIntegerField()
    comment = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField()
    log = models.TextField(blank=True, null=True)
    is_default = models.BooleanField()
    copy_from_id = models.ForeignKey(
        'self', models.DO_NOTHING, blank=True, null=True)
    system_requirements = models.ManyToManyField(SystemRequirement)

    class Meta:
        db_table = 'system_requirement_pack'


class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    comment = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'tag'


class Template(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)
    type = models.TextField()
    content = models.TextField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    log = models.TextField(blank=True, null=True)
    mode = models.TextField()
    is_deleted = models.BooleanField()

    class Meta:
        db_table = 'template'


class TestCase(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_flagged = models.BooleanField()
    comment = models.TextField(blank=True, null=True)
    log = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField()
    group = models.ForeignKey(Group, models.DO_NOTHING)
    priority = models.IntegerField()
    test_case_type = models.CharField(max_length=5,
                                      blank=False, null=False, choices=TestCaseType.choices, default=TestCaseType.JSON)
    project = models.ForeignKey(Project, models.DO_NOTHING)
    copy_from_id = models.ForeignKey(
        'self', models.DO_NOTHING, blank=True, null=True)
    timeout = models.IntegerField()
    ref_run_set = models.ForeignKey(
        RunSet, models.DO_NOTHING, blank=True, null=True)
    resource_md5 = models.CharField(max_length=32, blank=True, null=True)
    # This field type is a guess.
    parameter = models.TextField(blank=True, null=True)
    uuid = models.UUIDField()
    singleton = models.BooleanField()
    project_name = models.TextField()
    tags = models.ManyToManyField(Tag)

    class Meta:
        db_table = 'test_case'
        unique_together = (('id', 'uuid'), ('id', 'name'),
                           ('name', 'project'),)


class TestCaseDriverAliasMap(models.Model):
    id = models.BigAutoField(primary_key=True)
    test_case = models.OneToOneField(TestCase, models.DO_NOTHING)
    driver_aliases = models.JSONField()

    class Meta:
        db_table = 'test_case_driver_alias_map'


class TestCaseDriverTypeMap(models.Model):
    id = models.BigAutoField(primary_key=True)
    test_case = models.OneToOneField(TestCase, models.DO_NOTHING)
    driver_types = models.JSONField()

    class Meta:
        db_table = 'test_case_driver_type_map'


class TestCaseExecutionInfo(models.Model):
    test_case_id = models.BigIntegerField(primary_key=True)
    test_case_name = models.TextField()
    test_case_created_at = models.DateTimeField()
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
    test_case_is_deleted = models.BooleanField()
    test_case_project_id = models.BigIntegerField()

    class Meta:
        db_table = 'test_case_execution_info'


class TestCaseInstructionTypeMap(models.Model):
    id = models.BigAutoField(primary_key=True)
    test_case = models.OneToOneField(TestCase, models.DO_NOTHING)
    instruction_types = models.JSONField()

    class Meta:
        db_table = 'test_case_instruction_type_map'


class TestCaseOption(models.Model):
    name = models.TextField(unique=True)
    id = models.BigAutoField(primary_key=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    comment = models.TextField(blank=True, null=True)
    is_value_required = models.BooleanField()
    is_active = models.BooleanField()
    is_predefined = models.BooleanField()

    class Meta:
        db_table = 'test_case_option'


class TestCaseOverwrite(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    test_case = models.ForeignKey(TestCase, models.DO_NOTHING)
    is_deleted = models.BooleanField()
    comment = models.TextField(blank=True, null=True)
    copy_from_id = models.ForeignKey(
        'self', models.DO_NOTHING, blank=True, null=True)
    log = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'test_case_overwrite'
        unique_together = (('id', 'test_case'), ('test_case', 'name'),)


class TestCaseShareFolder(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)
    description = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    is_deleted = models.BooleanField()
    log = models.TextField(blank=True, null=True)
    copy_from_id = models.ForeignKey(
        'self', models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    test_cases = models.ForeignKey(TestCase, models.DO_NOTHING)

    class Meta:
        db_table = 'test_case_share_folder'
        unique_together = (('id', 'name'),)
