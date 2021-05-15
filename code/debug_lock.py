from typing import Optional, Union
from threading import Lock, RLock


class BaseLock(object):

    def __init__(self, in_lock: Union[Lock, RLock], in_resource: Optional[str] = None):
        self.__locker: Optional[str] = None
        self.__resource: Optional[str] = in_resource
        self._lock: Union[Lock, RLock] = in_lock

    @property
    def locker(self) -> Optional[str]:
        return self.__locker

    @property
    def resource(self) -> Optional[str]:
        return self.__resource

    def set(self, locker: str, value: Optional[str] = None):
        self.__locker = locker
        if value is not None:
            self.__resource = value
        return self

    def acquire(self):
        print("acquired", self)
        self._lock.acquire()

    def release(self):
        print("released", self)
        self._lock.release()

    def __enter__(self):
        print('"{}" acquires "{}"'.format(self.locker if self.locker is not None else "locker is not set",
                                          self.resource if self.resource is not None else "resource is not set"))
        self.acquire()

    def __exit__(self, type, value, traceback):
        print('"{}" releases "{}"'.format(self.locker if self.locker is not None else "locker is not set",
                                          self.resource if self.resource is not None else "resource is not set"))
        self.release()


class ExtLock(BaseLock):

    def __init__(self, in_resource: Optional[str] = None):
        super().__init__(Lock(), in_resource)


class ExtRLock(BaseLock):

    def __init__(self, in_resource: Optional[str] = None):
        super().__init__(RLock(), in_resource)


resource1 = {}
resource2 = {}


lock = ExtLock("resource1")
with lock.set("main"):
    resource1[1] = 'a'

rlock = ExtRLock()
with rlock.set("main", "resource2"):
    resource2[1] = 'a'
