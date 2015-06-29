""" It is based on the fact that:
    ***The number of odd entries in row N of Pascal's Triangle is 2 raised to the number of 1's in the binary expansion of N.
    where series { nC0, nC1,... nCn } is the Pascal's Triangle."""
for _ in xrange(int(raw_input())):
    n = int(raw_input())
    odds = 1 << bin(n).count('1') #It raises the no of 1's in N to the power of 2.
    print '{0} {1}'.format(n + 1 - odds, odds)