'''Test all possible intervals.'''

import unittest

from inplacetuning import inplacetuning

def _conds(rdes, ropt, rinit):
    return [
        abs(rdes0 - ropt0) <= abs(rdes0 - rinit0) for
        rdes0, ropt0, rinit0 in zip(rdes, ropt, rinit)]

class TestAllIntervals(unittest.TestCase):
    '''Test all possible intervals.'''

    def setUp(self):
        '''Setup generic test.'''

        self.all_notes = [
            'a', 'a#', 'ab',
            'b', 'b#', 'bb',
            'c', 'c#', 'cb',
            'd', 'd#', 'db',
            'e', 'e#', 'eb',
            'f', 'f#', 'fb',
            'g', 'g#', 'gb',
        ]

        def _run_test(note):
            res = []
            for note0 in self.all_notes:
                _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
                    [note, note0])
                res.append(all(_conds(rdes, ropt, rinit)))
            return all(res)
        self.run_test = _run_test

    def test_run_notes(self):
        '''All intervals.'''

        for note in self.all_notes:
            self.assertTrue(self.run_test(note))

if __name__ == '__main__':
    unittest.main()
