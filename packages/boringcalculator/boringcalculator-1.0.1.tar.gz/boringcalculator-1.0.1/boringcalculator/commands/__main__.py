import argparse
import logging

import colorama
import coloredlogs

import boringcalculator

colorama.init()
parser = argparse.ArgumentParser()
parser.add_argument("function", type=str, help="The function to compute")
parser.add_argument(
    "--verbose",
    "-v",
    action="count",
    help="Prints the steps of the computation. Can be stacked [WARNINGS, INFO]",
    default=0,
)
parser.add_argument(
    "--parallel",
    "-p",
    action="store_true",
    help="Use parallel computation",
    default=True,
)
parser.add_argument(
    "--timeout",
    "-t",
    type=int,
    help="Set a timeout for the computation (defaults to %(default)s)",
    default=2,
)
args = parser.parse_args()

if args.verbose == 0:
    level = logging.CRITICAL
elif args.verbose == 1:
    level = logging.WARNING
elif args.verbose == 2:
    level = logging.INFO
else:
    level = logging.DEBUG

coloredlogs.install(level=level)


def main():
    bc = boringcalculator.BasicOperationProcessor(args.function, printResults=True)
    bc.fullCompute(timeout=args.timeout, parallel=args.parallel)


if __name__ == "__main__":
    main()
