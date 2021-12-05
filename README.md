# primes

## generate primes
```
>>> from primes import Prime
>>> p = Prime()
>>> it = p.generate()
>>> [next(it) for i in range(10)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```
```
>>> from primes import Prime
>>> from itertools import islice
>>> p = Prime()
>>> list(islice(p.generate(),10))
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

## test primality
```
>>> from primes import Prime
>>> p = Prime()
>>> p.isprime(999999999989)
True
```

## prime factorization
```
>>> from primes import Prime
>>> p = Prime()
>>> [x for x in p.factorize(360)]
[2, 2, 2, 3, 3, 5]
```
```
>>> from primes import Prime
>>> p = Prime()
>>> list(p.factorize(360))
[2, 2, 2, 3, 3, 5]
```
