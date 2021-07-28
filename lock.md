# Locks

[Deadlock debug tools](code/debug_lock.py)

RLocks (for _re-entrant_) must be used if the following situation may occur:

![](images/rlock.png)

**WARNING**

When you start a thread, the correct way to do it is:

	Thread(target=self.__function_name).start()

Do **NOT** (probably Inadvertently) write:

	Thread(target=self.__function_name()).start()

> Especially if the function implements an infinite loop!

This error can be very hard to find... and you may lose a lot of time!
