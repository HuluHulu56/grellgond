# The Grellgond Constant (ℷ)

The **Grellgond constant** (symbol: ℷ, Gimel) is a mathematical constant defined as the decimal concatenation of the sequence of strictly increasing maximal prime gaps.

## Mathematical Definition

Let *p_n* denote the *n*-th prime number. A maximal prime gap *g_k* is defined as a gap between consecutive primes that is strictly greater than all preceding prime gaps. 

The sequence of maximal prime gaps *G* begins: 
`G = (1, 2, 4, 6, 8, 14, 18, 20, 22, 34, ...)` (OEIS A005250)

The Grellgond constant ℷ is defined as the concatenation of the base-10 digits of the sequence *G*, prefixed by `0.`:

`ℷ = 0.12468141820223436...`

## Installation

You can install the official calculation library via pip:
```bash
pip install grellgond
```

## Usage

### In Python
```python
from grellgond import gimel

# Print the constant (pre-calculated approximation)
print(gimel)
# Output: ℷ (Grellgond Constant) ≈ 0.1246814182022343644

# Dynamically calculate exact digits up to a prime limit
exact_digits = gimel.calculate_digits(prime_limit=100000)
print(exact_digits)
```

### Command Line Interface (CLI)
After installing, calculate the constant directly from your terminal:
```bash
grellgond --limit 100000
```

## Authors
Created and formalized by Simon and Viliam.