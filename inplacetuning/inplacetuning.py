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

def _name_to_inverval(pair):
    '''Lookup interval from pair of notes.'''

    return {

        ('cbb', 'cbb'): 'P1',
        ('cbb', 'cb'): 'A1',
        ('cbb', 'dbbbb'): 'd2',
        ('cbb', 'dbbb'): 'm2',
        ('cbb', 'dbb'): 'M2',
        ('cbb', 'db'): 'A2',
        ('cbb', 'ebbbb'): 'd3',
        ('cbb', 'ebbb'): 'm3',
        ('cbb', 'ebb'): 'M3',
        ('cbb', 'eb'): 'A3',
        ('cbb', 'fbbb'): 'd4',
        ('cbb', 'fbb'): 'P4',
        ('cbb', 'fb'): 'A4',
        ('cbb', 'gbbb'): 'd5',
        ('cbb', 'gbb'): 'P5',
        ('cbb', 'gb'): 'A5',
        ('cbb', 'abbbb'): 'd6',
        ('cbb', 'abbb'): 'm6',
        ('cbb', 'abb'): 'M6',
        ('cbb', 'ab'): 'A6',
        ('cbb', 'bbbbb'): 'd7',
        ('cbb', 'bbbb'): 'm7',
        ('cbb', 'bbb'): 'M7',
        ('cbb', 'bb'): 'A7',
        ('cbb', 'cbbb'): 'd8',

        ('cb', 'cb'): 'P1',
        ('cb', 'c'): 'A1',
        ('cb', 'dbbb'): 'd2',
        ('cb', 'dbb'): 'm2',
        ('cb', 'db'): 'M2',
        ('cb', 'd'): 'A2',
        ('cb', 'ebbb'): 'd3',
        ('cb', 'ebb'): 'm3',
        ('cb', 'eb'): 'M3',
        ('cb', 'e'): 'A3',
        ('cb', 'fbb'): 'd4',
        ('cb', 'fb'): 'P4',
        ('cb', 'f'): 'A4',
        ('cb', 'gbb'): 'd5',
        ('cb', 'gb'): 'P5',
        ('cb', 'g'): 'A5',
        ('cb', 'abbb'): 'd6',
        ('cb', 'abb'): 'm6',
        ('cb', 'ab'): 'M6',
        ('cb', 'a'): 'A6',
        ('cb', 'bbbb'): 'd7',
        ('cb', 'bbb'): 'm7',
        ('cb', 'bb'): 'M7',
        ('cb', 'b'): 'A7',
        ('cb', 'cbb'): 'd8',

        ('c', 'c'): 'P1',
        ('c', 'c#'): 'A1',
        ('c', 'c##'): 'm2', # technically?
        ('c', 'dbb'): 'd2',
        ('c', 'db'): 'm2',
        ('c', 'd'): 'M2',
        ('c', 'd#'): 'A2',
        ('c', 'ebb'): 'd3',
        ('c', 'eb'): 'm3',
        ('c', 'e'): 'M3',
        ('c', 'e#'): 'A3',
        ('c', 'fb'): 'd4',
        ('c', 'f'): 'P4',
        ('c', 'f#'): 'A4',
        ('c', 'gb'): 'd5',
        ('c', 'g'): 'P5',
        ('c', 'g#'): 'A5',
        ('c', 'abb'): 'd6',
        ('c', 'ab'): 'm6',
        ('c', 'a'): 'M6',
        ('c', 'a#'): 'A6',
        ('c', 'bbb'): 'd7',
        ('c', 'bb'): 'm7',
        ('c', 'b'): 'M7',
        ('c', 'b#'): 'A7',
        ('c', 'cb'): 'd8',

        ('c#', 'c#'): 'P1',
        ('c#', 'c##'): 'A1',
        ('c#', 'db'): 'd2',
        ('c#', 'd'): 'm2',
        ('c#', 'd#'): 'M2',
        ('c#', 'd##'): 'A2',
        ('c#', 'eb'): 'd3',
        ('c#', 'e'): 'm3',
        ('c#', 'e#'): 'M3',
        ('c#', 'e##'): 'A3',
        ('c#', 'f'): 'd4',
        ('c#', 'f#'): 'P4',
        ('c#', 'f##'): 'A4',
        ('c#', 'g'): 'd5',
        ('c#', 'g#'): 'P5',
        ('c#', 'g##'): 'A5',
        ('c#', 'ab'): 'd6',
        ('c#', 'a'): 'm6',
        ('c#', 'a#'): 'M6',
        ('c#', 'a##'): 'A6',
        ('c#', 'bb'): 'd7',
        ('c#', 'b'): 'm7',
        ('c#', 'b#'): 'M7',
        ('c#', 'b##'): 'A7',
        ('c#', 'c'): 'd8',

        ('c##', 'c##'): 'P1',

        ('dbb', 'dbb'): 'P1',

        ('db', 'db'): 'P1',

        ('d', 'd'): 'P1',
        ('d', 'e'): 'M2',
        ('d', 'f'): 'm3',
        ('d', 'g'): 'P4',
        ('d', 'a'): 'P5',
        ('d', 'b'): 'M6',
        ('d', 'c'): 'm7',

        ('d#', 'd#'): 'P1',

        ('d##', 'd##'): 'P1',

        ('ebb', 'ebb'): 'P1',

        ('eb', 'eb'): 'P1',

        ('e', 'e'): 'P1',
        ('e', 'f'): 'm2',
        ('e', 'g'): 'm3',
        ('e', 'a'): 'P4',
        ('e', 'b'): 'P5',
        ('e', 'c'): 'm6',
        ('e', 'd'): 'm7',

        ('e#', 'e#'): 'P1',

        ('e##', 'e##'): 'P1',

        ('fb', 'fb'): 'P1',

        ('f', 'f'): 'P1',
        ('f', 'g'): 'M2',
        ('f', 'a'): 'M3',
        ('f', 'b'): 'A4',
        ('f', 'c'): 'P5',
        ('f', 'd'): 'M6',
        ('f', 'e'): 'M7',

        ('f#', 'f#'): 'P1',

        ('f##', 'f##'): 'P1',

        ('gb', 'gb'): 'P1',

        ('g', 'g'): 'P1',
        ('g', 'a'): 'M2',
        ('g', 'b'): 'M3',
        ('g', 'c'): 'P4',
        ('g', 'd'): 'P5',
        ('g', 'e'): 'M6',
        ('g', 'f'): 'm7',

        ('g#', 'g#'): 'P1',

        ('g##', 'g##'): 'P1',

        ('abb', 'abb'): 'P1',
        ('abb', 'c'): 'A3',

        ('ab', 'ab'): 'P1',
        ('ab', 'c'): 'M3',
        ('ab', 'c#'): 'A3',

        ('a', 'a'): 'P1',
        ('a', 'b'): 'M2',
        ('a', 'c'): 'm3',
        ('a', 'c#'): 'M3',
        ('a', 'd'): 'P4',
        ('a', 'e'): 'P5',
        ('a', 'f'): 'm6',
        ('a', 'g'): 'm7',

        ('a#', 'a#'): 'P1',
        ('a#', 'c'): 'd3',
        ('a#', 'c#'): 'm3',

        ('a##', 'a##'): 'P1',
        ('a##', 'c#'): 'd3',

        ('bbb', 'bbb'): 'P1',
        ('bbb', 'c'): 'A2',

        ('bb', 'bb'): 'P1',
        ('bb', 'c'): 'M2',
        ('bb', 'c#'): 'A2',

        ('b', 'b'): 'P1',
        ('b', 'c'): 'm2',
        ('b', 'c#'): 'M2',
        ('b', 'd'): 'm3',
        ('b', 'e'): 'P4',
        ('b', 'f'): 'd5',
        ('b', 'g'): 'm6',
        ('b', 'a'): 'm7',

        ('b#', 'b#'): 'P1',
        ('b#', 'c'): 'd2',
        ('b#', 'c#'): 'm2',

        ('b##', 'b##'): 'P1',
        ('b##', 'c#'): 'd2',

    }[pair]

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
    notes = sorted(notes) # rest of code assumes lexigraphic order
    pairs = combinations(notes)

    # Define what we "mean" when we say [interval type] between two
    # notes. I'll call this the "semantics" of the note group
    _semantics = {
        'P1': 1, # unison
        'A1': 25/24, # augmented unison
        'd2': 128/125, # dimished second
        'm2': 16/15, # minor second
        'M2': 9/8, # major second
        'A2': 75/64, # augmented second
        'd3': 144/125, # dimished third
        'm3': 6/5, # minor third
        'M3': 5/4, # major third
        'A3': 125/96, # Augmented third
        'd4': 32/25, # dimished fourth
        'P4': 4/3, # perfect fourth
        'A4': 45/32, # augmented fourth
        'd5': 25/18, # dimished fifth
        'P5': 3/2, # perfect fifth
        'A5': 25/16, # augmented fifth
        'm6': 8/5, # minor sixth
        'M6': 5/3, # major sixth
        'm7': 16/9, # minor seventh
        'M7': 15/8, # major seventh
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
