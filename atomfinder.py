#!/usr/bin/env python3.10

import sys
from functools import partial
# check if w can be constructed from atoms given in u
check = lambda u,w: any(map(lambda m: not w[len(m):] or check(u, w[len(m):]), set(map(lambda i: w[:i], range(1,1+len(w)))).intersection(u)))

def stats(u,ws):
    sw = tuple(filter(partial(check,u),ws))

    s = {
        "canbe" : sw,
        "cantbe": ws.difference(sw),
        "howmanycan": len(sw),
        "howmanycant": len(ws)-len(sw),
        "percentage": len(sw)/len(ws) * 100,
        "total": len(ws),
    }

    return s


def print_stats(s,f):
    print(f"Out of {s['total']} total words, {s['howmanycan']} could be constructed from atoms in the given universe. That's {s['percentage']} percent.")
    if f:
        print('\n'.join(s["canbe"]))


USAGE = f"""python {sys.argv[0]} <UNIVERSE FILE> <SEQ FILE> [PRINT MATCHES?]
UNIVERSE FILE must be a text file containing one atom per line.
SEQ FILE must be a text file containing one sequence to check per line.
PRINT MATCHES is a flag that defaults to false and can be set by passing a third argument
    It controls whether sequences that can be constructed are printed.

the output of this program is statistics about how many of SEQ can be
constructed from atoms in the given universe.
"""

if __name__ == "__main__":

    if len(sys.argv) <= 2:
        print(USAGE)
        sys.exit(1)

    with open(sys.argv[1]) as uf,open(sys.argv[2]) as sf:
        univ  = set(l.strip() for l in uf.readlines())
        words = set(l.strip() for l in sf.readlines())

    s = stats(univ, words)

    print_stats(s, len(sys.argv) >= 4)