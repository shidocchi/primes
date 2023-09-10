# primes

## generate primes
`generate()` returns an infinite iterator of prime numbers:
```
>>> from primes import Prime
>>> from itertools import islice
>>> p = Prime()
>>> list(islice(p.generate(), 10))
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
>>> next(islice(p.generate(), 9999, None))
104729
```
Prime object has indexing and slicing operator as pickup n-th prime number:
```
>>> from primes import Prime
>>> p = Prime()
>>> list(p[:10])
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
>>> p[9999]
104729
```

## test primality
`isprime(d)` does primality test:
```
>>> from primes import Prime
>>> p = Prime()
>>> p.isprime(999999999989)
True
```
Prime object has containment operator as primality test:
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
First argument of Prime() is initial number of primes prior to be called generate().
```
>>> from primes import Prime

>>> p = Prime(1)
>>> p.table
array('L', [2])

>>> p = Prime(2)
>>> p.table
array('L', [2, 3])

>>> p = Prime(3)
>>> p.table
array('L', [2, 3, 5])
```
It affects processing speed of generating.
```
>>> from timeit import Timer
>>> from primes import Prime

>>> p = Prime(1)
>>> Timer('999999999989 in p', globals=globals()).timeit(1)
6.5800526999999995

>>> p = Prime(10)
>>> Timer('999999999989 in p', globals=globals()).timeit(1)
5.1535572

>>> p = Prime(100)
>>> Timer('999999999989 in p', globals=globals()).timeit(1)
5.505758799999999

>>> p = Prime(110)
>>> Timer('999999999989 in p', globals=globals()).timeit(1)
4.2914393

>>> p = Prime(120)
>>> Timer('999999999989 in p', globals=globals()).timeit(1)
2.6435238000000005

>>> p = Prime(130)
>>> Timer('999999999989 in p', globals=globals()).timeit(1)
2.878485399999999

>>> p = Prime(140)
>>> Timer('999999999989 in p', globals=globals()).timeit(1)
2.599328

>>> p = Prime(150)
>>> Timer('999999999989 in p', globals=globals()).timeit(1)
2.6003222999999984

>>> p = Prime(160)
>>> Timer('999999999989 in p', globals=globals()).timeit(1)
3.058673800000001

>>> p = Prime(170)
>>> Timer('999999999989 in p', globals=globals()).timeit(1)
3.2432144999999934

>>> p = Prime(180)
>>> Timer('999999999989 in p', globals=globals()).timeit(1)
3.0593873999999985

>>> p = Prime(190)
>>> Timer('999999999989 in p', globals=globals()).timeit(1)
2.8756100000000018

>>> p = Prime(200)
>>> Timer('999999999989 in p', globals=globals()).timeit(1)
2.885937499999997

>>> p = Prime(1000)
>>> Timer('999999999989 in p', globals=globals()).timeit(1)
11.356283400000002
```
