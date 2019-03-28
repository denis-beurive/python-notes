# UUID: unique ID

    from uuid import uuid4
    import hashlib

    def get_uid(length: int=None, uppercase: bool=False) -> str:
        """Generate a unique ID.

        Args:
            length (str): length of the unique ID.
                By default, if no length is specified, the returned ID is made of 64 hexadecimal characters.
                For example: "6e3dd27602b2ca246f68a6ddf0d0044a162339d40be80acb0f11276468c95efb"
            uppercase (bool): flag that indicates whether the returned ID must be an all uppercase string of not.
                The value True indicates that the returned ID must be all uppercase.
                By default, the returned ID is all lowercase.

        Returns:
            str: a string that represents the unique ID.
        """
        uid: str = hashlib.sha256(uuid4().bytes).hexdigest()[0:length]
        if uppercase:
            return uid.upper()
        return uid

    print(get_uid())
    print(get_uid(5))
    print(get_uid(length=10))
    print(get_uid(5, True))
    print(get_uid(length=10, uppercase=True)))


