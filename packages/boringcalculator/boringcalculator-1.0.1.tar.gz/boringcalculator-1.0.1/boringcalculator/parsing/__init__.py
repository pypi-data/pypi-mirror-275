"""
Copyright © 2023 Boring Calculator - All rights reserved.
Written by Sirenityk in GitHub
"""

import re

import sympy


def fn(x):
    """
    Returns `x` if the number is x.

    `x` must be a sympy object.

    Rounds the number in case the number isn't actually integer.

    Returns the introduced value in case of an exception.

    EXAMPLES:
    ========

    >>> fn(2.0)
    2
    >>> fn(3.0000000000)
    3
    >>> fn(3.14)
    3.14
    >>> fn(3+2.0*sympy.I)
    3 + 2*I
    >>> fn(4.340000+3.5000*sympy.I)
    4.34 + 3.5*I
    """
    try:
        v = []
        for i in x.as_real_imag():
            if not float(i) % 1:
                v.append(int(float(i)))
            else:
                v.append(i)
        return v[0] + v[1] * sympy.I
    except:
        return x


def rev(item: dict) -> dict:
    def rev1(item: dict, args) -> dict:
        result = item.copy()
        for key in item.keys():
            if result[key] in args:
                result.pop(key)
        return result

    result = {}
    for key, value in item.items():
        if value not in result.values():
            if isinstance(value, dict):
                b = item.copy()
                b.pop(key)
                value = rev1(value, args=list(b.values()))
            result[key] = value
    return result


def calcSyntax(text: str) -> str:
    """
    Returns a correct interpretation of all functions included in the calculator so SymPy can calculate everything correctly.

    Examples
    ========

    >>> calcSyntax('lambertw')
    'LambertW'

    >>> calcSyntax('productlog')
    'LambertW'
    """

    replacements = {
        "∫": "Integral",
        "[Σ∑]": "Sum",
        "√": "sqrt",
        "∞": "oo",
        "π": "pi",
        "Γ": "gamma",
        chr(8226): "*",
        chr(8211): "-",
    }

    for key, value in replacements.items():
        text = re.sub(key, value, text)

    text = text.replace("[", "(").replace("{", "(").replace("]", ")").replace("}", ")")
    text = (
        text.replace(":", "/")
        .replace("\\", "/")
        .replace("productlog", "LambertW")
        .replace("lambertw", "LambertW")
        .replace("mod", r"%")
        .replace("eulergamma", "EulerGamma")
    )
    words = [
        "Chi",
        "Shi",
        "Ci",
        "Si",
        "Li",
        "li",
        "E1",
        "expint",
        "Ei",
        "erf2inv",
        "erfcinv",
        "erfinv",
        "erf2",
        "erfi",
        "erfc",
        "erf",
        "piecewise_fold",
        "Piecewise",
        "frac",
        "ceiling",
        "floor",
        "acsch",
        "asech",
        "acoth",
        "atanh",
        "acosh",
        "asinh",
        "csch",
        "sech",
        "coth",
        "tanh",
        "cosh",
        "sinh",
        "LambertW",
        "log",
        "ln",
        "exp",
        "atan2",
        "acot",
        "acsc",
        "asec",
        "atan",
        "acos",
        "asin",
        "sinc",
        "cot",
        "csc",
        "sec",
        "tan",
        "cos",
        "sin",
        "gamma",
        "factorial",
        "sqrt",
        "abs",
        "zeta",
        "pi",
        "cbrt",
    ]
    words_fix = [" " + i + " " for i in words]
    for i in range(len(words)):
        text = text.replace(words[i], words_fix[i])
    text = (
        text.replace("a   sin h", "asinh")
        .replace("a  cos h", "acosh")
        .replace("a  tan h", "atanh")
        .replace("a  csc h", "acsch")
        .replace("a  sec h", "asech")
        .replace("a  cot h", "acoth")
        .replace("a sin", "asin")
        .replace("a cos", "acos")
        .replace("a tan", "atan")
        .replace("a sec", "asec")
        .replace("a csc", "acsc")
        .replace("a cot", "cot")
        .replace("sin h", "sinh")
        .replace("cos h", "cosh")
        .replace("tan h", "tanh")
        .replace("cot h", "coth")
        .replace("sec h", "sech")
        .replace("csc h", "csch")
        .replace("poly gamma", "polygamma")
    )
    text = (
        text.replace("summation", "Sum")
        .replace("sum", "Sum")
        .replace("integrate", "Integral")
        .replace("integral", "Integral")
        .replace("diff", "Derivative")
        .replace("derivative", "Derivative")
    )
    return text


