class InjectedClass1:

    def __init__(self):
        self.boo: str = 'boo'
        print(f'InjectedClass1 created - id=[{id(self)}]')

    def foo(self, str1: str) -> str:
        return str1*2 + self.boo
