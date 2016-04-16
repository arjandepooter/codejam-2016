#!/usr/bin/env python

def solve(w):
    result = w[0]

    for c in w[1:]:
        if ord(c) >= ord(result[0]):
            result = c + result
        else:
            result += c

    return result

if __name__ == '__main__':
    n = int(raw_input())

    for i in xrange(n):
        print "Case #%d: %s" % (i + 1, solve(raw_input()))
