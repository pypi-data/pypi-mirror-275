import sys


class increase_recursionlimit:
    def __init__(self, new_limit=2**31 - 1):
        self.new_limit = new_limit
        self.previous_limit = None

    def __enter__(self):
        self.previous_limit = sys.getrecursionlimit()
        sys.setrecursionlimit(self.new_limit)

    def __exit__(self, *args):
        del args
        assert self.previous_limit is not None
        sys.setrecursionlimit(self.previous_limit)
