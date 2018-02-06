import numpy as np
X = np.random.randn(10)

for i in range(10):
    s = np.sum(X[:i+1])
    print(s)
    print('ily')