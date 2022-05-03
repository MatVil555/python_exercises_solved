# for task 10
class InvalidOperationException(Exception):
    pass


# for task 12
class EvenStream(object):
    def __init__(self):
        self.current = -2

    def get_next(self):
        self.current += 2
        return self.current


class OddStream(object):
    def __init__(self):
        self.current = -1

    def get_next(self):
        self.current += 2
        return self.current
