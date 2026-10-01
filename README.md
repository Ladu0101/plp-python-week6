
# Question 1 - Safe Functions

- `safe_tools.py` - Contains three functions that safely handle common errors.
- `unbreakable.py` - Contains additional practice with error handling.
- `README.md` - Contains information about this assignment.

## Why can the `if` check not catch `abc` on its own?

The `if` check cannot catch `abc` because `int("abc")` causes a `ValueError` before the `if` statement can run. We use `try` and `except` to handle the error safely. 