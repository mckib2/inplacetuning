'''In-place tuning.

References
----------
.. [1] https://en.wikipedia.org/wiki/Just_intonation
.. [2] https://pages.mtu.edu/~suits/notefreqs.html
.. [2] https://en.wikipedia.org/wiki/Interval_(music)
'''

from collections import OrderedDict

import numpy as np
from scipy.optimize import minimize

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

    # Make sure notes provided are valid -- only diatonic currently
    _notenames = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    assert all([n0 in _notenames for n0 in notes]), (
        'Invalid note name provided!')

    # Get all pairwise relationships we need to optimize over
    notes = sorted(notes) # rest of code assumes lexigraphic order
    pairs = combinations(notes)

    # Define what we "mean" when we say [interval type] between two
    # notes. I'll call this the "semantics" of the note group
    _semantics = {
        'P1': 1, # unison
        'P8': 2, # octave
        'P5': 3/2, # perfect fifth
        'P4': 4/3, # perfect fourth
        'M6': 5/3, # major sixth
        'M3': 5/4, # major third
        'm6': 8/5, # minor sixth
        'm3': 6/5, # minor third
        'M2': 9/8, # major second
        'm2': 16/15, # minor second
        'd5': 25/18, # dimished fifth
        'A4': 45/32, # augmented fourth
        'm7': 16/9, # minor seventh
        'M7': 15/8, # major seventh
    }

    # Map pairwise relationships to desired ratios -- only supports
    # diatonic currently
    _map = {
        'cc': 'P1',
        'cd': 'M2',
        'ce': 'M3',
        'cf': 'P4',
        'cg': 'P5',
        'ca': 'M6',
        'cb': 'M7',

        'dd': 'P1',
        'de': 'M2',
        'df': 'm3',
        'dg': 'P4',
        'da': 'P5',
        'db': 'M6',
        'dc': 'm7',

        'ee': 'P1',
        'ef': 'm2',
        'eg': 'm3',
        'ea': 'P4',
        'eb': 'P5',
        'ec': 'm6',
        'ed': 'm7',

        'ff': 'P1',
        'fg': 'M2',
        'fa': 'M3',
        'fb': 'A4',
        'fc': 'P5',
        'fd': 'M6',
        'fe': 'M7',

        'gg': 'P1',
        'ga': 'M2',
        'gb': 'M3',
        'gc': 'P4',
        'gd': 'P5',
        'ge': 'M6',
        'gf': 'm7',

        'aa': 'P1',
        'ab': 'M2',
        'ac': 'm3',
        'ad': 'P4',
        'ae': 'P5',
        'af': 'm6',
        'ag': 'm7',

        'bb': 'P1',
        'bc': 'm2',
        'bd': 'm3',
        'be': 'P4',
        'bf': 'd5',
        'bg': 'm6',
        'ba': 'm7',
    }

    # Get desired ratios according to semantics
    ratio_desired = np.array(
        [_semantics[_map[p0[0] + p0[1]]] for p0 in pairs])

    # Get starting frequencies for notes (equal temperment)
    _nominal_freqs = {
        'a': 440,
        'b': 493.88,
        'c': 523.25,
        'd': 587.33,
        'e': 659.25,
        'f': 698.46,
        'g': 783.99,
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

    # notes = ['c', 'e', 'g']
    # notes = ['d', 'f', 'a', 'c', 'e']
    # notes = ['e', 'g', 'b']
    notes = ['f', 'a', 'c', 'e']
    (freq_opt, freq_eq,
     ratio_opt, ratio_desired, ratio_init,
     cost) = inplacetuning(notes)

    print(freq_eq)
    print(freq_opt)
    print(ratio_desired)
    print(ratio_opt)
    print(ratio_init)
    print(cost)
