import inspect
import builtins
from typing import Callable, List, Dict
from abc import ABCMeta

from dependency_injection.decorators.autowired_enums import AutoWiredType, AutoWiredState
from dependency_injection.data_structures.dependency_injection_exception import DependencyInjectionException
from dependency_injection.design_patterns.singleton import Singleton
from dependency_injection.design_patterns.singleton_handler import SingletonHandler


class AutowiredHandler(metaclass=Singleton):
    def __init__(self):
        self.builtin_types = [getattr(builtins, d) for d in dir(builtins) if isinstance(getattr(builtins, d), type)]

    def autowire(self, func: Callable, auto_wired_type: AutoWiredType, qualifiers: Dict, *args, **kwargs) -> Callable:
        signature: inspect.Signature = inspect.signature(func)
        parameter: inspect.Parameter = None
        annotation: type = None
        instance: object = None
        instance_type: type = None
        sub_classes: List = None
        args_index: int = -1
        auto_wired_state: AutoWiredState = AutoWiredState.IN_ARGS

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
                    raise DependencyInjectionException(1, f'type hints must be used in order to inject a type. param_name=[{key}]')

                else:
                    if annotation in self.builtin_types:
                        raise DependencyInjectionException(1, f'Cannot inject builtin types. param_type=[{annotation.__name__}] param_name=[{key}]')

                    instance_type = annotation
                    # handle abstract type injection
                    if type(annotation) is ABCMeta:
                        sub_classes = [cls for cls in annotation.__subclasses__()]
                        if len(sub_classes) == 1:
                            instance_type = sub_classes[0]
                        else:
                            if qualifiers is None:
                                raise DependencyInjectionException(1, f'There are a few implementations of abstract-class=[{annotation.__name__}] types=[{sub_classes}] you need to provide a qualifiers dictionary')

                            instance_type = qualifiers.get(annotation, None)
                            if instance_type is None:
                                raise DependencyInjectionException(1, f'Can not find a match in qualifier dict for abstract-class=[{annotation.__name__}] Please add it to the qualifier dict')

                    if auto_wired_type == AutoWiredType.SINGLECALL:
                        try:
                            kwargs[key] = instance_type()
                        except Exception as ex:
                            raise DependencyInjectionException(1, str(ex) + f'Cannot create object - param_type=[{instance_type.__name__}] param_name=[{key}] object should have empty constructor')

                    elif auto_wired_type == AutoWiredType.SINGLETON:
                        instance = SingletonHandler.get_singleton(instance_type)
                        if instance is None:
                            raise DependencyInjectionException(1, f'Cannot create singleton - param_type=[{instance_type.__name__}] param_name=[{key}] object should have empty constructor')
                        kwargs[key] = instance

        return func(**kwargs)


autowired_handler: AutowiredHandler = AutowiredHandler()
