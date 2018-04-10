import random


def sample_wr(iterable, choose=random.choice):
    while True:
        yield choose(iterable)


if __name__ == '__main__':
    import itertools
    from string import ascii_lowercase
    x = ''.join(itertools.islice(sample_wr(ascii_lowercase), 50))
    print(x)
