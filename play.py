#!/usr/bin/python

import sys
import re
import time
import random

import rpyc

from asterisk.agi import AGI

agi = AGI()
agi.verbose("python agi started")
aCallerId = agi.env['agi_callerid']
aType = agi.env["agi_type"]
agi.verbose("XXXXXXXXXXXXXX call from %s" % aCallerId)
agi.verbose(sys.executable)

l = [aCallerId, aType]
agi.verbose("XXXXXXXXXXXXXX l")

c = rpyc.connect("localhost", 18861)
c.root.asteriskCall(l)
