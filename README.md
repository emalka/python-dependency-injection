# python-dependency-injection

python-dependency-injection is a simple yet powerful mini-framework for dependency injection in Python

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Python-dependency-injection.

```bash
pip install python-dependency-injection
```

## Description
```
python-dependency-injection enables developers to easily inject any Python class into another Python class 
(the injected class) upon the creation of the latter. The framework scans the injected class __init__ 
function parameters and provides any user-defined type not provided by the developer when the function 
is triggered.

The framework enables the developer to inject a class as singleton wherein every injection of the class
the framework will provide the same object instance or inject the class as singlecall wherein every 
injection of the class the framework will provide a different object instance.

python-dependency-injection is very easy to use. all you need to do is put the autowired decorator 
on top of the __init__ function of the class you want to inject too (see below) and the mini-framework 
will take care of everything for you.

There are a few pre-requisites:
* You need to use Python typing hints in the injected class __init__ function 
  see https://docs.python.org/3/library/typing.html.
* The injected class cannot be Python builtin types like str or int.
* All injected classes should appear as the last parameters in the __init__ function of the class 
  developer inject to i.e. __init__(non_inject1, non_inject2, inject3: InjectType3, inject4 InjectType4)

If the framework can not inject an object a DependencyInjectionException will be raise specifying 
the error.
```


## Code

```python
# this class will be injected
from dependency_injection.decorators.autowired import autowired
from dependency_injection.decorators.autowired_enums import AutoWiredType

class InjectedClass:
    def __init__(self):
        self.message: str = ' from InjectedClass'

    def foo(self, str1: str) -> str:
        return str1 + self.message


# class objects will be injected to
class TestSingletonInjection:
    @autowired() # Or use @autowired(AutoWiredType.SINGLETON)
    def __init__(self, my_name: str, injected_class: InjectedClass):
        self.injected_class = injected_class
        self.my_name = my_name

    def test_inject(self) -> str:
        return self.injected_class.foo('hello TestClassSingleton')


# class objects will be injected to
class TestSingleCallInjection:
    @autowired(AutoWiredType.SINGLECALL)
    def __init__(self, my_name: str, injected_class: InjectedClass):
        self.injected_class = injected_class
        self.my_name = my_name

    def test_inject(self) -> str:
        return self.injected_class.foo('hello TestClassSinglecall')

if __name__ == '__main__':
    test_singleton_injection: TestSingletonInjection = TestSingletonInjection('TestSingletonInjection')
    print(test_singleton_injection.test_inject())

    test_singlecall_injection: TestSingleCallInjection = TestSingleCallInjection('TestSingleCallInjection')
    print(test_singlecall_injection.test_inject())
```

## Abstract Classes
```
python-dependency-injection support injection of classes derived from abstract classes (abs). If in 
the developer project there is only one derived class the framework will find the derived class and 
inject it.

If there are a more then one derived class from the abstract class the user need to provid a
qualifiers dictionary that will inform the mini framework about the actual implementation that
should be used
```

## Abstract Classes Code

```python
from abc import ABC, abstractmethod
from dependency_injection.decorators.autowired import autowired
from dependency_injection.decorators.autowired_enums import AutoWiredType


class AbsCls(ABC):
    def __init__(self):
        super().__init__()
        self.message = 'AbsCls'

    @abstractmethod
    def foo(self, str1: str) -> str:
        pass


class Drv1(AbsCls):

    def __init__(self):
        super().__init__()
        self.message += ' + Drv1'

    def foo(self, str1: str) -> str:
        return str1 + self.message


class Drv2(AbsCls):
    def __init__(self):
        super().__init__()
        self.message += ' + Drv2'

    def foo(self, str1: str) -> str:
        return str1 + self.message


class Inject2Me:

    # if only one object was derived from AbsCls the developer will use @autowired() instead
    @autowired(AutoWiredType.SINGLETON, {AbsCls: Drv1})
    def __init__(self, name: str, my_obj: AbsCls):
        self.name = name
        self.my_obj = my_obj

    def run_me(self) -> str:
        return self.my_obj.foo("InjectMe")


if __name__ == '__main__':
    inject_2_me: Inject2Me = Inject2Me('Inject2Me')
    print(inject_2_me.run_me())
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

##License 
[MIT](https://choosealicense.com/licenses/mit/)