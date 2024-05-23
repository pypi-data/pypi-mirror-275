def rstrip_list(iterable):
    list=[]
    for string in iterable:
        string=str(string)
        list.append(string.rstrip())
    return list