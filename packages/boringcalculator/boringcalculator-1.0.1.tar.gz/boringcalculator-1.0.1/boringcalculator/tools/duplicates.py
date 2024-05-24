import sympy

__all__ = ["removeRepeated"]


def removeRepeated(op, name="", *args, **kwargs):
    # print(op, name, args, kwargs)w
    if name == "input":
        return op
    if name == "result" and sympy.pretty(kwargs.get("original")) != sympy.pretty(op):
        # TODO: Sympy had errors here, this is horrible, I need to find a solution
        # original is self.function (which is the user input NOT EVALUATED), this function might return a different result than the original
        # even if the input is the same
        # example: x^2+5x-76 is the same as x^2+5x-1*76, sympy usually returns the second one when parse_expr has the parameter evaluate=False
        # why does sympy returns 1*76 instead of 76? when pretty is called, it returns 76, it's the **bad** solution I found
        return op
    if isinstance(op, sympy.Eq):
        return op
    if isinstance(op, (tuple, list)):
        r = tuple(filter(lambda x: x not in args, set(op)))
        if r:
            if len(r) == 1:
                return r[0]
            return r
    else:
        if op not in args:
            return op
