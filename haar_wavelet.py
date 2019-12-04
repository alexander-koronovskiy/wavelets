import numpy as np
import math


# calculating HAAR matrices for linear array
def HaarMatrices(n):

    # check input parameter and make sure it's the power of 2
    Level1 = math.log(n, 2)
    Level = int(Level1)+1

    # Initialization, NC - normalization constant
    H = [1]
    NC = 1 / math.sqrt(2)
    LP = [1, 1]
    HP = [1, -1]

    # The core of the calculation; H - the result matrix
    for i in range(1, Level):
        H = np.dot(NC, np.concatenate([np.matrix(np.kron(H, LP)), np.matrix(np.kron(np.eye(len(H)), HP))]))

    return H


# application HAAR-Transform Wavelet for "signal" array
def haarFWT(signal, level):

    # scaling -- try 1 or ( 2 ** .5 )
    s = .5

    # h - lowpass filter
    # g - highpass filter
    # f - length of the filter
    h = [1,  1]
    g = [1, -1]
    f = len(h)

    # t - 'workspace' array
    # l - length of the current signal
    # y - initialise output
    t = signal
    l = len(t)
    y = [0] * l

    # padding for the workspace
    t = t + [0, 0]

    # y - initialise the next level
    # l2 - half approximation, half detail
    for i in range(level):
        y[0:l] = [0] * l
        l2 = l // 2

        for j in range(l2):
            for k in range(f):
                y[j] += t[2*j + k] * h[k] * s
                y[j+l2] += t[2*j + k] * g[k] * s

        # continue with the approximation
        l = l2
        t[0:l] = y[0:l]

    return y


# application method (1) for linear array
def HaarMatriciesExample(x):
    n = len(x)
    H = HaarMatrices(n)

    # haar transformation
    y = H.dot(x)
    print(y)

    # haar inverse transform
    x1 = H.transpose().dot(y.transpose())
    print(x1.transpose())


# application method (2) for linear array
def haarFWTExample(s0):

    print("level 0")
    print(s0)

    print("level 1")
    print(haarFWT(s0, 1))

    print("level 2")
    print(haarFWT(s0, 2))

    print("level 3")
    print(haarFWT(s0, 3))


# main method - comparison the result of different methods
def main():
    x = [1, -14, 28, 49, 5, 6, 7, 8]
    HaarMatriciesExample(x)

    # i'm think, it doesen't work correct
    # haarFWTExample(x)


if __name__ == "__main__":
    main()
