from math import *
import matplotlib.pyplot as plt


def discreteHaarWaveletTransform(x):
    N = len(x)
    output = [0.0]*N
    length = N >> 1
    while True:
        for i in range(0, length):
            summ = x[i * 2] + x[i * 2 + 1]
            difference = x[i * 2] - x[i * 2 + 1]
            output[i] = summ
            output[length + i] = difference
        if length == 1:
            return output

        x = output[:length << 1]
        length >>= 1


N = 8
res = [1, 2, 3, 4]
# for k in range(N): print(res[k])
plt.plot(res); print(res)

res = discreteHaarWaveletTransform(res)
plt.plot(res); print(res)
res = discreteHaarWaveletTransform(res)
plt.plot(res); print(res)
plt.show()
