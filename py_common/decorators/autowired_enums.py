from enum import Enum


class AutoWiredType(Enum):
    SINGLETON = 'singleton'
    SINGLECALL = 'singlecall'


class AutoWiredState(Enum):
    IN_ARGS = 'args'
    OUT_OF_ARGS = 'kwargs'
