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
      if self.isprime(d):
        yield d
        self.table.append(d)

  def isprime(self, d):
    """test primality"""
    r = self.table[-1]
    if d <= r:
      return d in self.table
    elif d <= r * r:
      g = self.table
    else:
      g = self.generate()
    for r in g:
      if d % r == 0:
        return False
      if r * r > d:
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
