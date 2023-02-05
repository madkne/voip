#!/usr/bin/python3

import sys
import re
import time
import random

#import rpyc

from asterisk.agi import *

agi = AGI()
agi.verbose("python agi started", 0)
agi.answer()
aCallerId = agi.env['agi_callerid']
aType = agi.env["agi_type"]
agi.verbose("XXXXXXXXXXXXXX call from %s" % aCallerId)
agi.verbose(sys.executable)
#api.sayDigits(123)
#api.say_alpha('Hello')

#l = [aCallerId, aType]
#agi.verbose("XXXXXXXXXXXXXX l")
#api.exec_command("mpg123 /root/sound1.mp3")
agi.stream_file('sound1')

while True:
  agi.stream_file('vm-extension')
  result = agi.wait_for_digit(-1)  agi.verbose("got digit %s" % result)
  if result.isdigit():
    agi.say_number(result)
    break
#c = rpyc.connect("localhost", 18861)
#c.root.asteriskCall(l)

agi.verbose("python agi ended", 0)
