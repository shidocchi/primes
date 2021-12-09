# coding:utf-8

import unittest
from itertools import islice
from primes import Prime

class PrimesTest(unittest.TestCase):

  c = [
      2,  3,  5,  7, 11,
     13, 17, 19, 23, 29,
     31, 37, 41, 43, 47,
     53, 59, 61, 67, 71,
     73, 79, 83, 89, 97,
    101,103,107,109,113,
  ]

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_init1(self):
    """remove multiples of 2"""
    p = Prime(1)
    self.assertEqual(self.c[:1], p.table)
    self.assertEqual(self.c[1:4], list(islice(p.sieve,3)))
    self.assertEqual(9, next(p.sieve))

  def test_init2(self):
    """remove multiples of 2-3"""
    p = Prime(2)
    self.assertEqual(self.c[:2], p.table)
    self.assertEqual(self.c[2:9], list(islice(p.sieve,7)))
    self.assertEqual(25, next(p.sieve))

  def test_init3(self):
    """remove multiples of 2-3-5"""
    p = Prime(3)
    self.assertEqual(self.c[:3], p.table)
    self.assertEqual(self.c[3:15], list(islice(p.sieve,12)))
    self.assertEqual(49, next(p.sieve))

  def test_init4(self):
    """remove multiples of 2-3-5-7"""
    p = Prime(4)
    self.assertEqual(self.c[:4], p.table)
    self.assertEqual(self.c[4:30], list(islice(p.sieve,26)))
    self.assertEqual(121, next(p.sieve))

  def test_generate1(self):
    """prime generator 1"""
    p = Prime()
    self.assertEqual(self.c, list(p[:len(self.c)]))

  def test_generate2(self):
    """prime generator 2"""
    p = Prime()
    self.assertEqual(131071, p[12250])

  def test_isprime1(self):
    """primality test 1"""
    p = Prime()
    self.assertTrue(99999989 in p)

  def test_isprime2(self):
    """primality test 2"""
    p = Prime()
    self.assertTrue(999999999989 in p)

  def test_isprime3(self):
    """primality test 3"""
    p = Prime()
    self.assertTrue(99999989 in p)
    self.assertTrue(999999999989 in p)

  def test_isprime4(self):
    """primality test 4"""
    p = Prime()
    self.assertTrue(9999399973 not in p)

  def test_factorize1(self):
    """prime factorization 1"""
    p = Prime()
    self.assertEqual([2,2,3,3,5,5], list(p.factorize(900)))

  def test_factorize2(self):
    """prime factorization 2"""
    p = Prime()
    self.assertEqual([99991,100003], list(p.factorize(9999399973)))

if __name__ == "__main__":
    unittest.main()
