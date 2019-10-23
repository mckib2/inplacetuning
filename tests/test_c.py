'''Test all intervals based on C.'''

import unittest

from inplacetuning import inplacetuning

def _conds(rdes, ropt, rinit):
    return [
        abs(rdes0 - ropt0) <= abs(rdes0 - rinit0) for
        rdes0, ropt0, rinit0 in zip(rdes, ropt, rinit)]

class TestC(unittest.TestCase):
    '''Test all intervals based on C.'''

    def test_p1(self):
        '''[C, C]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'c'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_d2(self):
        '''[C, Dbb]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'dbb'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_m2(self):
        '''[C, Db]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'db'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_M2(self):
        '''[C, D]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'd'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_A2(self):
        '''[C, D#]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'd#'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_d3(self):
        '''[C, Ebb]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'ebb'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_m3(self):
        '''[C, Eb]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'eb'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_M3(self):
        '''[C, E]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'e'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_A3(self):
        '''[C, E#]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'e#'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_d4(self):
        '''[C, Fb]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'fb'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_P4(self):
        '''[C, F]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'f'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_A4(self):
        '''[C, F#]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'f#'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_d5(self):
        '''[C, Gb]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'gb'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_P5(self):
        '''[C, G]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'g'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_A5(self):
        '''[C, G#]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'g#'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_d6(self):
        '''[C, Abb]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'abb'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_m6(self):
        '''[C, Ab]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'ab'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_M6(self):
        '''[C, A]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'a'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_A6(self):
        '''[C, A#]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'a#'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_d7(self):
        '''[C, Bbb]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'bbb'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_m7(self):
        '''[C, Bb]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'bb'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_M7(self):
        '''[C, B]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'b'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_A7(self):
        '''[C, B#]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'b#'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_d8(self):
        '''[C, Cb]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'cb'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_A8(self):
        '''[C, C#]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['c', 'c#'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

if __name__ == '__main__':
    unittest.main()
