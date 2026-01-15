import argparse
import code
from itertools import count, islice
from array import array
from collections.abc import Iterator
from typing import Literal, Optional, Union

__version__ = '0.5.0'

TypeCode = Optional[Literal['H', 'L', 'Q']]
Table = Union[array, list[int]]
Sieve = Union[count, filter]
Gen = Union[array, list[int], Iterator[int]]
Index = Union[slice, int]
Item = Union[Iterator[int], int]

class Prime:
  """class about prime numbers"""
  
  def __init__(self, level:int=200, typecode:TypeCode='L') -> None:
    self.level: int = level
    self.typecode: TypeCode = typecode
    self.table: Table
    self.sieve: Sieve
    self.init_sieve()

  def init_sieve(self) -> None:
    """initial state of sieve"""
    self.table = [2]
    if self.typecode:
      self.table = array(self.typecode, self.table)
    self.sieve = count(3, 2)
    for i in range(1, self.level):
      p = next(self.sieve)
      self.sieve = filter(p.__rmod__, self.sieve)
      self.table.append(p)

  def generate(self) -> Iterator[int]:
    """infinite generator of primes"""
    yield from self.table
    while True:
      p = next(self.sieve)
      if self._isprime(p, self.table[self.level:]):
        self.table.append(p)
        yield p

  def isprime(self, d:int) -> bool:
    """test primality"""
    r = self.table[-1]
    if d <= r:
      return d in self.table
    elif d <= r * r:
      return self._isprime(d, self.table)
    else:
      return self._isprime(d, self.generate())

  def _isprime(self, d:int, gen:Gen) -> bool:
    for r in gen:
      if r * r > d:
        break
      if d % r == 0:
        return False
    return True

  def factorize(self, d:int) -> Iterator[int]:
    """prime factorization"""
    for r in self.generate():
      if r * r > d:
        yield d
        break
      while True:
        q, m = divmod(d, r)
        if m != 0:
          break
        yield r
        d = q
      if d == 1:
        break

  def get(self, idx:Index) -> Item:
    if isinstance(idx, slice):
      return islice(self.generate(), idx.start, idx.stop, idx.step)
    else:
      return next(islice(self.generate(), idx, None))

  __contains__ = isprime
  __getitem__ = get

def get_parser():
  """argument parser"""
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', '--interact', action='store_true',
                      help='interaction assigned p as primes object')
  parser.add_argument('-n', '--number', type=int,
                      help='number of primes: p[n]')
  parser.add_argument('-p', '--isprime', type=int,
                      help='check primality: n in p')
  parser.add_argument('-f', '--factor', type=int,
                      help='factorize')
  parser.add_argument('-t', '--type', choices=tuple('HLQ'),
                      help='array type')
  return parser

if __name__ == '__main__':
  parser = get_parser()
  args = parser.parse_args()
  p = Prime(typecode=args.type)
  if args.interact:
    code.interact(banner='', local={'p':p})
  elif args.number is not None:
    print('p[{}] : {}'
          .format(args.number, p[args.number]))
  elif args.isprime is not None:
    print('{} in p : {}'
          .format(args.isprime, args.isprime in p))
  elif args.factor is not None:
    print('p.factorize({}) : {}'
          .format(args.factor, list(p.factorize(args.factor))))
  else:
    parser.print_help()
