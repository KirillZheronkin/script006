
def task_2(i:list) -> str:
    return ''.join(x for x in i if isinstance(x, str))