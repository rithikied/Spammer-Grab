#!/usr/bin/python

# - Spammer v3.0
# | Description: spams a phone number by sending it a lot of sms by using Grab API
# | Author: P4kL0nc4t
# | Date: 06/01/2018
# | Disclaimer: Editing author will not make you the real coder
# | What's New?
# | - Added coloring
# | - Added support multiple proxies (BETA)
# | - Added feature to create a new separate thread for each proxy in order to increase spam speed (BETA)
# | - Added support for phone number with +xxxxxx format 
# | - And another fixes

import spammer_decompile
spammer = spammer_decompile.Spammer()
spamer = spammer_decompile
spammer.author = "P4kL0nc4t"
try:
    spammer.main()
except KeyboardInterrupt:
    print(spamer.color.FAIL + spamer.color.REVERSE +\
          "\r[!][except] KeyboardInterrupt detected! Exiting . . ." \
          + spamer.color.ENDC)
    exit()