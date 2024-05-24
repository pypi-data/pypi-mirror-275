"""
Copyright © 2023 Boring Calculator - All rights reserved.
Written by Sirenityk in GitHub
"""

import base64
import gc
import io
import logging
import multiprocessing.dummy as multiprocessing
import urllib
from multiprocessing.context import TimeoutError as ProcessTimeoutError

import sympy
import termcolor
from sympy.calculus.util import continuous_domain, function_range
from sympy.plotting import plot
from sympy.simplify import FU

from .. import parsing, tools

logger = logging.getLogger(__name__)

# I just noticed that using dummy multiprocessing is faster than using the normal one
# certainly python takes it's time forking processes so that means
# that I've been wasting my time I wanna die

__all__ = ["OperationProcessor", "BasicOperationProcessor"]


def Integral(expr, b=None, a=None):
    if expr.is_number:
        var = sympy.symbols("x")
    else:
        var = list(expr.free_symbols)[0]

    if not b:
        return sympy.Integral(expr, var)
    return sympy.Integral(expr, (var, b, a))


def Sum(expr, b, a=0):
    var = list(expr.free_symbols)[0]
    if isinstance(b, tuple):
        return sympy.Sum(expr, b)
    return sympy.Sum(expr, (var, b, a))


class OperationProcessor:
    def __init__(self, operation, printResults=False):
        self.results = {}
        self.operation = operation
        self.variable = sympy.symbols(parsing.maxchar(operation))
        self.printResults = printResults

        self.dict_fixes = {
            # Variables
            "i": sympy.core.numbers.I,
            "e": sympy.core.numbers.E,
            "W": sympy.LambertW,
            # Functions
            "Integral": Integral,
            "Sum": Sum,
        }

        self.function = sympy.parse_expr(
            parsing.calcSyntax(str(self.operation)),
            local_dict=self.dict_fixes,
            transformations="all",
            evaluate=False,
        )

        self.v = (
            sympy.sin,
            sympy.cos,
            sympy.tan,
            sympy.sec,
            sympy.csc,
            sympy.cot,
            sympy.asin,
            sympy.acos,
            sympy.atan,
            sympy.asec,
            sympy.acsc,
            sympy.acot,
            sympy.sinh,
            sympy.cosh,
            sympy.tanh,
            sympy.coth,
            sympy.sech,
            sympy.csch,
            sympy.asinh,
            sympy.acosh,
            sympy.atanh,
            sympy.acoth,
            sympy.asech,
            sympy.acsch,
        )
        self.classes = (
            sympy.core.relational.Equality,
            sympy.core.relational.GreaterThan,
            sympy.core.relational.LessThan,
            sympy.core.relational.StrictGreaterThan,
            sympy.core.relational.StrictLessThan,
            sympy.logic.boolalg.BooleanFalse,
            sympy.logic.boolalg.BooleanTrue,
        )

        self.f = self.function.doit()  # TODO: test this self.f replacement

    def addResults(self, name: str, result: any):
        """
        Adds the given result to the dictionary of results under the specified name.
        """
        result = tools.duplicates.removeRepeated(
            result, name, self.f, original=self.function
        )
        # if name == 'input' and result != self.function
        if result is not None:
            logger.info(f"Adding result {result} to {name}")
            self.results[name] = result
            if self.printResults:
                name = termcolor.colored(name.title(), "cyan")
                print(name)
                if isinstance(result, (list, tuple, set)):
                    for i in result:
                        outrepr = parsing.pretty(i)
                        lenout = map(len, outrepr.splitlines())

                        print(termcolor.colored(outrepr, "green"))
                        if result[-1] != i:
                            print(
                                termcolor.colored(
                                    "─" * max(lenout) + "─" * 3, "magenta"
                                )
                            )
                else:
                    result = termcolor.colored(parsing.pretty(result), "green")
                    print(result)

    def graph(self, graphType=plot, backend="matplotlib"):
        logger.info("Generating graph")
        """
        Generate a graph of the function.
        
        Parameters:
        - graphType (optional): The type of graph to generate. Defaults to 'plot'.

        Returns:
        - image: The generated graph as an image in base64 format, or an empty string if the function is not drawable.
        """
        # TODO: Add result as an ASCII plot when the `backend` parameter is 'text', so it can work with the
        #  `calculate` command
        if (
            not isinstance(self.f, (tuple, set, dict))
            and not isinstance(self.f, self.classes)
            and not self.f.is_number
        ):
            try:
                fig = graphType(
                    sympy.Piecewise(
                        (
                            sympy.oo,
                            abs(1 / self.f.rewrite(sympy.gamma)) < 1 / sympy.S(100),
                        ),
                        (self.f.rewrite(sympy.gamma), True),
                    ),
                    show=False,
                )
                buf = io.BytesIO()
                fig.save(buf)
                buf.seek(0)
                string = base64.b64encode(buf.read())
                uri = "data:image/png;base64," + urllib.parse.quote(string)
                image = uri

                self.addResults("graph", image)
                del image, buf, string, uri, fig
                gc.collect()
            except:
                pass

        else:
            logger.warning("Failed to plot the function")

    def integrate(self):
        # TODO: Fix this code or make it better, more understandable, the guy who did this had 2 months of python
        #  experience
        integral = ""
        if not isinstance(self.f, self.classes) and (
            "Integral" not in str(self.f) and "Derivative" not in str(self.f)
        ):
            if isinstance(
                sympy.integrate(self.f, self.variable, risch=True),
                sympy.integrals.risch.NonElementaryIntegral,
            ):
                logger.info("Calculated integral is not elementary")
                self.addResults("integral", "Integral is not elementary")
                return

            try:
                int_eval = sympy.integrate(self.f, self.variable, manual=True)
                if "Integral" in str(int_eval):
                    int_eval = sympy.integrate(self.f, self.variable)
            except:
                try:
                    int_eval = sympy.integrate(self.f, self.variable)
                except:
                    self.addResults("integral", "Could not solve this integral")

            if not isinstance(int_eval, sympy.Integral) or "Integral" not in str(
                int_eval
            ):
                integral = sympy.Eq(
                    sympy.Integral(self.f, self.variable), int_eval, evaluate=False
                )

            else:
                self.addResults("integral", "Could not solve this integral")

        else:
            return
        self.addResults("integral", integral)

    def derivative(self):
        derivative = sympy.Eq(
            sympy.Derivative(self.f, self.variable),
            sympy.diff(self.f, self.variable),
            evaluate=False,
        )
        self.addResults("derivative", derivative)

    def series(self):
        """
        Calculate the series expansion of the function.
        """

        r = sympy.series(self.f, self.variable)
        self.addResults("series", r)

    def apart(self):
        """
        Perform partial fraction decomposition on the given expression.
        """
        try:
            r = sympy.apart(self.f)
            self.addResults("apart", r)
        except NotImplementedError:
            logger.warning(
                "Partial fraction decomposition is not implemented for this expression, skipping"
            )

    def domain(self):
        domain = continuous_domain(self.f, self.variable, sympy.S.Reals)
        self.addResults("domain", domain)

    def range(self):
        range = function_range(self.function, self.variable, sympy.S.Reals)
        self.addResults("range", range)


