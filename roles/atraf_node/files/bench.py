#!/usr/bin/env python

DEFAULT_DB = 'atraf'

import glob
import os
import random
import re
import sys
import subprocess

class Issue(Exception):
    def __init__(self, msg):
        self.msg = msg

def sayer(outfilename):
    if outfilename:
        outfile = open(outfilename, 'a')
    else:
        outfile = None

    def say(fmt, *args):
        line = fmt % args
        print line
        if outfile:
            print >>outfile, line
            outfile.flush()

    return say

def qq(s):
    if '"' in s or '\\' in s:
        raise("Oops")
    return '"' + s + '"'

def main(argv0, config=None, db=DEFAULT_DB):
    show_header = True
    seq = 0
    say = sayer(None)
    if config:
        outfilename = config + '.csv'
        say = sayer(outfilename)
        if os.path.exists(outfilename):
            contents = open(outfilename).readlines()
	    show_header = not contents
            if len(contents) > 1:
                last = contents[-1]
                seq = int(last.split(',')[1])
    else:
        config = 'adhoc'

    queries = glob.glob('sql/q??.sql')
    if not queries:
	raise Issue("No queries found")

    rnd = random.Random(0)

    if show_header:
        say("config,seqno,query,duration")
    while True:
        rnd.shuffle(queries)   # in-place, ew!
        for q in queries:
            seq += 1
            duration = run(db, q)
            name = os.path.splitext(os.path.basename(q))[0]
            say("%s,%d,%s,%f", qq(config), seq, qq(name), duration)

def run(db, queryfile):
    cmd = ['mclient', '-d', db, '-ims', queryfile]
    try:
        output = subprocess.check_output(cmd)
    except CalledProcessError, e:
        print >>sys.stderr, "Query %s triggered an exception:" % queryfile
        raise e

    
    pattern = re.compile(r'^[0-9]+ tuples? \(([0-9.]+)ms\)', re.M)
    m = pattern.search(output)
    if not m:
        max = 100
        snippet = output if len(output) <= max else "..." + output[-max:]
        raise Issue("Query %s failed: %r" % (queryfile, snippet))
    return float(m.group(1))



if __name__ == "__main__":
    try:
        sys.exit(main(*sys.argv))
    except Issue, e:
        print >>sys.stderr, "An error occurred:", e.msg
        sys.exit(1)
