__author__ = "Michael E Miles"


def func(p1, p2, *args, k, **kwargs) -> None:
    """
    purely theoretical function.

    :param p1: positional or keyword parameter
    :param p2: positional or keyword parameter
    :param args:  variable, positional parameter
    :param k: keyword parameter
    :param kwargs: variable keyword parameter
    """
    print("positional-or-keyword:... {}, {}".format(p1, p2))
    print("var-positional (*args):.. {}".format(args))
    print("keyword:................. {}".format(k))
    print("var-keyword (**kwargs):...{}".format(kwargs))


func(1, 2, 3, 4, 5, 9, k=6, Mike=58, Rick=73, Tyra=68, Chris=70, Diane=56)