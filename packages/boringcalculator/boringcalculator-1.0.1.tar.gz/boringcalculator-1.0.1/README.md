## Source code of boring calculator

This python package is the logic source of boring calculator, which uses sympy.

### Commands available:

`calculate` is a command included when the package is installed, this command returns all the possible calculations for the input, it's in early development.

#### Options

| Command  |     Prefix     |                    Description                    |
| :------: | :------------: | :-----------------------------------------------: |
| Verbose  | -v, --verbose  |        Prints the steps of the computation        |
| Timeout  | -t, --timeout  | Set a timeout for the computation (defaults to 2) |
| Parallel | -p, --parallel |       Select whether or not use parallelism       |

### Building and distributing

- Building requires `build` package, it can be installed this way:

```bash
pip install build
```

```bash
python -m build -w # stack with -n to avoid creating a virtual environment
```

- **Note:** Source distribution does not work for now, as it does not include any files in the package _boringcalculator_. We have to figure out how to only include sources in sdist and only binaries on wheel
