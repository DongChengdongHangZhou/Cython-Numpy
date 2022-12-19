import numpy as np
import dot_cython
a = np.random.randn(100, 200).astype(np.float32)
b = np.random.randn(200, 50).astype(np.float32)
print(dot_cython.naive_dot(a,b))
