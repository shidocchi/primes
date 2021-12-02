__version__ = '0.2'

class Prime:
  """class about prime numbers"""
  
  def __init__(self, initial=None):
    self.table = initial or [2, 3, 5, 7, 11]

  def generate(self):
    """infinite generator of primes"""
    yield from self.table
    d = self.table[-1]
    assert d > 3
    while True:
      d += (d + 3) % 6
      if self._isprime(d, self.table[2:]):
        yield d
        self.table.append(d)

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

if __name__ == '__main__':
  p = Prime()
  print(p.isprime(888888888887))