class BasicOperationProcessor(OperationProcessor):
    def __init__(self, operation, printResults=False):
        super().__init__(operation, printResults=printResults)
        self.functions = {
            "input": self.function,
            "result": self.f,
            "apart": self.apart,
            "findAlternativeForms": self.findAlternativeForms,
            "findTrigAlts": self.findTrigAlts,
            "findRoots": self.findRoots,
            "domain": self.domain,
            "range": self.range,
            "derivative": self.derivative,
            "integrate": self.integrate,
            "series": self.series,
            # 'graph': self.graph,
        }

    def execute(self, evaluate=True, parseToLatex=False):
        if not evaluate:
            result = self.function
        else:
            op = self.f.simplify()
            result = op
        if parseToLatex:
            result = parsing.tomathjax(result)
        return result

    def executeTask(self, task):
        if task in self.functions.keys():
            f = self.functions[task]
            if callable(f):
                f()
            else:
                self.addResults(task, f)

    def fullCompute(self, timeout=2, parallel=True):
        functions = self.functions.keys()
        if parallel:
            with multiprocessing.Pool() as pool:
                for task in functions:
                    try:
                        res = pool.apply_async(self.executeTask, args=(task,))
                        res.get(timeout=timeout)
                    except ProcessTimeoutError:
                        logger.warning(f"Function {task} timed out")
                    except Exception as e:
                        logger.warning(
                            f"Function {task} failed with {e.__class__.__name__} exception: {e}"
                        )
        else:
            logger.warning("Note that parallel computations disable the timeout")
            for task in functions:
                try:
                    self.executeTask(task)
                except Exception as e:
                    logger.warning(
                        f"Function {task} failed with {e.__class__.__name__} exception: {e}"
                    )

    def findRoots(self):
        """-
        Finds the roots of the equation represented by the function `self.f`.
        """
        logger.info("Finding roots")

        roots = sympy.solveset(self.f, self.variable)
        if isinstance(roots, (set, sympy.sets.sets.FiniteSet)):
            r = list(roots)
            self.addResults("roots", r)

        else:
            self.addResults("roots", [roots])

    def findAlternativeForms(self):
        """
        Finds alternative forms of the expression.

        This method finds alternative forms of the expression by applying various rewrite rules.
        The alternative forms are stored in a set and then added to the results queue.
        """
        logger.info("Finding alternative forms")

        alts = [sympy.together(self.f)]
        mem = sympy.nsimplify(self.f)
        if mem != self.f:
            alts.append(mem)
        alts.append(self.f.rewrite(sympy.sqrt))
        alts.append(self.f.rewrite(sympy.exp))
        alts.append(self.f.rewrite(sympy.log))
        alts.append(self.f.rewrite(sympy.gamma))
        alts.append(self.f.rewrite(sympy.factorial))

        self.addResults("alternativeForms", alts)

    def findTrigAlts(self):
        """
        Finds alternative trigonometric representations of the function.

        This method checks if the function contains any trigonometric atoms and
        generates alternative representations for them. It uses the FU functions
        to rewrite the function and applies them to each variable in the function.
        Additionally, it applies the FU functions to the function itself, excluding
        the 'L' function. Finally, it puts the set of alternative representations
        in the `results_queue` and returns the list of alternative representations.
        """
        logger.info("Finding trigonometric alternative forms")

        if self.f.atoms(*self.v):
            trigId = [self.f]
            for i in self.v:
                trigId.append(self.f.rewrite(i))
            for i in filter(lambda x: x != "L", list(FU)):
                trigId.append(sympy.together(FU.get(i)(self.f)))
            self.addResults("trigAlts", trigId)
