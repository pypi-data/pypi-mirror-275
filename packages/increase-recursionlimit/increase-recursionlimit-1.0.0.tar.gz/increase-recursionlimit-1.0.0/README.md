
# increase_recursionlimit

Context manager to increase the recursion limit temporarily.

```python
from increase_recursionlimit import increase_recursionlimit

with increase_recursionlimit(10000):
    # do something that requires a higher recursion limit
    pass
```

If you don't pass a value to `increase_recursionlimit`, it will increase the recursion limit to 2^31 - 1,
the maximum value allowed by Python.
