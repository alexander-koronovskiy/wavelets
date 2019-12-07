import haar_my
import haar_lib
import numpy as np
import matplotlib.pyplot as plt
from pylab import figure, plot, xlabel, grid, legend, title, savefig
from matplotlib.font_manager import FontProperties


# main method - comparison the result of different methods
def main():

    # signal - build as single function / module
    n = 40
    u = np.linspace(1, n, n)

    # lib method
    v = haar_lib.haar_1d(n, u)
    w = haar_lib.haar_1d_inverse(n, v)

    # my method
    x = haar_my.haar_1d(n, u)
    y = haar_my.haar_1d_inverse(n, v)

    # console output - build as single function / module
    print('')
    print('   i      U(i)        H(U)(i)  Hinv(H(U))(i)')
    print('')
    for i in range(n):
        print('  %2d  %10f  %10f  %10f' % (i, u[i], x[i], y[i]))

    # save results as png format - build as single function / module
    plt.plot(u)
    plt.plot(x)
    plt.plot(y)
    grid(True)
    plt.title("linear signal HWT")
    figure(1, figsize=(10, 8))
    xlabel('$Argument, x$')
    plt.ylabel('$Functions, u$')
    legend(('u(x)', 'H(u(x))', 'Hinv(H(u))(x)'), prop=FontProperties(size=12))
    savefig('HWT.png', dpi=150)
    plt.clf()


if __name__ == "__main__":
    main()
