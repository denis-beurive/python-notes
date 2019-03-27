# UUID: unique ID

    from uuid import uuid4
    import hashlib

    long_id = hashlib.sha256(uuid4().bytes).hexdigest()
    print(long_id)
    print(long_id[0:5])
