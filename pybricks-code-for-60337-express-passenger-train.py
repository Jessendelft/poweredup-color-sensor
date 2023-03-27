from pybricks.pupdevices import ColorDistanceSensor, DCMotor # ColorSensor instead of ColorDistanceSensor if using Mindstorms sensor
from pybricks.parameters import Color, Port
from pybricks.tools import wait

motor = DCMotor(Port.A)
sensor = ColorDistanceSensor(Port.B) # ColorSensor instead of ColorDistanceSensor if using Mindstorms sensor

station_stop_time_ms = 2500
eol_stop_time_ms = 5000
forward_speed = 20
check_color_interval_ms = 20
forward_direction = True

def do_on_red():
    print("red detected, at end of line, stopping and going back to station")
    motor.brake()
    wait(eol_stop_time_ms)
    forward_direction = False
    
def do_on_yellow():
    print("yellow detected, at end of line, stopping and going back to station")
    motor.brake()
    wait(eol_stop_time_ms)
    forward_direction = True

def do_on_green():
    print("green detected, at station, stopping and continuing")
    motor.brake()
    wait(station_stop_time_ms)

while True:
    if sensor.color() = Color.GREEN:
        do_on_green()
    elif sensor.color() = Color.YELLOW:
        do_on_yellow()
    elif sensor.color() = Color.RED:
        do_on_red()
    else:
        if forward_direction:
            motor.dc(forward_speed)
        else:
            motor.dc(-forward_speed)
    wait(check_color_interval_ms)

