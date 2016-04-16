#!/usr/bin/env python

from collections import defaultdict

def solve(sets):
    cnt = defaultdict(int)

    for s in sets:
        for n in s:
            cnt[n] += 1

    missing = [k for k, v in cnt.iteritems() if v % 2 == 1]
    missing.sort()
    return ' '.join(str(c) for c in missing)

if __name__ == '__main__':
    n = int(raw_input())

    for i in xrange(n):
        l = int(raw_input())
        sets = [tuple(int(c) for c in raw_input().split(" ")) for _ in xrange(2*l-1)]
        print "Case #%d: %s" % (i + 1, solve(sets))
