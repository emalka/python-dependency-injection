import builtins
from functools import wraps

from py_common.decorators.autowired_enums import AutoWiredType
from py_common.decorators.autowired_handler import autowired_handler


builtin_types = [getattr(builtins, d) for d in dir(builtins) if isinstance(getattr(builtins, d), type)]


def autowired(auto_wired_type=AutoWiredType.SINGLETON):
    def wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            return autowired_handler.autowire_and_call(func, auto_wired_type, *args, **kwargs)
        return inner_wrapper
    return wrapper

# signature: inspect.Signature = inspect.signature(func)
# parameter: inspect.Parameter = None
# annotation: type = None
# args_index: int = -1
# auto_wired_state: AutoWiredState = AutoWiredState.IN_ARGS
# type_name: str = None
#
# for key in signature.parameters:
#     args_index += 1
#     parameter = signature.parameters[key]
#     annotation = parameter.annotation
#
#     if len(args) == args_index:
#         auto_wired_state = AutoWiredState.OUT_OF_ARGS
#
#     if auto_wired_state == AutoWiredState.IN_ARGS:
#         kwargs[key] = args[args_index]
#         continue
#
#     if auto_wired_state == AutoWiredState.OUT_OF_ARGS:
#         if key in kwargs:
#             continue
#
#         elif annotation == inspect._empty:
#             """
#                 type hint must be used in order to inject a type using python-dependency-injection
#             """
#             raise DependencyInjectionException(1, f'type hint must be used in order to inject a type. param_name=[{key}]')
#
#         else:
#             if annotation in builtin_types:
#                 raise DependencyInjectionException(1, f'Cannot inject builtin types. param_type=[{annotation.__name__}] param_name=[{key}]')
#
#             if auto_wired_type == AutoWiredType.SINGLECALL:
#                 kwargs[key] = annotation()
#             elif auto_wired_type == AutoWiredType.SINGLETON:
#                 pass
#
# return func(**kwargs)
