from hub import port
import distance_sensor
import time
import runloop

custom_port = port.B

async def main():
    while(True):
        await pixel_down(1, 100, 1)
        await pixel_up(1, 100, 1)

async def pixel_down(data, intensety=100, data_time=1):
    distance_sensor.set_pixel(custom_port, 1, 0, intensety)
    distance_sensor.set_pixel(custom_port, 1, 1, intensety)
    if data == 1:
        time.sleep(data_time)
    else:
        time.sleep(data_time / 2)
    
    distance_sensor.set_pixel(custom_port, 1, 0, 0)
    distance_sensor.set_pixel(custom_port, 1, 1, 1)

async def pixel_up(data, intensety=100, data_time=1):
    distance_sensor.set_pixel(custom_port, 0, 0, intensety)
    distance_sensor.set_pixel(custom_port, 0, 1, intensety)

    if data == 1:
        time.sleep(data_time)
    else:
        time.sleep(data_time / 2)

    distance_sensor.set_pixel(custom_port, 0, 0, 0)
    distance_sensor.set_pixel(custom_port, 0, 1, 1)

runloop.run(main())