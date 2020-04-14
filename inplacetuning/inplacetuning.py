'''In-place tuning.

References
----------
.. [1] https://en.wikipedia.org/wiki/Just_intonation
.. [2] https://pages.mtu.edu/~suits/notefreqs.html
.. [3] https://en.wikipedia.org/wiki/Interval_(music)
.. [4] http://www.huygens-fokker.org/docs/intervals.html
.. [5] https://www.musictheory.net/calculators/interval
'''

from collections import OrderedDict

import numpy as np
from scipy.optimize import minimize

from utils import _name_to_inverval

def combinations(x):
    '''Pairwise combinations in predictable order.'''

    pairs = OrderedDict()
    for x0 in x:
        for x1 in x:
            pairs[x1] = x0
            pairs[x0] = x1
    return zip(pairs.keys(), pairs.values())

def _get_ratios(freqs):
    '''Get ratio between frequencies.'''
    return [np.max(f0)/np.min(f0) for f0 in combinations(freqs)]

def inplacetuning(notes):
    '''Given a set of notes, return optimized frequencies.

    Parameters
    ----------
    notes : list of str
        Note names sounding concurrently.

    Returns
    -------
    freq_opt : list
        Optimized frequencies to preserve "just" intonation.
    freq_init : list
        Equal temperment frequencies.
    ratio_opt : list
        Ratios of optimized frequencies.
    ratio_desired : list
        Desired ratios between pairwise notes.
    ratio_init : list
        Ratios of equal temperment frequencies.
    cost
        Final objective function evaluation.

    Notes
    -----
    The idea is to examine input notes and infer the desired ratios
    between pairs of notes. The ratios will be satisfied for only the
    set of notes provided irrespective of unsupplied notes, hence
    the frequency optimization happens "in-place."

    The optimization starts with equal-tempered frequencies and
    ends with frequencies that satisfy the conditions of just
    intonation frequency ratios.
    '''

    # Sanity checks
    assert isinstance(notes, list), 'Must have a list of notes!'

    # Make sure notes provided are valid
    _notenames = [
        'a', 'a#', 'a##', 'ab', 'abb',
        'b', 'b#', 'b##', 'bb', 'bbb',
        'c', 'c#', 'c##', 'cb', 'cbb',
        'd', 'd#', 'd##', 'db', 'dbb',
        'e', 'e#', 'e##', 'eb', 'ebb',
        'f', 'f#', 'f##', 'fb', 'fbb',
        'g', 'g#', 'g##', 'gb', 'gbb'
    ]
    assert all([n0 in _notenames for n0 in notes]), (
        'Invalid note name provided!')

    # Get all pairwise relationships we need to optimize over
    # notes = sorted(notes) # rest of code assumes lexigraphic order
    pairs = combinations(notes)

    # Define what we "mean" when we say [interval type] between two
    # notes. I'll call this the "semantics" of the note group
    _semantics = {
        'P1': 1, # unison
        'A1': 25/24, # augmented unison
        'AA1': 1125/1024, # double augmented unison
        'dd2': 135/128, # double dimished second (maybe?)
        'd2': 128/125, # dimished second
        'm2': 16/15, # minor second
        'M2': 9/8, # major second
        'A2': 75/64, # augmented second
        'AA2': 10125/8192, # doubly augmented second
        'dd3': 2048/1875, # doubly dimished third
        'd3': 144/125, # dimished third
        'm3': 6/5, # minor third
        'M3': 5/4, # major third
        'A3': 125/96, # Augmented third
        'AA3': 5625/4096, # double augmented third
        'dd4': 4096/3375, # doubly dimished fourth
        'd4': 32/25, # dimished fourth
        'P4': 4/3, # perfect fourth
        'A4': 45/32, # augmented fourth
        'AA4': 375/256, # double augmented fourth
        'AAA4': 8/5, # triply augmented fourth (copy m6?)
        'ddd5': 5/4, # triply dimished fifth (copy M3?)
        'dd5': 512/375, # doubly dimished fifth
        'd5': 25/18, # dimished fifth
        'P5': 3/2, # perfect fifth
        'A5': 25/16, # augmented fifth
        'AA5': 3375/2048, # double augmented fifth
        'dd6': 8192/5625, # doubly dimished sixth
        'd6': 192/125, # dimished sixth
        'm6': 8/5, # minor sixth
        'M6': 5/3, # major sixth
        'A6': 125/72, # augmented sixth
        'AA6': 1875/1024, # double augmented sixth
        'dd7': 16384/10125, # doubly dimished seventh
        'd7': 128/75, # dimished seventh
        'm7': 16/9, # minor seventh
        'M7': 15/8, # major seventh
        'A7': 125/64, # augmented seventh
        'AA7': 1162261467/536870912, # double augmented seventh (Pyth)
        'dd8': 2048/1125, # doubly dimished octave
        'd8': 48/25, # dimished octave
        'P8': 2, # octave
    }

    # Get desired ratios according to semantics
    ratio_desired = np.array(
        [_semantics[_name_to_inverval(p0)] for p0 in pairs])

    # Get starting frequencies for notes (equal temperment)
    _nominal_freqs = {
        'abb': 783.99,
        'ab': 415.30,
        'a': 440,
        'a#': 466.16,
        'a##': 493.88,
        'bbb': 440,
        'bb': 466.16,
        'b': 493.88,
        'b#': 523.25,
        'b##': 554.37,
        'cb': 493.88,
        'c': 523.25,
        'c#': 554.37,
        'c##': 587.33,
        'dbb': 523.25,
        'db': 554.37,
        'd': 587.33,
        'd#': 622.25,
        'd##': 659.25,
        'ebb': 587.33,
        'eb': 622.25,
        'e': 659.25,
        'e#': 698.46,
        'e##': 739.99,
        'fb': 659.25,
        'f': 698.46,
        'f#': 739.99,
        'f##': 783.99,
        'gb': 739.99,
        'g': 783.99,
        'g#': 830.61,
        'g##': 440,
    }
    freq_init = [_nominal_freqs[n0] for n0 in notes]
    ratio_init = _get_ratios(freq_init)

    # Modify freqs to minize difference between ratios and
    # semantically desired ratios
    def _obj(x, ratio_desired):
        freq_ratios = _get_ratios(x) # all pairwise combinations
        return np.linalg.norm(freq_ratios - ratio_desired)

    # Do the thing:
    res = minimize(
        _obj,
        freq_init,
        bounds=[(1, np.inf)]*len(freq_init),
        args=(ratio_desired,))
    freq_opt, cost = res['x'], res['fun']
    ratio_opt = _get_ratios(freq_opt)

    # Return interesting outputs
    return(
        freq_opt, freq_init,
        ratio_opt, ratio_desired, ratio_init,
        cost)


if __name__ == '__main__':
    pass
