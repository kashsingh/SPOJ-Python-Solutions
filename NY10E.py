from math import factorial


def main():
    for _ in xrange(int(raw_input())):
        s, n = map(int, raw_input().split())
        ans = 1
        for x in xrange(n + 9, n, -1):
            ans *= x
        ans //= factorial(9)
        print s, ans


main()