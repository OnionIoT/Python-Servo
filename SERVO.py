from onion import PWM


pwm = PWM.get_device()



servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096


def set_angle(servo, ang):

    if ang < 0:
        ang = 0
    elif ang > 180:
        ang = 180

    angle_range = 180
    servo_range = servo_max - servo_min


    value = float(ang) * float(servo_range) / float(angle_range)  + servo_min

    pwm.setPWM(servo, 0, value)
