from threading import Lock


class Singleton(type):
    lock: Lock = Lock()
    _class_locks: dict = {}
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        class_lock: Lock = None
        instance: any = None

        # get specific class lock to avoid dead lock when creating singleton inside singleton
        cls.lock.acquire()
        if cls.__name__ not in cls._class_locks:
            cls._class_locks[cls.__name__] = Lock()
        class_lock = cls._class_locks.get(cls.__name__, None)
        cls.lock.release()

        # using the class lock access the in
        class_lock.acquire()
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        instance = cls._instances[cls]
        class_lock.release()

        return instance

    @classmethod
    def clear_instance(mcs):
        class_lock: Lock = None
        instance: any = None

        # get specific class lock to avoid dead lock when creating singleton inside singleton
        mcs.lock.acquire()
        if mcs.__name__ not in mcs._class_locks:
            mcs._class_locks[mcs.__name__] = Lock()
        class_lock = mcs._class_locks.get(mcs.__name__, None)
        mcs.lock.release()

        # using the class lock access the in
        class_lock.acquire()
        if mcs not in mcs._instances:
            for instance in mcs._instances:
                del instance
        mcs._instances.clear()
        class_lock.release()
