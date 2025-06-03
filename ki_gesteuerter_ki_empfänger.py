import color_sensor
from hub import port
import time
import runloop

color_sensor_up = port.A
color_sensor_down = port.C


async def main():
    while True:
        down = color_sensor.reflection(color_sensor_down)
        up = color_sensor.reflection(color_sensor_up)

        print("Down: " + str(down) + " | Up: " + str(up))
        time.sleep(0.5)


runloop.run(main())
