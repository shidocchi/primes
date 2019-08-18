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
    for r in self.generate():
      if d % r == 0:
        return False
      if r * r > d:
        return True

if __name__ == '__main__':
  p = Prime()
  print(p.isprime(888888888887))
