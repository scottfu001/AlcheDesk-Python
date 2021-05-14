import enum


class LogLevel(enum.Enum):
    ERROR = 1
    WARN = 2
    INFO = 3
    DEBUG = 4
    TRACE = 5


class Status(enum.Enum):
    NEW = 1
    WIP = 2
    PASS = 3
    FAIL = 4
    ERROR = 5
    STOP = 6
    NA = 7
    TIMEOUT = 8
    TERMINATED = 9
