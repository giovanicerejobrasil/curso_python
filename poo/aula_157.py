"""
Classes decoradoras (Decorator Classes)
"""


class Multiplying:
    def __init__(self, multiplier):
        self._multiplier = multiplier

    def __call__(self, func):
        def internal(*args, **kwargs):
            return func(*args, **kwargs) * self._multiplier

        return internal


@Multiplying(9)
def sum_(x, y):
    return x + y


two_plus_four = sum_(2, 4)
print(two_plus_four)
