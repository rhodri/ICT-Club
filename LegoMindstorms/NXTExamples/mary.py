#!/usr/bin/env python
#
# Converted from mary.rb found in ruby_nxt package
# Plays "Mary Had A Little Lamb"
# Author: Christopher Continanza <christopher.continanza@villanova.edu>

from time import sleep
import nxt.locator

FREQ_C = 523
FREQ_D = 587
FREQ_E = 659
FREQ_G = 784

b = nxt.locator.find_one_brick(debug=True, name="ICTCLUB3")

b.play_tone_and_wait(FREQ_E, 500)
b.play_tone_and_wait(FREQ_C, 750)
