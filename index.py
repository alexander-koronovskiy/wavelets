from wavelets import haar_my
from WorkWData import signals, output_res


if __name__ == "__main__":
    # type signal, wavelet transformation
    type_transform = "DobWT"
    type_signal = "linear"
    u = signals.linear()
    n = len(u)

    # task 1. my hwt example
    # x = haar_my.haar_1d(n, u)
    # y = haar_my.haar_1d_inverse(n, x)

    output_res.write_to_file(u, 'signals/' + type_signal + '.txt')

    # task 2. Dobeshi realisation with matlab code help
    x = output_res.write_to_list('signals/' + type_signal + '_DobWT.txt')
    y = output_res.write_to_list('signals/' + type_signal + '_invDobWT.txt')

    # save fig, output in file, output in console
    output_res.plot_wt(type_signal, type_transform, u, x, y)
    output_res.file_output('signals/' + type_signal + '_' + type_transform + '_all.txt', u, x, y)
    output_res.console_output(u, x, y)
