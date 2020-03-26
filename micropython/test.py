import ntptime
ntptime.settime()

import days_forward
days_forward.daysForward(10000)

import three_days_forward
three_days_forward.threeDaysForward()

import three_days_forward_raid
three_days_forward_raid.threeDaysForwardAndRaid()

import get_eggs
get_eggs.getEggs()

import hatching_eggs
hatching_eggs.hatchingEggs(delay=3,initCol=0,maxBox=0,maxCol=5,eggCycle=20,flamebody=True)

import machine
machine.reset()
