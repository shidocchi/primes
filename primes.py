from itertools import count, islice

__version__ = '0.4.0'

class Prime:
  """class about prime numbers"""
  
  def __init__(self, level=300):
    self.level = level
    self.init_sieve()

  def init_sieve(self):
    """initial state of sieve"""
    self.table = [2]
    self.sieve = count(3, 2)
    for i in range(1, self.level):
      p = next(self.sieve)
      self.sieve = filter(p.__rmod__, self.sieve)
      self.table.append(p)

  def generate(self):
    """infinite generator of primes"""
    yield from self.table
    while True:
      p = next(self.sieve)
      if self._isprime(p, self.table[self.level:]):
        self.table.append(p)
        yield p

  def isprime(self, d):
    """test primality"""
    r = self.table[-1]
    if d <= r:
      return d in self.table
    elif d <= r * r:
      return self._isprime(d, self.table)
    else:
      return self._isprime(d, self.generate())

  def _isprime(self, d, gen):
    for r in gen:
      if r * r > d:
        break
      if d % r == 0:
        return False
    return True

  def factorize(self, d):
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

  def get(self, item):
    if isinstance(item, slice):
      return islice(self.generate(), item.start, item.stop)
    else:
      return next(islice(self.generate(), item, None))

  __contains__ = isprime
  __getitem__ = get


if __name__ == '__main__':
  p = Prime()
  print(p.isprime(999999999989))
