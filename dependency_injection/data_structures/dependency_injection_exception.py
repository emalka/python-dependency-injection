class DependencyInjectionException(Exception):

    def __init__(self, exception_id: int, exception_description: str):
        super().__init__(exception_description)
        self.exception_id: int = exception_id
        self.exception_description: str = exception_description


