'''Test cases for simple triads.'''

import unittest

from inplacetuning import inplacetuning

def _conds(rdes, ropt, rinit):
    return [
        abs(rdes0 - ropt0) <= abs(rdes0 - rinit0) for
        rdes0, ropt0, rinit0 in zip(rdes, ropt, rinit)]

class TestTriads(unittest.TestCase):
    '''Test cases for simple triads.'''

    def test_cmajor(self):
        '''C major triad.'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'e', 'g'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_cmajor7(self):
        '''C major 7.'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'e', 'g', 'b'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_dminor(self):
        '''D minor triad.'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'f', 'a'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_dminor7(self):
        '''D minor 7.'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'f', 'a', 'c'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_eminor(self):
        '''E minor triad.'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['e', 'g', 'b'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_fmajor(self):
        '''F major triad.'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['f', 'a', 'c'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_gmajor(self):
        '''G major triad.'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['g', 'b', 'd'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_aminor(self):
        '''A minor triad.'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['a', 'c', 'e'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_bdiminished(self):
        '''B dimished triad.'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['b', 'd', 'f'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

if __name__ == '__main__':
    unittest.main()
