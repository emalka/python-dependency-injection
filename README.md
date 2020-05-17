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

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

##License 
[MIT](https://choosealicense.com/licenses/mit/)