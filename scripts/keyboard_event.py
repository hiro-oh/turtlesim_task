#!/usr/bin/env python3.8

import keyboard, sys

def key_event(key):
    if key.name == 'q' and key.event_type == keyboard.KEY_DOWN:
        print("システムを終了します．")
        keyboard.unhook_all()

print("keyboard_event searching...")
keyboard.hook(key_event)

while True:
    pass