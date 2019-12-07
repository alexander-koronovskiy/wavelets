from wavelets import haar_my, haar_lib
from WorkWData import signals, output_res


if __name__ == "__main__":
    # type signal, wavelet transformation
    type_signal = "constant"; type_transform = "haar"
    u = signals.constant()
    n = len(u)

    # my hwt example
    x = haar_my.haar_1d(n, u)
    y = haar_my.haar_1d_inverse(n, x)

    # save fig, output in file, output in console
    output_res.plot_wt(type_signal, type_transform, u, x, y)
    output_res.file_output('results/' + type_signal + '_' + type_transform + '.txt', u, x, y)
    output_res.console_output(u, x, y)
