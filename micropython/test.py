import ntptime
ntptime.settime()

import days_forward
days_forward.run(frames=32446,date=1,maxDate=30,)

import three_days_forward
three_days_forward.run(date=1,maxDate=30,isSecondary=True)

import three_days_forward_raid
three_days_forward_raid.run(date=1,maxDate=30,isSecondary=True)

import get_eggs
get_eggs.run(isSecondary=True)

import hatching_eggs
hatching_eggs.run(initCol=0,maxBox=0,maxCol=5,eggCycle=20,flamebody=True,isSecondary=True,delay=3)

import machine
machine.reset()
