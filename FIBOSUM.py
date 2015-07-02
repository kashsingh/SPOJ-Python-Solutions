#This is not my solution of the problem, it belongs to eightnoteight. He was able to solve the problem using Python.
# I am storing it to undersand hi approach to the problem as he has used a nice and fast algorithm here.
class fibwhip:
    def __init__(self):
        self.mat = (1, 1, 1, 0)
        self.cache = { 0: (1, 1, 1, 0), }
        self.cache_max = 0

    def fib(self, n):
        from math import log
        try:
            if n < 2:
                return n
            if n == 1 << int(log(n, 2)):
                return self.cache[int(log(n, 2))][1] % 1000000007
        except KeyError:
            pass
            
        cm = self.cache_max
        while int(log(n, 2)) > cm:
            a, b, c, d = self.cache[cm]
            self.cache[cm + 1] = (
                (a * a + b * b) % 1000000007,
                (b * (a + d)) % 1000000007,
                (b * (a + d)) % 1000000007,
                (b * b + d * d) % 1000000007
            )
            cm += 1
        self.cache_max = cm
        ans = self.cache[int(log(n, 2))]
        n -= 1 << int(log(n, 2))
        while n > 0:
            tmp = self.cache[int(log(n, 2))]
            ans = (
                (ans[0] * tmp[0] + ans[1] * tmp[2]) % 1000000007,
                (ans[0] * tmp[1] + ans[1] * tmp[3]) % 1000000007,
                (ans[2] * tmp[0] + ans[3] * tmp[2]) % 1000000007,
                (ans[2] * tmp[1] + ans[3] * tmp[3]) % 1000000007,
            )
            n -= 1 << int(log(n, 2))
        assert ans[1] == ans[2]
        return ans[1] % 1000000007


fibs = fibwhip()
for _ in xrange(int(raw_input())):
    n, m = map(int, raw_input().split())
    print (fibs.fib(m + 2) - fibs.fib(n + 1)) % 1000000007