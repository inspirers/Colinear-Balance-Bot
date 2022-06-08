import time

import simple_navigator
import os
import neopixel
import board
from remote import RemoteController
from startup import find_controller

if "XDG_RUNTIME_DIR" not in os.environ:
    os.environ["XDG_RUNTIME_DIR"] = "/tmp/runtime-root"
"""
try:
    os.environ["DISPLAY"]
except:
    os.environ["SDL_VIDEODRIVER"] = "dummy"
"""

def main():
    find_controller()

    heartbeat_color = (255, 0, 255)
    heartbeat_state = True

    navigator = simple_navigator.ManualNavigator()
    
    while not navigator.get_button(1):
        time.sleep(0.1)

    try:
        while True:
            navigator.start()
            iter_count = 0
            max_iter_count = 1000
            while not navigator.fallen_over:
                navigator.main_task()

                if not iter_count % 32:
                    color = heartbeat_color if heartbeat_state else (255, 255, 255)
                    heartbeat_state = not heartbeat_state
                    navigator.update_constants()
                    navigator.print_telemetry()
                    if navigator.get_button(0):
                        break

                iter_count += 1
                iter_count = iter_count % max_iter_count
                time.sleep(0.001)

            navigator.stop()
            print("Manual halt or angle threshold reached, press x to enable motors")
            while not navigator.get_button(1):
                time.sleep(0.1)

    finally:
        navigator.stop()
        navigator.cleanup()
        for i in range(3):
            ()

if __name__ == '__main__':
    main()
