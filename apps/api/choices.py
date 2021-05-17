from django.db import models


class LogLevel(models.TextChoices):
    """level choices for log, max length 5"""
    ERROR = 'ERROR'
    WARN = 'WARN'
    INFO = 'INFO'
    DEBUG = 'DEBUG'
    TRACE = 'TRACE'


class Status(models.TextChoices):
    """status choices for models, max length 5"""
    NEW = 'NEW'
    WIP = 'WIP'
    PASS = 'PASS'
    FAIL = 'FAIL'
    ERROR = 'ERROR'
    STOP = 'STOP'
    NA = 'N/A'
    TIMEOUT = 'T/O'
    TERMINATED = 'TERM'


class ProjectType(models.TextChoices):
    """project type choices for models, max length 5"""
    PERSONAL = 'PERS'
    GROUP = 'GROUP'


class TestCaseType(models.TextChoices):
    """test case type choices for models, max length 5"""
    JSON = 'JSON'
    JMETER = 'JM'
    ANDROID = 'ANDRO'


class StepLogType(models.TextChoices):
    """step log type choices for models, max length 7"""
    INSTRUCTION = 'INS'
    INSTRUCTION_BEGIN = 'INS_BIN'
    INSTRUCTION_END = 'INS_END'
    PASS = 'PASS'
    ELEMENT_NOT_FOUND = 'ELE_NF'
    TIME_OUT = 'T/O'
    EXCEPTION = 'EXCEPT'
    FAIL = 'FAIL'


class SystemRequirementType(models.TextChoices):
    """system requirement type choices for models, max length 4"""
    CORE = 'CORE'
    RAM = 'RAM'
    OS = 'OS'
    BANDWIDTH = 'B/W'


class RunType(models.TextChoices):
    """run type choices for models, max length 3"""
    PRODUCTION = 'PRD'
    DEVELOPMENT = 'DEV'


class RunSetType(models.TextChoices):
    """run set type choices for models, max length 3"""
    INTERNAL = 'INT'
    EXTERNAL = 'EXT'


class InstructionColor(models.TextChoices):
    """The color used to displyed the instructions, mac length 3"""
    BLUE = 'BLU'
    GREEN = 'GRE'
    ORANGE = 'ORA'
    RED = 'RED'
    GREY = 'GRY'
    WHITE = 'WHT'


class BrowserResolution(models.TextChoices):
    HD_READY = '1366x768'
    SXGA = '1280x1024'
    WXGA = '1280x800'
    FHD = '1920x1080'
    WXGAP = '1440x900'
