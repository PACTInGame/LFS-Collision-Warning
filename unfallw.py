import pyinsim
import math
import pyautogui
import winsound

insim = pyinsim.insim('127.0.0.1', 29999, Admin='', Flags=pyinsim.ISF_MCI | pyinsim.ISF_LOCAL, Interval=20)


def car_info(insim, MCI):

    h = MCI.Info[0]

    y_kord_car_one = h.Y
    Speed_Auto_eins = h.Speed/91.02
    x_kord_car_one = h.X
    Heading_Auto_eins = h.Heading
    z_kord_car_one = h.Z

    j = MCI.Info[1]

    y_kord_car_two = j.Y
    Speed_Auto_zwei = j.Speed/91.02
    x_kord_car_two = j.X
    Heading_Auto_zwei = j.Heading
    z_kord_car_two = h.Z

    ang = (math.atan2((x_kord_car_two / 65536 - x_kord_car_one / 65536), (y_kord_car_two / 65536 - y_kord_car_one / 65536)) * 180.0) / 3.1415926535897931
    if ang < 0.0:

        ang = 360.0 + ang


    dir = ang + Heading_Auto_eins / 182
    if (dir > 360.0):

                dir -= 360.0

    y = round(dir, 0)

    a = (x_kord_car_one/65536, y_kord_car_one/65536, 0)
    b = (x_kord_car_two/65536, y_kord_car_two/65536, 0)

    dist = math.sqrt((b[0] - a[0]) * (b[0] - a[0]) + (b[1] - a[1]) * (b[1] - a[1]) + (b[2] - a[2]) * (b[2] - a[2]))


    rel_speed = Speed_Auto_eins - Speed_Auto_zwei

    print "rel speed:", rel_speed
    print "ang", y
    print "dist", dist
    if Speed_Auto_eins <= 50 and Speed_Auto_eins > 8:

        if rel_speed > 5 and dist < 6:
                if y > 352 or y < 8:
                        pyautogui.mouseDown(button="right")
                        insim.send(pyinsim.ISP_MST,
                           Msg="/press 9")


        elif rel_speed > 10 and rel_speed <= 20 and dist < 7:
               if y > 352 or y < 8:
                        pyautogui.mouseDown(button="right")
                        insim.send(pyinsim.ISP_MST,
                          Msg="/press 9")

        elif rel_speed > 20 and rel_speed <= 30 and dist < 8:
               if y > 352 or y < 8:
                        pyautogui.mouseDown(button="right")
                        insim.send(pyinsim.ISP_MST,
                          Msg="/press 9")

        elif rel_speed > 30 and rel_speed <= 40 and dist < 12:
            if y > 352 or y < 8:
                pyautogui.mouseDown(button="right")
                insim.send(pyinsim.ISP_MST,
                           Msg="/press 9")

        elif rel_speed > 40 and rel_speed <= 50 and dist < 15 :
            if y > 352 or y < 8:
                pyautogui.mouseDown(button="right")
                insim.send(pyinsim.ISP_MST,
                           Msg="/press 9")






    elif Speed_Auto_eins > 50 and Speed_Auto_eins <=70:

        if rel_speed > 5 and dist < 6:
                if y > 352 or y < 8:
                        pyautogui.mouseDown(button="right")
                        insim.send(pyinsim.ISP_MST,
                           Msg="/press 9")


        elif rel_speed > 10 and rel_speed <= 20 and dist < 8:
               if y > 352 or y < 8:
                        pyautogui.mouseDown(button="right")
                        insim.send(pyinsim.ISP_MST,
                                   Msg="/press 9")


        elif rel_speed > 20 and rel_speed <= 30 and dist < 9:
               if y > 352 or y < 8:
                        pyautogui.mouseDown(button="right")
                        insim.send(pyinsim.ISP_MST,
                                   Msg="/press 9")


        elif rel_speed > 30 and rel_speed <= 40 and dist < 14:
            if y > 352 or y < 8:
                pyautogui.mouseDown(button="right")
                insim.send(pyinsim.ISP_MST,
                           Msg="/press 9")


        elif rel_speed > 40 and rel_speed <= 50 and dist < 17:
                if y > 352 or y < 8:
                        pyautogui.mouseDown(button="right")
                        insim.send(pyinsim.ISP_MST,
                                   Msg="/press 9")


        elif rel_speed > 50 and rel_speed <= 60 and dist < 20:
                if y > 352 or y < 8:
                        pyautogui.mouseDown(button="right")
                        insim.send(pyinsim.ISP_MST,
                                   Msg="/press 9")

        elif rel_speed > 60 and rel_speed <= 70 and dist < 23:
                if y > 352 or y < 8:
                        pyautogui.mouseDown(button="right")
                        insim.send(pyinsim.ISP_MST,
                                   Msg="/press 9")





    elif Speed_Auto_eins > 70 and Speed_Auto_eins <= 90:
        if rel_speed > 5 and dist < 6:
                if y > 352 or y < 8:
                        pyautogui.mouseDown(button="right")
                        insim.send(pyinsim.ISP_MST,
                           Msg="/press 9")


        elif rel_speed > 10 and rel_speed <= 20 and dist < 8:
               if y > 352 or y < 8:
                        pyautogui.mouseDown(button="right")
                        insim.send(pyinsim.ISP_MST,
                                   Msg="/press 9")


        elif rel_speed > 20 and rel_speed <= 30 and dist < 9:
               if y > 352 or y < 8:
                        pyautogui.mouseDown(button="right")
                        insim.send(pyinsim.ISP_MST,
                                   Msg="/press 9")


        elif rel_speed > 30 and rel_speed <= 40 and dist < 14:
            if y > 352 or y < 8:
                pyautogui.mouseDown(button="right")
                insim.send(pyinsim.ISP_MST,
                           Msg="/press 9")


        elif rel_speed > 40 and rel_speed <= 50 and dist < 17:
                if y > 352 or y < 8:
                        pyautogui.mouseDown(button="right")
                        insim.send(pyinsim.ISP_MST,
                                   Msg="/press 9")


        elif rel_speed > 50 and rel_speed <= 60 and dist < 21:
                if y > 352 or y < 8:
                        pyautogui.mouseDown(button="right")
                        insim.send(pyinsim.ISP_MST,
                                   Msg="/press 9")

        elif rel_speed > 60 and rel_speed <= 70 and dist < 24:
                if y > 352 or y < 8:
                        pyautogui.mouseDown(button="right")
                        insim.send(pyinsim.ISP_MST,
                                   Msg="/press 9")
        elif rel_speed > 70 and rel_speed <= 80 and dist < 27:
                if y > 352 or y < 8:
                        pyautogui.mouseDown(button="right")
                        insim.send(pyinsim.ISP_MST,
                                   Msg="/press 9")
        elif rel_speed > 80 and rel_speed <= 90 and dist < 32:
                if y > 352 or y < 8:
                        pyautogui.mouseDown(button="right")
                        insim.send(pyinsim.ISP_MST,
                                   Msg="/press 9")

    elif Speed_Auto_eins > 90 and Speed_Auto_eins <= 100:
        if rel_speed > 5 and dist < 6:
            if y > 352 or y < 8:
                pyautogui.mouseDown(button="right")
                insim.send(pyinsim.ISP_MST,
                           Msg="/press 9")


        elif rel_speed > 10 and rel_speed <= 20 and dist < 9:
            if y > 352 or y < 8:
                pyautogui.mouseDown(button="right")
                insim.send(pyinsim.ISP_MST,
                           Msg="/press 9")


        elif rel_speed > 20 and rel_speed <= 30 and dist < 10:
            if y > 352 or y < 8:
                pyautogui.mouseDown(button="right")
                insim.send(pyinsim.ISP_MST,
                           Msg="/press 9")


        elif rel_speed > 30 and rel_speed <= 40 and dist < 17:
            if y > 352 or y < 8:
                pyautogui.mouseDown(button="right")
                insim.send(pyinsim.ISP_MST,
                           Msg="/press 9")


        elif rel_speed > 40 and rel_speed <= 50 and dist < 21:
            if y > 352 or y < 8:
                pyautogui.mouseDown(button="right")
                insim.send(pyinsim.ISP_MST,
                           Msg="/press 9")


        elif rel_speed > 50 and rel_speed <= 60 and dist < 24:
            if y > 352 or y < 8:
                pyautogui.mouseDown(button="right")
                insim.send(pyinsim.ISP_MST,
                           Msg="/press 9")

        elif rel_speed > 60 and rel_speed <= 70 and dist < 26:
            if y > 352 or y < 8:
                pyautogui.mouseDown(button="right")
                insim.send(pyinsim.ISP_MST,
                           Msg="/press 9")
        elif rel_speed > 70 and rel_speed <= 80 and dist < 31:
            if y > 352 or y < 8:
                pyautogui.mouseDown(button="right")
                insim.send(pyinsim.ISP_MST,
                           Msg="/press 9")
        elif rel_speed > 80 and rel_speed <= 90 and dist < 35:
            if y > 352 or y < 8:
                pyautogui.mouseDown(button="right")
                insim.send(pyinsim.ISP_MST,
                           Msg="/press 9")
        elif rel_speed > 90 and rel_speed <= 100 and dist < 38:
            if y > 352 or y < 8:
                pyautogui.mouseDown(button="right")
                insim.send(pyinsim.ISP_MST,
                           Msg="/press 9")










    elif Speed_Auto_eins > 100 and Speed_Auto_eins <= 120:
        if rel_speed > 5 and dist < 6:
                if y > 352 or y < 8:
                        pyautogui.mouseDown(button="right")
                        insim.send(pyinsim.ISP_MST,
                           Msg="/press 9")


        elif rel_speed > 10 and rel_speed <= 20 and dist < 12:
               if y > 352 or y < 8:
                        pyautogui.mouseDown(button="right")
                        insim.send(pyinsim.ISP_MST,
                                   Msg="/press 9")


        elif rel_speed > 20 and rel_speed <= 30 and dist < 17:
               if y > 352 or y < 8:
                        pyautogui.mouseDown(button="right")
                        insim.send(pyinsim.ISP_MST,
                                   Msg="/press 9")


        elif rel_speed > 30 and rel_speed <= 40 and dist < 25:
            if y > 352 or y < 8:
                pyautogui.mouseDown(button="right")
                insim.send(pyinsim.ISP_MST,
                           Msg="/press 9")


        elif rel_speed > 40 and rel_speed <= 50 and dist < 32:
                if y > 352 or y < 8:
                        pyautogui.mouseDown(button="right")
                        insim.send(pyinsim.ISP_MST,
                                   Msg="/press 9")


        elif rel_speed > 50 and rel_speed <= 60 and dist < 35:
                if y > 352 or y < 8:
                        pyautogui.mouseDown(button="right")
                        insim.send(pyinsim.ISP_MST,
                                   Msg="/press 9")

        elif rel_speed > 60 and rel_speed <= 70 and dist < 37:
                if y > 352 or y < 8:
                        pyautogui.mouseDown(button="right")
                        insim.send(pyinsim.ISP_MST,
                                   Msg="/press 9")
                    
        elif rel_speed > 70 and rel_speed <= 80 and dist < 44:
                if y > 352 or y < 8:
                        pyautogui.mouseDown(button="right")
                        insim.send(pyinsim.ISP_MST,
                                   Msg="/press 9")
                    
        elif rel_speed > 80 and rel_speed <= 90 and dist < 45:
                if y > 352 or y < 8:
                        pyautogui.mouseDown(button="right")
                        insim.send(pyinsim.ISP_MST,
                                   Msg="/press 9")

        elif rel_speed > 90 and rel_speed <= 120 and dist < 50:
                if y > 352 or y < 8:
                        pyautogui.mouseDown(button="right")
                        insim.send(pyinsim.ISP_MST,
                                   Msg="/press 9")


insim.bind(pyinsim.ISP_MCI, car_info)


pyinsim.run()
