class cached_property(object):
    """
    A property this is cached this function compute once.
    """

    def __init__(self, wrapped, name=None):
        self.wrapped = wrapped
        self.__doc__ = getattr(wrapped, '__doc__', None)
        self.name = name or '_' + wrapped.__name__

    def __get__(self, inst, cls):
        if inst is None:
            return self
        name = self.name
        result = self.wrapped(inst)
        setattr(inst, name, result)
        return result


if __name__ == '__main__':
    class A(object):

        def __init__(self, n):
            self.n = n

        @cached_property
        def square(self):
            """
            Return square
            """
            return self.n * self.n

    a = A(2)
    print(a.square)
    print(a.square)
    a.square = 2
    print(a.square)
    del a.square
    print(a.square)
