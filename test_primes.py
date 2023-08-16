# coding:utf-8

import unittest
from itertools import islice
from array import array
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

  def test_sieve(self):
    """default sieve"""
    p = Prime()
    self.assertEqual(1223, p.table[-1])
    self.assertEqual(1229, next(p.sieve))

  def test_sieve1(self):
    """remove multiples of 2"""
    p = Prime(1)
    self.assertEqual(self.c[:1], list(p.table))
    self.assertEqual(self.c[1:4], list(islice(p.sieve,3)))
    self.assertEqual(3**2, next(p.sieve))

  def test_sieve2(self):
    """remove multiples of 2-3"""
    p = Prime(2)
    self.assertEqual(self.c[:2], list(p.table))
    self.assertEqual(self.c[2:9], list(islice(p.sieve,7)))
    self.assertEqual(5**2, next(p.sieve))

  def test_sieve3(self):
    """remove multiples of 2-3-5"""
    p = Prime(3)
    self.assertEqual(self.c[:3], list(p.table))
    self.assertEqual(self.c[3:15], list(islice(p.sieve,12)))
    self.assertEqual(7**2, next(p.sieve))

  def test_sieve4(self):
    """remove multiples of 2-3-5-7"""
    p = Prime(4)
    self.assertEqual(self.c[:4], list(p.table))
    self.assertEqual(self.c[4:30], list(islice(p.sieve,26)))
    self.assertEqual(11**2, next(p.sieve))

  def test_table1(self):
    """char array"""
    p = Prime(54, typecode='B')
    self.assertIsInstance(p.table, array)
    self.assertEqual(251, p.table[-1])
    self.assertEqual(257, next(p.sieve))

  def test_table2(self):
    """short array"""
    p = Prime(typecode='H')
    self.assertIsInstance(p.table, array)

  def test_table3(self):
    """long array"""
    p = Prime(typecode='L')
    self.assertIsInstance(p.table, array)

  def test_table4(self):
    """long long array"""
    p = Prime(typecode='Q')
    self.assertIsInstance(p.table, array)

  def test_table5(self):
    """bigint list"""
    p = Prime(typecode=None)
    self.assertIsInstance(p.table, list)

  def test_table_overflow1(self):
    """char table overflow"""
    with self.assertRaises(OverflowError) as ctx:
      p = Prime(55, typecode='B')

  def test_table_overflow2(self):
    """short table overflow"""
    with self.assertRaises(OverflowError) as ctx:
      p = Prime(6543, typecode='H')

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
