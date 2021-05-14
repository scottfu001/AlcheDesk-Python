# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models.deletion import DO_NOTHING


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


class ContentArchive(models.Model):
    content_type = models.TextField()
    content_md5 = models.TextField(primary_key=True)
    content_json = models.JSONField(unique=True)

    class Meta:
        db_table = 'content_archive'


class ContentType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)

    class Meta:
        db_table = 'content_type'


class DevExecutionLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    message = models.TextField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    log_level = models.ForeignKey('LogLevel', models.DO_NOTHING)
    instruction_result = models.ForeignKey(
        'DevInstructionResult', models.DO_NOTHING)
    run = models.ForeignKey('Run', models.DO_NOTHING)
    run_type = models.ForeignKey('RunType', models.DO_NOTHING)

    class Meta:
        db_table = 'dev_execution_log'


class DevFile(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField()
    parameter = models.JSONField()
    file_type = models.ForeignKey('FileType', models.DO_NOTHING)
    instruction_result = models.ForeignKey(
        'DevInstructionResult', models.DO_NOTHING, blank=True, null=True)
    uri = models.TextField(blank=True, null=True)
    run_type = models.ForeignKey('RunType', models.DO_NOTHING)
    run = models.ForeignKey('Run', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'dev_file'


class DevInstructionResult(models.Model):
    id = models.BigAutoField(primary_key=True)
    action = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.ForeignKey('Status', models.DO_NOTHING)
    log = models.TextField(blank=True, null=True)
    is_finished = models.BooleanField()
    instruction = models.JSONField()
    data = models.JSONField()
    run = models.ForeignKey('Run', models.DO_NOTHING)
    run_type = models.ForeignKey('RunType', models.DO_NOTHING)
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
        'Instruction', models.DO_NOTHING, db_column='instruction_id', blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'dev_instruction_result'


class DevStepLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    message = models.TextField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    instruction_result = models.ForeignKey(
        DevInstructionResult, models.DO_NOTHING)
    step_log_type = models.ForeignKey('StepLogType', models.DO_NOTHING)
    run_type = models.ForeignKey('RunType', models.DO_NOTHING)

    class Meta:
        db_table = 'dev_step_log'


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
    driver_aliases = models.TextField()  # This field type is a guess.

    class Meta:
        db_table = 'driver_pack_driver_alias_map'


class DriverPackDriverLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    driver_pack = models.ForeignKey(DriverPack, models.DO_NOTHING)
    driver = models.ForeignKey(Driver, models.DO_NOTHING)
    driver_alias = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'driver_pack_driver_link'
        unique_together = (('driver_pack', 'driver'),)


class DriverPackDriverTypeMap(models.Model):
    id = models.BigAutoField(primary_key=True)
    driver_pack = models.OneToOneField(DriverPack, models.DO_NOTHING)
    driver_types = models.TextField()  # This field type is a guess.

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

    class Meta:
        db_table = 'driver_type'


class DriverTypeInstructionTypeLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    driver_type = models.ForeignKey(DriverType, models.DO_NOTHING)
    instruction_type = models.OneToOneField(
        'InstructionType', models.DO_NOTHING)

    class Meta:
        db_table = 'driver_type_instruction_type_link'
        unique_together = (('driver_type', 'instruction_type'),)


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
        'ElementTypeElementLocatorTypeLink', models.DO_NOTHING)
    element_locator_type = models.ForeignKey(
        'ElementLocatorType', models.DO_NOTHING, blank=True, null=True)
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


class ElementLocatorType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)
    is_active = models.BooleanField()
    is_predefined = models.BooleanField()

    class Meta:
        db_table = 'element_locator_type'


class ElementType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)
    is_active = models.BooleanField()
    is_driver = models.BooleanField()

    class Meta:
        db_table = 'element_type'


class ElementTypeElementLocatorTypeLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    element_type = models.ForeignKey(ElementType, models.DO_NOTHING)
    element_locator_type = models.ForeignKey(
        ElementLocatorType, models.DO_NOTHING)

    class Meta:
        db_table = 'element_type_element_locator_type_link'
        unique_together = (('element_type', 'element_locator_type'),)


