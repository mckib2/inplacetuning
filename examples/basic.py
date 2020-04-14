'''Basic usage of inplace tuning.'''

import numpy as np
from scipy.io.wavfile import write
from inplacetuning import inplacetuning

if __name__ == '__main__':


    # Try a few triads out
    triads = [
        ['c', 'e', 'g'],
    ]

    freqs_opt = []
    freqs_eq = []
    for triad in triads:
        fopt, feq, ropt, rdes, rinit, cost = inplacetuning(triad)
        freqs_opt.append(fopt)
        freqs_eq.append(feq)

        print('Frequencies:')
        print('    fopt:', fopt)
        print('     feq:', feq)
        print('Ratios:')
        print('    rdes:', rdes)
        print('    ropt:', ropt)
        print('   rinit:', rinit)

    # make a sum of sines wave
    rate = 44100
    sec = 2
    t = np.linspace(0, sec, int(rate*sec), endpoint=False)
    res = []
    for fo, fe in zip(freqs_opt, freqs_eq):
        sine_opt = np.mean([np.sin(t*f*2*np.pi) for f in fo], axis=0)
        sine_eq = np.mean([np.sin(t*f*2*np.pi) for f in fe], axis=0)
        res.append(np.concatenate((sine_eq, sine_opt)))

    write('test.wav', rate=rate, data=np.concatenate(res))
