import itertools

test = input()


def rle(text):
    for k, s in itertools.groupby(text):
        i = sum(1 for x in s)
        yield k if (i == 1) else str(i) + k


print(''.join(rle(test)))
