import color_sensor
from hub import port
import time
import runloop

# --- CONFIG ---
color_sensor_up = port.C    # Oberer Sensor definieren
color_sensor_down = port.A  # Untere Sensor definieren
use_top = False             # Sollte der Obere sensor Benutzt werden?
update_intervall = 0.1      # Wie oft sollte der Satus der Sensoren Geprüft werden?
# --- END ---

down_active_time = 0
up_active_time = 0

was_down_active = False
was_up_active = False

def main():
    global down_active_time, up_active_time
    global was_down_active, was_up_active

    while True:
        down_reflection = color_sensor.reflection(color_sensor_down)
        up_reflection = color_sensor.reflection(color_sensor_up)

        down_active = down_reflection <= 10
        up_active = up_reflection <= 10

        output = []


        # --- DOWN SENSOR ---
        if down_active:
            down_active_time += update_intervall
        elif was_down_active:
            # Wechsel von aktiv zu inaktiv erkannt
            output.append("Down active for " + str(down_active_time) + "s")
            down_active_time = 0.0
        was_down_active = down_active

        # --- UP SENSOR ---
        if use_top == True:
            if up_active:
                up_active_time += update_intervall
            elif was_up_active:
                # Wechsel von aktiv zu inaktiv erkannt
                output.append("Up active for " + str(up_active_time) + "s")
                up_active_time = 0.0
            was_up_active = up_active

        if output:
            print(" | ".join(output))

        time.sleep(update_intervall)

# Start
runloop.run(main())
