import network
import socket
import machine
import uasyncio as asyncio
import utime


switch = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
beeper = machine.Pin(5, machine.Pin.OUT)

wlan = network.WLAN(network.AP_IF)
wlan.active(True)
wlan.ifconfig(("192.168.1.1", "255.255.255.0", "192.168.1.2", "8.8.8.8"))
wlan.config(essid="ESP")
wlan.active(True)

dist = 0


def getDist():
    try:
        s = socket.socket()
        s.connect(("192.168.1.50", 80))
        s.send("gimme ur data boi")
        rawdata = s.recv(64) #number of bytes to recieve. should only need like 4, but let's stay on the safe side

        stringdata = rawdata.decode("utf-8")

        return int(stringdata)
    except:
        print("o fuk")
        return 0


def getDelay(dist):
    wlan.active(True)
    # should return 100 at values < 50, should return 2000 at values > 300
    temp = 38 * dist
    temp = temp/5
    temp = temp - 280
    if temp < 0:
        temp = 0
    elif temp > 2000:
        temp = 2000
    return int(temp)


def isOn():
    if switch.value() == 1:
        return True
    else:
        return False

async def distLoop():
    global dist
    while True:
        dist = getDist()
        await asyncio.sleep(1)


async def beepyShit():
    global dist
    while True:
        print("hey, im beepin here")
        beeper.value(1)
        print("beepy boi on")
        await asyncio.sleep_ms(50)
        beeper.value(0)
        print("beepy boi of")
        print(dist)
        print(getDelay(dist))
        await asyncio.sleep_ms(getDelay(dist))


async def areWeThereYet():
    while True:
        if not isOn():
            print("switched off")
            return
        await asyncio.sleep(2)
        

def run():
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(distLoop())
        loop.create_task(beepyShit())
        loop.run_until_complete(areWeThereYet())
    finally:
        print("we done here")
        loop.close()



def main():
    while True:
        if isOn():
            print("!!! starting up")
            machine.freq(160000000)
            wlan.active(True)
            run()
        else:
            print("zzzzz")
            wlan.active(False)
            machine.freq(80000000)
            utime.sleep(2) #replace with esp8266 light sleep?


main()