class ElementTypeInstructionActionLink(models.Model):
    element_type = models.ForeignKey(ElementType, models.DO_NOTHING)
    instruction_action = models.ForeignKey(
        'InstructionAction', models.DO_NOTHING)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        db_table = 'element_type_instruction_action_link'
        unique_together = (('element_type', 'instruction_action'),)


class ElementTypeInstructionOptionLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    element_type = models.ForeignKey(ElementType, models.DO_NOTHING)
    instruction_option = models.ForeignKey(
        'InstructionOption', models.DO_NOTHING)

    class Meta:
        db_table = 'element_type_instruction_option_link'
        unique_together = (('element_type', 'instruction_option'),)


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
        'InstructionTypeInstructionActionLink', models.DO_NOTHING, blank=True, null=True)
    is_driver = models.BooleanField()
    parameter = models.JSONField()
    copy_from_id = models.ForeignKey(
        'self', models.DO_NOTHING, blank=True, null=True)
    expected_value = models.TextField(blank=True, null=True)
    resource_md5 = models.CharField(max_length=32, blank=True, null=True)
    element_type = models.ForeignKey(
        ElementType, models.DO_NOTHING, blank=True, null=True)
    driver_type = models.ForeignKey(
        DriverTypeInstructionTypeLink, models.DO_NOTHING, blank=True, null=True)
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

    class Meta:
        db_table = 'instruction_action'


class InstructionActionInstructionOptionLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    instruction_action = models.ForeignKey(
        InstructionAction, models.DO_NOTHING)
    instruction_option = models.ForeignKey(
        'InstructionOption', models.DO_NOTHING)

    class Meta:
        db_table = 'instruction_action_instruction_option_link'
        unique_together = (('instruction_action', 'instruction_option'),)


