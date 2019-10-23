'''Test all intervals based on D.'''

import unittest

from inplacetuning import inplacetuning

def _conds(rdes, ropt, rinit):
    return [
        abs(rdes0 - ropt0) <= abs(rdes0 - rinit0) for
        rdes0, ropt0, rinit0 in zip(rdes, ropt, rinit)]

class TestD(unittest.TestCase):
    '''Test all intervals based on D.'''

    def test_p1(self):
        '''[D, D]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'd'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_A1(self):
        '''[D, D#]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'd#'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))


    def test_d2(self):
        '''[D, Ebb]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'ebb'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_m2(self):
        '''[D, Eb]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'eb'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_M2(self):
        '''[D, E]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'e'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_A2(self):
        '''[D, E#]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'e#'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_d3(self):
        '''[D, Fb]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'fb'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_m3(self):
        '''[D, F]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'f'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_M3(self):
        '''[D, F#]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'f#'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_A3(self):
        '''[D, F##]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'f##'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_d4(self):
        '''[D, Gb]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'gb'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_P4(self):
        '''[D, G]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'g'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_A4(self):
        '''[D, G#]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'g#'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_d5(self):
        '''[D, Ab]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'ab'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_P5(self):
        '''[D, A]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'a'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_A5(self):
        '''[D, A#]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'a#'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_d6(self):
        '''[D, Bbb]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'bbb'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_m6(self):
        '''[D, Bb]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'bb'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_M6(self):
        '''[D, B]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'b'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_A6(self):
        '''[D, B#]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'b#'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_d7(self):
        '''[D, Cb]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'cb'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_m7(self):
        '''[D, C]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'c'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_M7(self):
        '''[D, C#]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'c#'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_A7(self):
        '''[D, C##]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'c##'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

    def test_d8(self):
        '''[D, Db]'''
        _fopt, _feq, ropt, rdes, rinit, _cost = inplacetuning(
            ['d', 'db'])
        self.assertTrue(all(_conds(rdes, ropt, rinit)))

if __name__ == '__main__':
    unittest.main()
