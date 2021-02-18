line = "this is a string"


def split_and_join(line):
    return '-'.join(word for word in line.split())


print(split_and_join(line))
