#Python version 3.3.2

import random
import math
import time
from tkinter import tix
# import tkinter
from turtle import *

## setturtles(3)

screensize(1000,680)
mode("logo")
colormode(255)
bgcolor("sky blue")

kills = 0



def bull():
    global y
    pensize(3)
    color("black", "black")
    y = random.randint(-270, 270)
    ht()
    pu()
    goto(280, y)
    pd()
    begin_fill()
    circle(20)
    end_fill()
    color("red", "red")
    pu()
    goto(280,y+10)
    begin_fill()
    circle(10)
    end_fill()

   


## hide declarations
    
pensize(15)
color("sky blue")

#declare barrel

begin_poly()
pensize(15)
fd(150)
end_poly()
   
barrel = get_poly()
register_shape("gun", barrel)
addshape("gun", barrel)

## declare target killer

begin_poly()
begin_fill()
rt(90)
fd(5)
lt(120)
fd(10)
lt(120)
fd(10)
lt(120)
fd(5)
end_fill()
end_poly()

projectile = get_poly()
addshape("death", projectile)


## repeat game here

while(True):
    
    # tracer(45)
    bgcolor("sky blue")

    color("black")
    bull()

    pu()
    goto(-500, -340)
    color("olive drab")
    color("olive drab", "olive drab")
    pd()
    begin_fill()
    goto (-420, -273)
    goto (-280, -273)
    goto (-200, -340)
    goto (-400, -340)
    end_fill()
    pu()
    ht()

    gun = Turtle()
    gun.color("olive drab")
    gun.pu()
    gun.ht()

    gun.goto(-280, -280)
    gun.pd()
    gun.seth(90)
    gun.st()

    gun.shape("gun")
    gun.shapesize(1, 1, 15)
    
    death = Turtle()
    death.color("blue")
    death.ht()

    time.sleep(1)

    ## turtlesize(30)

    gunpos = 90

    ## start loop

    while(True):

        class label(Exception): pass
            
        
        # aim = int(input("Choose an angle: "))
        aim = -1
        aim = int(numinput("Aim the gun", "Choose an angle: ", 45 , minval=0, maxval=90))

##        if aim == -1:
##            quit = textinput("Are you sure?", "Are you sure you want to quit? (y/n)")
##            if quit == "Y" or quit == "y":
##                break
##            else: 
##                raise label()
##                pass
            
        z = math.tan(math.radians(90-aim))
    ##    aimhi = math.tan((y+320)/560)
    ##    aimlo = math.tan((y+280)/560)
        aimhi = (y+330)/560  ## was 320
        aimlo = (y+270)/560  ## was 280
        lof = int(math.sqrt(math.pow((y+280), 2) + (math.pow(560, 2))))

        ## move barrel
        
        gun.pd()
        gun.seth(gunpos)
        gun.color("olive drab")
        gun.shape("gun")
        gun.shapesize(1, 1, 15)
    ##    gun.ht()
        gun.st()

        if (aim < gunpos):
            
            for upw in range(gunpos, aim, -1):
                gun.lt(1)            
                gun.shape("gun")
                gun.shapesize(1, 1, 15)            
        else:
            for dnw in range(gunpos, aim, 1):
                gun.rt(1)
                #gun = Turtle()
                gun.shape("gun")
                gun.shapesize(1, 1, 15)
        gunpos = aim


    ##    death = Turtle()
        death.pu()
        death.goto(-280, -280)
        death.seth(gunpos)
        #death.fd(150)
        #death.pd()
        
        #fire bullet
        for flight in range (0, lof-150, 5):
            #death = Turtle()
            death.st()
            death.color("blue")
            death.shape("death")
            death.shapesize (1, 1, 14)
            death.fd(5)
        death.ht()

        if aimhi > z and z > aimlo:
            kills = kills + 1
            gun.ht()
            clear()
            # tix.PopupMenu("Target has been Destroyed!")
            break


    ## play again loopback

    replay = textinput("TARGET DESTROYED", "Do you want to play again? (y/n)")
    if replay != "Y" and replay != "y":
        break
    # gun.ht()
    # gun.ht()

write("You have ", True, align="center", font=("Arial", 72, "normal"))
write(kills, True, font=("Arial", 72, "normal"))
write(" Kills", True, font=("Arial", 72, "normal"))
    
    
            


