import numpy as np

x = np.array([0, 100, 255], dtype=np.uint8)
print(x)

# overflow
x = x + 1
print(x)


# underflow
x = x - 2
print(x)

#softmax
def softmax(z):
    return np.exp(z)/sum(np.exp(z))

a = np.full(5, 1)

softmax(a)
print(a)


def softmax_estable(z):
    z = z - np.max(z)
    return np.exp(z)/sum(np.exp(z))

b = np.full(5, 1)
softmax_estable(b)
print(b)

c = np.full(5, 1e10)
softmax_estable(c)
print(c)


