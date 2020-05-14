import inspect
import builtins
from typing import Callable

from py_common.decorators.autowired_enums import AutoWiredType, AutoWiredState
from py_common.dependency_injection.dependency_injection_exception import DependencyInjectionException
from py_common.design_patterns.singleton import Singleton


class AutowiredHandler(metaclass=Singleton):
    def __init__(self):
        self.builtin_types = [getattr(builtins, d) for d in dir(builtins) if isinstance(getattr(builtins, d), type)]

    def autowire_and_call(self, func: Callable, auto_wired_type: AutoWiredType, *args, **kwargs) -> Callable:

        signature: inspect.Signature = inspect.signature(func)
        parameter: inspect.Parameter = None
        annotation: type = None
        args_index: int = -1
        auto_wired_state: AutoWiredState = AutoWiredState.IN_ARGS
        type_name: str = None

        for key in signature.parameters:
            args_index += 1
            parameter = signature.parameters[key]
            annotation = parameter.annotation

            if len(args) == args_index:
                auto_wired_state = AutoWiredState.OUT_OF_ARGS

            if auto_wired_state == AutoWiredState.IN_ARGS:
                kwargs[key] = args[args_index]
                continue

            if auto_wired_state == AutoWiredState.OUT_OF_ARGS:
                if key in kwargs:
                    continue

                elif annotation == inspect._empty:
                    """
                        type hint must be used in order to inject a type using python-dependency-injection 
                    """
                    raise DependencyInjectionException(1, f'type hint must be used in order to inject a type. param_name=[{key}]')

                else:
                    if annotation in self.builtin_types:
                        raise DependencyInjectionException(1, f'Cannot inject builtin types. param_type=[{annotation.__name__}] param_name=[{key}]')

                    if auto_wired_type == AutoWiredType.SINGLECALL:
                        kwargs[key] = annotation()
                    elif auto_wired_type == AutoWiredType.SINGLETON:
                        kwargs[key] = annotation()

        return func(**kwargs)


autowired_handler: AutowiredHandler = AutowiredHandler()
