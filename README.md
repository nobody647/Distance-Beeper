# Distance-Beeper

This project has two parts (and two repos)
The other part is over at https://github.com/nobody647/Backup-distance-detector


This repo has stuff for an esp8266 that when turned on, creates an AP that another esp8266 connects to. It uses asyncio to poll a distance sensor at 192.168.1.50 as often as it can. It uses an active buzzer to make a beeping sound that becomes more frequent the closer something is to the distance sensor (ie: beep &nbsp;&nbsp;&nbsp;&nbsp; beep &nbsp;&nbsp;&nbsp;&nbsp; beep &nbsp;&nbsp; beep &nbsp; beepp beep BEEPBEEPBEEPBEEP)

I'm gonna mount these bad boys to my car so I have a sorta primative backup detector thingy