class InstructionBundle(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    comment = models.TextField()
    is_deleted = models.BooleanField()

    class Meta:
        db_table = 'instruction_bundle'


class InstructionBundleEntry(models.Model):
    id = models.BigAutoField(primary_key=True)
    comment = models.TextField()
    instruction_bundle = models.ForeignKey(
        InstructionBundle, models.DO_NOTHING)
    instruction_type_id = models.BigIntegerField(blank=True, null=True)
    element_type = models.ForeignKey(
        ElementTypeInstructionActionLink, models.DO_NOTHING, blank=True, null=True)
    instruction_action = models.ForeignKey(
        'InstructionTypeInstructionActionLink', models.DO_NOTHING, blank=True, null=True)
    order_index = models.BigIntegerField()
    is_deleted = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'instruction_bundle_entry'


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


class InstructionOptionEntry(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.ForeignKey(
        InstructionOption, models.DO_NOTHING, db_column='name')
    value = models.TextField(blank=True, null=True)
    is_value_required = models.BooleanField()
    instruction = models.OneToOneField(Instruction, models.DO_NOTHING)

    class Meta:
        db_table = 'instruction_option_entry'


class InstructionOptionMap(models.Model):
    instruction_option = models.OneToOneField(
        InstructionOption, models.DO_NOTHING, primary_key=True)
    instruction_action_ids = models.TextField()  # This field type is a guess.
    element_type_ids = models.TextField()  # This field type is a guess.

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

    class Meta:
        db_table = 'instruction_type'
        unique_together = (('id', 'overridable_fields'), ('id', 'is_driver'),)


class InstructionTypeElementTypeLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    instruction_type = models.ForeignKey(InstructionType, models.DO_NOTHING)
    element_type = models.ForeignKey(ElementType, models.DO_NOTHING)

    class Meta:
        db_table = 'instruction_type_element_type_link'
        unique_together = (('instruction_type', 'element_type'),)


class InstructionTypeInstructionActionLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    instruction_type = models.ForeignKey(InstructionType, models.DO_NOTHING)
    instruction_action = models.ForeignKey(
        InstructionAction, models.DO_NOTHING)

    class Meta:
        db_table = 'instruction_type_instruction_action_link'
        unique_together = (('instruction_type', 'instruction_action'),)


class LogLevel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)

    class Meta:
        db_table = 'log_level'


class Module(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    version = models.TextField()
    comment = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    log = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField()

    class Meta:
        db_table = 'module'
        unique_together = (('name', 'version'),)


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

    class Meta:
        db_table = 'notification'


class NotificationEmailNotificationTargetLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    notification = models.ForeignKey(Notification, models.DO_NOTHING)
    email_notification_target = models.ForeignKey(
        EmailNotificationTarget, models.DO_NOTHING)

    class Meta:
        db_table = 'notification_email_notification_target_link'
        unique_together = (('notification', 'email_notification_target'),)


class ParameterScript(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.TextField()
    symbol = models.TextField()
    script = models.TextField()

    class Meta:
        db_table = 'parameter_script'


class ProdExecutionLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    message = models.TextField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    log_level = models.ForeignKey(LogLevel, models.DO_NOTHING)
    instruction_result = models.ForeignKey(
        'ProdInstructionResult', models.DO_NOTHING)
    run = models.ForeignKey('Run', models.DO_NOTHING)
    run_type = models.ForeignKey('RunType', models.DO_NOTHING)

    class Meta:
        db_table = 'prod_execution_log'


class ProdFile(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField()
    parameter = models.JSONField()
    file_type = models.ForeignKey(FileType, models.DO_NOTHING)
    instruction_result = models.ForeignKey(
        'ProdInstructionResult', models.DO_NOTHING, blank=True, null=True)
    uri = models.TextField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    run_type = models.ForeignKey('RunType', models.DO_NOTHING)
    run = models.ForeignKey('Run', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'prod_file'


class ProdInstructionResult(models.Model):
    id = models.BigAutoField(primary_key=True)
    action = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.ForeignKey('Status', models.DO_NOTHING)
    log = models.TextField(blank=True, null=True)
    is_finished = models.BooleanField()
    instruction = models.JSONField()
    data = models.JSONField()
    run = models.ForeignKey('Run', models.DO_NOTHING)
    run_type = models.ForeignKey('RunType', models.DO_NOTHING)
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
        db_table = 'prod_instruction_result'


class ProdStepLog(models.Model):
    message = models.TextField()
    id = models.BigAutoField(primary_key=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    instruction_result = models.ForeignKey(
        ProdInstructionResult, models.DO_NOTHING)
    step_log_type = models.ForeignKey('StepLogType', models.DO_NOTHING)
    run_type = models.ForeignKey('RunType', models.DO_NOTHING)

    class Meta:
        db_table = 'prod_step_log'


class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    comment = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField()
    log = models.TextField(blank=True, null=True)
    project_type = models.ForeignKey('ProjectType', models.DO_NOTHING)
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
    active_test_case_ids = models.TextField()  # This field type is a guess.
    executed_test_case_ids = models.TextField()  # This field type is a guess.
    passed_test_case_ids = models.TextField()  # This field type is a guess.
    passed_test_case_number = models.IntegerField()
    total_test_case_number = models.IntegerField()
    test_case_ids = models.TextField()  # This field type is a guess.
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


class ProjectType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)
    is_active = models.BooleanField()

    class Meta:
        db_table = 'project_type'


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
    status = models.ForeignKey('Status', models.DO_NOTHING)
    is_finished = models.BooleanField()
    test_case = models.JSONField()
    parameter = models.JSONField()
    # Field renamed because of name conflict.
    test_case_0 = models.ForeignKey(
        'TestCase', models.DO_NOTHING, db_column='test_case_id')
    run_type = models.ForeignKey('RunType', models.DO_NOTHING)
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
    run_set_test_case_link_id = models.BigIntegerField(blank=True, null=True)
    result_overwritten = models.IntegerField()
    project = models.ForeignKey(Project, models.DO_NOTHING)

    class Meta:
        db_table = 'run'
        unique_together = (('id', 'start_at', 'end_at'), ('id', 'uuid'), ('id', 'group'), (
            'id', 'test_case_0'), ('id', 'run_set_result'), ('id', 'priority'), ('id', 'is_finished'),)


class RunExecutionInfo(models.Model):
    run = models.OneToOneField(Run, models.DO_NOTHING, primary_key=True)
    run_name = models.TextField()
    run_type_id = models.BigIntegerField()
    run_status_id = models.BigIntegerField(blank=True, null=True)
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
    run_set_type = models.ForeignKey('RunSetType', models.DO_NOTHING)
    priority = models.IntegerField()
    copy_from_id = models.ForeignKey(
        'self', models.DO_NOTHING, blank=True, null=True, related_name='+')
    parent_id = models.ForeignKey(
        'self', models.DO_NOTHING, blank=True, null=True, related_name='+')
    uuid = models.UUIDField()
    # This field type is a guess.
    aliases = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'run_set'
        unique_together = (('id', 'uuid'),)


class RunSetAliasLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    run_set = models.ForeignKey(RunSet, models.DO_NOTHING)
    alias = models.ForeignKey(Alias, models.DO_NOTHING)

    class Meta:
        db_table = 'run_set_alias_link'
        unique_together = (('run_set', 'alias'),)


class RunSetAliasNameMap(models.Model):
    id = models.BigAutoField(primary_key=True)
    run_set = models.OneToOneField(RunSet, models.DO_NOTHING)
    alias_names = models.TextField()  # This field type is a guess.

    class Meta:
        db_table = 'run_set_alias_name_map'


class RunSetJobLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    run_set = models.ForeignKey(RunSet, models.DO_NOTHING)
    job_uuid = models.UUIDField(unique=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    run_set_uuid = models.UUIDField(blank=True, null=True)

    class Meta:
        db_table = 'run_set_job_link'


class RunSetNotificationLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    run_set = models.ForeignKey(RunSet, models.DO_NOTHING)
    notification = models.ForeignKey(Notification, models.DO_NOTHING)

    class Meta:
        db_table = 'run_set_notification_link'
        unique_together = (('run_set', 'notification'),)


class RunSetResult(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    start_at = models.DateTimeField(blank=True, null=True)
    end_at = models.DateTimeField(blank=True, null=True)
    status = models.ForeignKey('Status', models.DO_NOTHING)
    log = models.TextField()
    group = models.ForeignKey(Group, models.DO_NOTHING)
    run_set_type = models.ForeignKey('RunSetType', models.DO_NOTHING)
    priority = models.IntegerField()
    run_set = models.ForeignKey(
        RunSet, models.DO_NOTHING, blank=True, null=True)
    is_finished = models.BooleanField()
    run_type = models.ForeignKey('RunType', models.DO_NOTHING)
    source_type = models.ForeignKey('SourceType', models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    run = models.JSONField(blank=True, null=True)
    uuid = models.UUIDField()
    total_run_number = models.IntegerField()
    passed_run_number = models.IntegerField()
    failed_run_number = models.IntegerField()
    run_ids = models.TextField()  # This field type is a guess.
    passed_run_ids = models.TextField()  # This field type is a guess.
    failed_run_ids = models.TextField()  # This field type is a guess.

    class Meta:
        db_table = 'run_set_result'
        unique_together = (('id', 'uuid'),)


class RunSetResultJobLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    run_set_result = models.OneToOneField(RunSetResult, models.DO_NOTHING)
    job_uuid = models.UUIDField(unique=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    run_set_result_uuid = models.UUIDField(blank=True, null=True)

    class Meta:
        db_table = 'run_set_result_job_link'


class RunSetTestCaseLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    run_set = models.ForeignKey(
        RunSet, models.DO_NOTHING, related_name='run_set')
    test_case = models.ForeignKey(
        'TestCase', models.DO_NOTHING, blank=True, null=True)
    test_case_overwrite = models.ForeignKey(
        'TestCaseOverwrite', models.DO_NOTHING, blank=True, null=True)
    driver_pack = models.ForeignKey(
        DriverPack, models.DO_NOTHING, blank=True, null=True)
    ref_run_set = models.ForeignKey(
        RunSet, models.DO_NOTHING, blank=True, null=True, related_name='ref_run_set')
    system_requirement_pack = models.ForeignKey(
        'SystemRequirementPack', models.DO_NOTHING, blank=True, null=True)
    synchronize = models.BooleanField()

    class Meta:
        db_table = 'run_set_test_case_link'
        unique_together = (('run_set', 'ref_run_set'), ('run_set', 'test_case'), ('run_set', 'test_case', 'driver_pack'), (
            'run_set', 'test_case', 'driver_pack', 'test_case_overwrite'), ('run_set', 'test_case', 'test_case_overwrite'),)


class RunSetType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)
    is_predefined = models.BooleanField()
    is_active = models.BooleanField()

    class Meta:
        db_table = 'run_set_type'


class RunTaskLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    run = models.OneToOneField(Run, models.DO_NOTHING)
    task_uuid = models.UUIDField(unique=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    run_uuid = models.UUIDField()

    class Meta:
        db_table = 'run_task_link'


class RunType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)
    is_active = models.BooleanField()
    is_predefined = models.BooleanField()

    class Meta:
        db_table = 'run_type'


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


class SourceType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    is_predefined = models.BooleanField()
    is_active = models.BooleanField()

    class Meta:
        db_table = 'source_type'


class Status(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)
    is_active = models.BooleanField()
    is_predefined = models.BooleanField()

    class Meta:
        db_table = 'status'


class StepLogType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)
    is_active = models.BooleanField()
    is_predefined = models.BooleanField()

    class Meta:
        db_table = 'step_log_type'


class SystemRequirement(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)
    comment = models.TextField(blank=True, null=True)
    is_predefined = models.BooleanField()
    system_requirement_type = models.ForeignKey(
        'SystemRequirementType', models.DO_NOTHING)
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

    class Meta:
        db_table = 'system_requirement_pack'


class SystemRequirementPackSystemRequirementLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    system_requirement_pack = models.ForeignKey(
        SystemRequirementPack, models.DO_NOTHING)
    system_requirement = models.ForeignKey(
        SystemRequirement, models.DO_NOTHING)
    system_requirement_type_id = models.BigIntegerField()

    class Meta:
        db_table = 'system_requirement_pack_system_requirement_link'
        unique_together = (('system_requirement_pack', 'system_requirement_type_id'),
                           ('system_requirement_pack', 'system_requirement'),)


class SystemRequirementType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)
    is_multiselectable = models.BooleanField()
    is_active = models.BooleanField()
    is_predefined = models.BooleanField()

    class Meta:
        db_table = 'system_requirement_type'


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


class Tenant(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.TextField()
    uuid = models.UUIDField(unique=True)
    account_uuid = models.UUIDField()

    class Meta:
        db_table = 'tenant'


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
    test_case_type = models.ForeignKey('TestCaseType', models.DO_NOTHING)
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

    class Meta:
        db_table = 'test_case'
        unique_together = (('id', 'uuid'), ('id', 'name'),
                           ('name', 'project'),)


class TestCaseDriverAliasMap(models.Model):
    id = models.BigAutoField(primary_key=True)
    test_case = models.OneToOneField(TestCase, models.DO_NOTHING)
    driver_aliases = models.TextField()  # This field type is a guess.

    class Meta:
        db_table = 'test_case_driver_alias_map'


class TestCaseDriverTypeMap(models.Model):
    id = models.BigAutoField(primary_key=True)
    test_case = models.OneToOneField(TestCase, models.DO_NOTHING)
    driver_types = models.TextField()  # This field type is a guess.

    class Meta:
        db_table = 'test_case_driver_type_map'


class TestCaseExecutionInfo(models.Model):
    test_case_id = models.BigIntegerField(primary_key=True)
    test_case_name = models.TextField()
    test_case_created_at = models.DateTimeField()
    total_run_count = models.BigIntegerField()
    latest_run_status_id = models.BigIntegerField(blank=True, null=True)
    latest_run_updated_at = models.DateTimeField(blank=True, null=True)
    latest_run_instruction_executed_count = models.BigIntegerField(
        blank=True, null=True)
    latest_run_instruction_pass_count = models.BigIntegerField(
        blank=True, null=True)
    latest_run_trigger_source = models.TextField(blank=True, null=True)
    latest_run_created_at = models.DateTimeField(blank=True, null=True)
    latest_run = models.ForeignKey(
        Run, models.DO_NOTHING, blank=True, null=True, related_name='latest_run')
    latest_run_executable_instruction_number = models.BigIntegerField(
        blank=True, null=True)
    total_dev_run_count = models.BigIntegerField(blank=True, null=True)
    latest_dev_run_status_id = models.BigIntegerField(blank=True, null=True)
    latest_dev_run_updated_at = models.DateTimeField(blank=True, null=True)
    latest_dev_run_instruction_executed_count = models.BigIntegerField(
        blank=True, null=True)
    latest_dev_run_instruction_pass_count = models.BigIntegerField(
        blank=True, null=True)
    latest_dev_run_trigger_source = models.TextField(blank=True, null=True)
    latest_dev_run_created_at = models.DateTimeField(blank=True, null=True)
    latest_dev_run = models.ForeignKey(
        Run, models.DO_NOTHING, blank=True, null=True, related_name='latest_dev_run')
    latest_dev_run_executable_instruction_number = models.BigIntegerField(
        blank=True, null=True)
    latest_run_instruction_fail_count = models.IntegerField()
    test_case_is_deleted = models.BooleanField()
    test_case_project_id = models.BigIntegerField()

    class Meta:
        db_table = 'test_case_execution_info'


class TestCaseInstructionTypeMap(models.Model):
    id = models.BigAutoField(primary_key=True)
    test_case = models.OneToOneField(TestCase, models.DO_NOTHING)
    instruction_types = models.TextField()  # This field type is a guess.

    class Meta:
        db_table = 'test_case_instruction_type_map'


class TestCaseModuleLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    test_case = models.ForeignKey(TestCase, models.DO_NOTHING)
    module = models.ForeignKey(Module, models.DO_NOTHING)

    class Meta:
        db_table = 'test_case_module_link'
        unique_together = (('test_case', 'module'),)


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


class TestCaseOptionEntry(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.ForeignKey(
        TestCaseOption, models.DO_NOTHING, db_column='name')
    value = models.TextField(blank=True, null=True)
    test_case = models.ForeignKey(TestCase, models.DO_NOTHING)
    is_value_required = models.BooleanField()

    class Meta:
        db_table = 'test_case_option_entry'


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

    class Meta:
        db_table = 'test_case_share_folder'
        unique_together = (('id', 'name'),)


class TestCaseShareFolderTestCaseLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    test_case = models.ForeignKey(TestCase, models.DO_NOTHING)
    test_case_share_folder = models.ForeignKey(
        TestCaseShareFolder, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'test_case_share_folder_test_case_link'
        unique_together = (('test_case', 'test_case_share_folder'),)


class TestCaseTagLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    test_case = models.ForeignKey(TestCase, models.DO_NOTHING)
    tag = models.ForeignKey(Tag, models.DO_NOTHING)

    class Meta:
        db_table = 'test_case_tag_link'
        unique_together = (('test_case', 'tag'),)


class TestCaseTaskLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    test_case = models.ForeignKey(TestCase, models.DO_NOTHING)
    task_uuid = models.UUIDField(unique=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    test_case_uuid = models.UUIDField(blank=True, null=True)

    class Meta:
        db_table = 'test_case_task_link'


class TestCaseType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(unique=True)
    is_predefined = models.BooleanField()
    is_active = models.BooleanField()

    class Meta:
        db_table = 'test_case_type'


class UserActivityLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_uuid = models.UUIDField()
    activity_uuid = models.UUIDField()
    target_model = models.CharField(max_length=255)
    action_name = models.CharField(max_length=255)
    input = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    user_name = models.TextField()

    class Meta:
        db_table = 'user_activity_log'


class UserContent(models.Model):
    id = models.BigAutoField(primary_key=True)
    content_uuid = models.UUIDField(unique=True, blank=True, null=True)
    sha256 = models.TextField(blank=True, null=True)
    original_name = models.TextField()
    modified_name = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey(ContentType, models.DO_NOTHING)
    version = models.TextField(blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    path = models.TextField()

    class Meta:
        db_table = 'user_content'
        unique_together = (('sha256', 'original_name'),)
