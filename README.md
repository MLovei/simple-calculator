# Calculator Package

## Overview

This Python package provides a simple calculator class with basic arithmetic operations, including addition, subtraction, multiplication, division, taking the root of a number, and resetting the calculator's memory.

## Installation

You can install the package using pip:

```bash
py -m pip install --index-url https://test.pypi.org/simple/ --no-deps calculations_MLovei

## Usage

from calculations_MLovei import calculator

# Create a calculator instance
c = calculator.Calculator()

# Add a value
result = c.add(69.715)
print(result)  # Output: 69.715

# Subtract a value
result = c.sub(13.715)
print(result)  # Output: 56.0

# Multiply by a value
result = c.mult(2.5)
print(result)  # Output: 140.0

# Divide by a value
result = c.div(7.5)
print(result)  # Output: 18.6666666667

# Take the root of the current value
result = c.root(3)
print(result)  # Output: 2.6527048053

# Reset the calculator
c.reset()
```
## Testing

To run the provided doctests, use the following:

```bash
#python calculator.py
```

This will run the doctests and ensure the functionality of the calculator class.
