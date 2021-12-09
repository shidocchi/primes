# primes

## generate primes
```
>>> from primes import Prime
>>> from itertools import islice
>>> p = Prime()
>>> list(islice(p.generate(), 10))
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
>>> next(islice(p.generate(), 9999, None))
104729
```
```
>>> from primes import Prime
>>> p = Prime()
>>> list(p[:10])
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
>>> p[9999]
104729
```

## test primality
```
>>> from primes import Prime
>>> p = Prime()
>>> p.isprime(999999999989)
True
```
```
>>> from primes import Prime
>>> p = Prime()
>>> 99999999989 in p
True
```

## prime factorization
```
>>> from primes import Prime
>>> p = Prime()
>>> list(p.factorize(360))
[2, 2, 2, 3, 3, 5]
```

## recursive level of sieve
```
>>> import timeit
>>> from primes import Prime

>>> p = Prime(1)
>>> timeit.timeit('p.isprime(999999999989)', globals=globals(), number=1)
172.78589289999996

>>> p = Prime(10)
>>> timeit.timeit('p.isprime(999999999989)', globals=globals(), number=1)
44.14487299999996

>>> p = Prime(100)
>>> timeit.timeit('p.isprime(999999999989)', globals=globals(), number=1)
18.42776409999999

>>> p = Prime(200)
>>> timeit.timeit('p.isprime(999999999989)', globals=globals(), number=1)
12.965470800000048

>>> p = Prime(300)
>>> timeit.timeit('p.isprime(999999999989)', globals=globals(), number=1)
13.335162399999945

>>> p = Prime(1000)
>>> timeit.timeit('p.isprime(999999999989)', globals=globals(), number=1)
19.738375399999995
