# Serialization

    import pickle

    lst = [10, 20, 30]
    with open('list.bin', mode='wb') as fd:
        pickle.dump(lst, fd)

    with open('list.bin', mode='rb') as fd:
        lst_bin = fd.read()
    list_object = pickle.loads(lst_bin)

    print(';'.join(map(lambda x: str(x), list_object))) # 10;20;30

