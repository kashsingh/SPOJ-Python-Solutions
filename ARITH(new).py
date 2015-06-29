#!/usr/bin/env python
# -*- encoding: UTF-8 -*-
from sys import stdin

op = ['+', '-', '*']
inputs = stdin.readlines()
for _ in xrange(int(inputs[0])):
    expr = inputs[_ + 1].strip()
    i = 0
    t = expr.find(op[i])
    while t == -1:
        i += 1
        t = expr.find(op[i])

    expr = expr[:t], expr[t:]
    if i == 0:  # addition
        res = str(int(expr[0]) + int(expr[1][1:]))
        field = max(len(expr[0]), len(expr[1]), len(res))
        print '{0:>{1}}'.format(expr[0], field)
        print '{0:>{1}}'.format(expr[1], field)
        print '{0:>{1}}'.format('-'*max(len(res), len(expr[1])), field)
        print '{0:>{1}}'.format(res, field)
    
    elif i == 1:  # subtraction
        res = str(int(expr[0]) - int(expr[1][1:]))
        field = max(len(expr[0]), len(expr[1]), len(res))
        print '{0:>{1}}'.format(expr[0], field)
        print '{0:>{1}}'.format(expr[1], field)
        print '{0:>{1}}'.format('-'*max(len(expr[1]), len(res)), field)
        print '{0:>{1}}'.format(res, field)
    
    else:  # multiplication
        a = int(expr[0])
        tmp = expr[1][1:]
        b = int(tmp)
        res = []
        for x in reversed(tmp):
            res.append(str(a*int(x)))
        finres = str(a * b)
        field = max(len(expr[0]), len(expr[1]), len(finres), len(res[-1]) + len(res) - 1)
        print '{0:>{1}}'.format(expr[0], field)
        print '{0:>{1}}'.format(expr[1], field)
        print '{0:>{1}}'.format('-'*max(len(res[0]), len(expr[1])), field)
        if len(res) != 1:
            for x in xrange(len(res)):
                print '{0:>{1}}{2:<{3}}'.format(res[x], field - x, ' ', x)
            print '{0:>{1}}'.format('-'*(max(len(res[-1]) + len(res) - 1, len(finres))), field)
        print '{0:>{1}}'.format(finres, field)