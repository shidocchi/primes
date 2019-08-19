# primes

## generate primes

    >>> from primes import Prime
    >>> p = Prime()
    >>> it = p.generate()
    >>> [next(it) for i in range(10)]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

## test primality

    >>> from primes import Prime
    >>> p = Prime()
    >>> p.isprime(888888888887)
    True

