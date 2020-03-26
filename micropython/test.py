import ntptime
ntptime.settime()

import days_forward
days_forward.daysForward(32446)

import three_days_forward
three_days_forward.threeDaysForward(isSecondary=True)

import three_days_forward_raid
three_days_forward_raid.threeDaysForwardAndRaid(isSecondary=True)

import get_eggs
get_eggs.getEggs(isSecondary=True)

import hatching_eggs
hatching_eggs.hatchingEggs(initCol=0,maxBox=0,maxCol=5,eggCycle=20,flamebody=True,isSecondary=True,second=3)

import machine
machine.reset()
