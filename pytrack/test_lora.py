#!/usr/bin/env python3
import time

from pytrack import LoRa

print("Create LoRa object")
mylora = LoRa(Channel=0, Frequency=915.0, Mode=1, DIO0=4)

while True:
    print("Send message")
    now = int(time.time())
    mylora.send_text(f"$$Mr. Watson, come here; I want you - {now}\n")

    while mylora.is_sending():
	    time.sleep(0.01)
    print("DONE")
    time.sleep(1)
