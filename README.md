# Uncommon Python TypeError Handling Bug
This repository demonstrates a subtle error related to exception handling in Python.  The `bug.py` file contains a function that attempts to handle both `ZeroDivisionError` and `TypeError`. However, if a `TypeError` occurs, it's not caught correctly due to the order of `except` blocks.
The `bugSolution.py` file provides the corrected version.
This is a good example of how the order of exception handling matters and how easily a seemingly simple piece of code can fail in unexpected ways. 