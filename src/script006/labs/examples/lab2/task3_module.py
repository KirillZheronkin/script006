def task3(i):
    if i == []:
        return i
    if isinstance(i[0], list):
        return task3(i[0]) + task3(i[1:])
    return i[:1] + task3(i[1:])


a = [1,
[2,3],
[[4,5,6],[7,8,9]],
]