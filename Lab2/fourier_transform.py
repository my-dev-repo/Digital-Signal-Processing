from pylab import *
from digital_signals import *
from cmath import exp, pi

def main():
    imp_sig = ImpulseSignal()
    make_fourier_transform(imp_sig)

    gaus_sig = GaussianSignal()
    make_fourier_transform(gaus_sig)

    plot_signal((imp_sig,gaus_sig))


def make_fourier_transform(sig):
    signal_vectorized = vectorize(sig.signal)

    sig.x_ideal = linspace(-sig.global_limit, sig.global_limit, sig.ideal_samples)
    sig.y_ideal = signal_vectorized(sig.x_ideal)

    sig.x_dft = linspace(-sig.global_limit, sig.global_limit, sig.dft_samples)
    sig.y_dft = signal_vectorized(sig.x_dft)

    sig.w_dft = linspace(0, 1.0/(2.0*sig.dt), sig.dft_samples/2)
    sig.f_dft = abs(array(compute_dft(sig.y_dft))[0:sig.dft_samples/2])

    sig.f_fft = abs(fftpack.fft(sig.y_dft)[0:sig.dft_samples/2])


def compute_dft(input):
    n = len(input)
    output = [complex(0)] * n
    for k in range(n):  # For each output element
        s = complex(0)
        for t in range(n):  # For each input element
            s += input[t] * exp(-2j * pi * t * k / n)
        output[k] = s
    return output

def plot_signal(signals):
    """
    Plots signals

    signals - list of DigitalSignal objects for plotting
    """
    num = len(signals)

    fig, axes = plt.subplots(num, 3)
    for n,sg in enumerate(signals):
        axes[n,0].set_title(sg.title)
        axes[n,0].plot(sg.x_ideal, sg.y_ideal, 'r')

        axes[n,1].set_title('Discrete Fourier Transform')
        axes[n,1].stem(sg.w_dft, sg.f_dft)

        axes[n,2].set_title('Fast Fourier Transform')
        axes[n,2].stem(sg.w_dft, sg.f_fft)

        for axis in axes[n]:
            axis.margins(0.05)
            axis.axis('tight')
            axis.grid(True)

    plt.tight_layout()
    plt.show()

# def plot_signal(signals):
#     """
#     Plots signals
#
#     signals - list of DigitalSignal objects for plotting
#     """
#     shp = signals.shape
#     fig, axes = plt.subplots(shp[0], shp[1])
#
#     for axis, sg in zip(axes, signals):
#         axis.margins(0.05)
#         axis.plot(sg.x_ideal, sg.y_ideal, 'r', lw=2)
#         axis.plot(sg.w_dft, sg.f_dft, 'g', marker='o', markersize=4)
#         axis.axis('tight')
#         axis.grid(True)
#         axis.set_title(sg.title)
#
#     plt.tight_layout()
#     plt.show()


if __name__ == "__main__":
    main()