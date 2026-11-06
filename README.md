# Complex Square Root Calculator

A Python program that calculates the two square roots of a complex number using **SymPy** and the trigonometric (polar) form of complex numbers.

## Overview

Every non-zero complex number has exactly two square roots.

This program takes the real and imaginary components of a complex number as input and calculates both square roots using its modulus and argument.

## Mathematical Background

A complex number can be expressed as:

$$
z=x+yi
$$

Where:
- $x$ = Real part
- $y$ = Imaginary part
- $i=\sqrt{-1}$

### 1. Modulus

The modulus of a complex number is:

$$
r=|z|=\sqrt{x^2+y^2}
$$

### 2. Argument

The argument is calculated using:

$$
\theta=\mathrm{atan2}(y,x)
$$

### 3. Square Roots

Using the polar representation of a complex number, its two square roots are:

$$
\omega_1=\sqrt r\left(\cos\frac{\theta}{2}+i\sin\frac{\theta}{2}\right)
$$

$$
\omega_2=-\sqrt r\left(\cos\frac{\theta}{2}+i\sin\frac{\theta}{2}\right)
$$

The program uses SymPy to simplify and expand the resulting expressions.

## Requirements

- Python 3
- SymPy

Install SymPy using:

```bash
pip install sympy
```

## How to Run

1. Clone or download this repository.
2. Make sure SymPy is installed.
3. Run the Python file:

```bash
python main.py
```

4. Enter the real and imaginary parts when prompted.

## Example

**Input:**

```text
Re(z): 1
Im(z): sqrt(3)
```

**Output:**

```text
|z|: 2
θ: pi/3
ω1: sqrt(6)/2 + sqrt(2)*I/2
ω2: -sqrt(6)/2 - sqrt(2)*I/2
```

## Libraries Used

| Library | Purpose |
|---|---|
| SymPy | Symbolic mathematics and simplification |
| sqrt | Calculates square roots |
| sin, cos | Trigonometric calculations |
| atan2 | Calculates the argument |
| expand | Expands mathematical expressions |

## Concepts Demonstrated

- Complex numbers
- Modulus and argument
- Polar representation
- De Moivre's theorem
- Trigonometric identities
- Symbolic computation using Python

## Future Improvements

- Support for calculating nth roots of complex numbers.
- Graphical representation on the complex plane.
- Better input validation.
- Conversion between Cartesian and polar forms.
- Numerical approximations alongside exact symbolic answers.

---

*A small project exploring the intersection of complex analysis and Python programming.*
