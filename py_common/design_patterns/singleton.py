from py_common.design_patterns.singleton_handler import SingletonHandler


class Singleton(type):
    def __call__(cls, *args, **kwargs):
        cls_init_func = super()
        return SingletonHandler.add_singleton(cls, cls_init_func, *args, **kwargs)

    @classmethod
    def clear_instance(mcs):
        pass