def returning(text: str, integral=False, var=sympy.Symbol("x"), center=False) -> str:
    """
    Returns the common notation of specific functions to make it more human-understandable.

    Examples
    ========

    >>> returning('polygamma') # Translates such function to its latex form.
    r'\psi'
    """

    if not text.replace(r"\mathtt{\text{}}", ""):
        return ""
    text = (
        text.replace("polygamma", "\\psi")
        .replace("log", "ln")
        .replace(r"1 \cdot ", "")
        .replace(r"\left(-1\right)^", r"\left(-1 \right)^")
        .replace(r"\left(-1\right)", "-")
        .replace("asinh", "sinh^{-1}")
        .replace("acosh", "cosh^{-1}")
        .replace("atanh", "tanh^{-1}")
        .replace("acsch", "csch^{-1}")
        .replace("asech", "sech^{-1}")
        .replace("acoth", "coth^{-1}")
        .replace("asin", "sin^{-1}")
        .replace("acos", "cos^{-1}")
        .replace("atan", "tan^{-1}")
        .replace("acsc", "csc^{-1}")
        .replace("asec", "sec^{-1}")
        .replace("acot", "cot^{-1}")
    )

    if integral:
        if "C" in text:
            text += r"+\text{constant}"
        else:
            text += "+C"
    return text


def tomathjax(f):
    return returning(sympy.latex(f))


def maxchar(text: str) -> str:
    """
    In order to suppose a variable to work with, :func:`maxchar(text)` returns the most repeated character of the introduced parameter,
    letting :func:`calc` work with a specific variable.

    Example
    =======

    >>> maxchar('x^t*x') # 'x' repeats 2 times, while 't' is single.
    'x'
    """
    textExceptions = [
        "series",
        "mod",
        "integrate",
        "diff",
        "summation",
        "EulerGamma",
        "integral",
        "derivative",
        "pi",
        "betainc_regularized",
        "betainc",
        "riemann_xi",
        "mathieucprime",
        "mathieusprime",
        "mathieuc",
        "mathieus",
        "beta",
        "elliptic_pi",
        "elliptic_e",
        "elliptic_f",
        "elliptic_k",
        "Znm",
        "Ynm_c",
        "Ynm",
        "jacobi_normalized",
        "jacobi",
        "gegenbauer",
        "assoc_laguerre",
        "laguerre",
        "chebyshevt_root",
        "chebyshevu_root",
        "chebyshevu",
        "chebyshevt",
        "hermite",
        "assoc_legendre",
        "legendre",
        "appellf1",
        "meijerg",
        "hyper",
        "marcumq",
        "airybiprime",
        "airyaiprime",
        "airybi",
        "airyai",
        "hn2",
        "hn1",
        "jn_zeros",
        "yn",
        "jn",
        "hankel2",
        "hankel1",
        "besselk",
        "besseli",
        "bessely",
        "besselj",
        "interpolating_spline",
        "bspline_basis_set",
        "bspline_basis",
        "Heaviside",
        "DiracDelta",
        "SingularityFunction",
        "KroneckerDelta",
        "LeviCivita",
        "Eijk",
        "stieltjes",
        "polylog",
        "lerchphi",
        "zeta",
        "dirichlet_eta",
        "EulerGamma",
        "multigamma",
        "trigamma",
        "digamma",
        "loggamma",
        "polygamma",
        "uppergamma",
        "lowergamma",
        "gamma",
        "fresnelc",
        "fresnels",
        "Chi",
        "Shi",
        "Ci",
        "Si",
        "Li",
        "li",
        "E1",
        "expint",
        "Ei",
        "erf2inv",
        "erfcinv",
        "erfinv",
        "erf2",
        "erfi",
        "erfc",
        "erf",
        "piecewise_fold",
        "Piecewise",
        "frac",
        "ceiling",
        "floor",
        "acsch",
        "asech",
        "acoth",
        "atanh",
        "acosh",
        "asinh",
        "csch",
        "sech",
        "coth",
        "tanh",
        "cosh",
        "sinh",
        "LambertW",
        "log",
        "ln",
        "exp_polar",
        "exp",
        "atan2",
        "acot",
        "acsc",
        "asec",
        "atan",
        "acos",
        "asin",
        "sinc",
        "cot",
        "csc",
        "sec",
        "tan",
        "cos",
        "sin",
        "unpolarify",
        "polarify",
        "adjoint",
        "transpose",
        "principal_branch",
        "unbranched_argument",
        "periodic_argument",
        "polar_lift",
        "arg",
        "conjugate",
        "Abs",
        "abs",
        "sign",
        "im",
        "re",
        "cbrt",
        "Rem",
        "real_root",
        "Id",
        "Max",
        "Min",
        "root",
        "sqrt",
        "partition",
        "genocchi",
        "catalan",
        "euler",
        "bell",
        "bernoulli",
        "harmonic",
        "tribonacci",
        "motzkin",
        "lucas",
        "fibonacci",
        "carmichael",
        "subfactorial",
        "FallingFactorial",
        "RisingFactorial",
        "binomial",
        "ff",
        "rf",
        "factorial2",
        "factorial",
        "i",
        "e",
        "oo",
        "W",
    ]
    # Remove characters from textExceptions
    for exc in textExceptions:
        text = text.replace(exc, "")

    # Create a dictionary to store character frequencies
    char_count = {}

    # Count character frequencies
    for char in text:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1

    if char_count:
        return max(char_count, key=char_count.get)
    else:
        return "x"


def pretty(obj):
    return sympy.pretty(obj)
