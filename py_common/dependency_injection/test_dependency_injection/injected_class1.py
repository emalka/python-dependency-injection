class InjectedClass1:

    def __init__(self):
        self.message: str = ' from InjectedClass1'
        print(f'InjectedClass1 created - id=[{id(self)}]')

    def foo(self, str1: str) -> str:
        return str1 + self.message
