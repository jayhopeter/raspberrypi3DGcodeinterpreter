import RPi.GPIO as GPIO
import time
from Bipolar_Stepper_Motor_Class_new import Bipolar_Stepper_Motor
from numpy import abs,sqrt,float
<<<<<<< HEAD
=======


def GCD(a,b):#greatest common diviser
    while b:
       a, b = b, a % b
    return a

def LCM(a,b):#least common multipler
    return a * b / GCD(a,b)

def LCMMulti(a,b,c):#least common multipler
    return LCM(LCM(a,b),c)
>>>>>>> refs/remotes/jayhopeter/master

def sign(a): #return the sign of number a
    if a > 0:
        return 1
    elif a < 0:
        return -1
    else:
        return 0

def Single_Motor_Step(stepper, step, speed=50):
#   control stepper motor 1 and 2 simultaneously
#   stepper1 and stepper2 are objects of Bipolar_Stepper_Motor class
#   direction is reflected in the polarity of [step1] or [step2]

    dir1 = sign(step)  #get dirction from the polarity of argument [step]
<<<<<<< HEAD

    step = abs(step)
=======

    step = abs(step)

# [total_micro_step] total number of micro steps
# stepper motor 1 will move one step every [micro_step1] steps
# stepper motor 2 will move one step every [micro_step2] steps
# So [total_mirco_step]=[micro_step1]*[step1] if step1<>0;
# [total_micro_step]=[micro_step2]*[step2] if step2<>0
>>>>>>> refs/remotes/jayhopeter/master

    T = step / speed      #total time
    dt = T / step                #time delay every micro_step
    stepper.move(dir1,step,dt) # don't pass dt here, not working for Z Axis have to figure out why?
    
<<<<<<< HEAD
=======

    T = step / speed      #total time
    dt = T / step                #time delay every micro_step
    stepper.move(dir1,step) # don't pass dt here, not working for Z Axis have to figure out why?
    
>>>>>>> refs/remotes/jayhopeter/master
    return 0
    
def Motor_Step(stepper1, step1, stepper2, step2, speed):
#   control stepper motor 1 and 2 simultaneously
#   stepper1 and stepper2 are objects of Bipolar_Stepper_Motor class
#   direction is reflected in the polarity of [step1] or [step2]

    dir1 = sign(step1)  #get dirction from the polarity of argument [step]
    dir2 = sign(step2)
<<<<<<< HEAD
    
    step1 = abs(step1)
    step2 = abs(step2)
 
    iterator = max(step1, step2)
            
    T = sqrt(step1 ** 2 + step2 ** 2) / speed      #total time
    dt = T / (step1 + step2)                #time delay every micro_step

    #Setup the Ratio Values.
    M1Ratio = float(step1) / float(iterator)
    M2Ratio = float(step2) / float(iterator)
 
    M1Holder = float(0)
    M2Holder = float(0)

    M1ctr = 0
    M2ctr = 0
    
    for i in range(0, iterator):
        M1Holder = float(M1Holder) + float(M1Ratio)
        M2Holder = float(M2Holder) + float(M2Ratio)

        if(M1Holder >= 1):
            M1Holder = float(M1Holder) - 1
            stepper1.move(dir1,1,dt)
            M1ctr = M1ctr + 1

        if(M2Holder >= 1):
            M2Holder = float(M2Holder) - 1
            stepper2.move(dir2,1,dt)
            M2ctr = M2ctr + 1

	#clean-up any missed or over steps...
    if(M1ctr < step1):
            stepper1.move(dir1,1,dt)
    if(M2ctr < step2):
            stepper2.move(dir2,1,dt)
   	#overstep?
    if(M1ctr > step1):
            stepper1.move(dir1 * -1,1,dt)
    if(M2ctr > step2):
            stepper2.move(dir2 * -1,1,dt)
=======

    step1 = abs(step1)
    step2 = abs(step2)

# [total_micro_step] total number of micro steps
# stepper motor 1 will move one step every [micro_step1] steps
# stepper motor 2 will move one step every [micro_step2] steps
# So [total_mirco_step]=[micro_step1]*[step1] if step1<>0;
# [total_micro_step]=[micro_step2]*[step2] if step2<>0

    if step1 == 0:
        total_micro_step = step2
        micro_step2 = 1
        micro_step1 = step2 + 100  #set [micro_step1]>[total_micro_step], so stepper motor will not turn
    elif step2 == 0:
        total_micro_step = step1
        micro_step1 = 1
        micro_step2 = step1 + 100
    else:
        total_micro_step = LCM(step1,step2)
        micro_step1 = total_micro_step / step1
        micro_step2 = total_micro_step / step2
    #debugging
    #print "step1 %d --- step2 %d --- speed %d" % (step1, step2, speed);
    T = sqrt(step1 ** 2 + step2 ** 2) / speed      #total time
    #debugging
                                                 #print str(T);
    dt = T / (step1 + step2)                #time delay every micro_step
    #debugging
                                #print str(dt);
    for i in range(1,total_micro_step + 1):    #i is the iterator for the micro_step.  i cannot start from 0
        #time_laps=0;
        if ((i % micro_step1) == 0):#motor 1 need to turn one step
            stepper1.move(dir1,1,dt)
            #time_laps+=dt/4.0;
            
        if ((i % micro_step2) == 0):#motor 2 need to turn one step
            stepper2.move(dir2,1,dt)
            #time_laps+=dt/4.0;
        
        #time.sleep(dt-time_laps);

>>>>>>> refs/remotes/jayhopeter/master
    return 0

def Motor_StepThree(stepper1, step1, stepper2, step2,stepper3,step3, speed):
#   control stepper motor 1 and 2 simultaneously
#   stepper1 and stepper2 are objects of Bipolar_Stepper_Motor class
#   direction is reflected in the polarity of [step1] or [step2]
    
    dir1 = sign(step1)  #get dirction from the polarity of argument [step]
    dir2 = sign(step2)
    dir3 = sign(step3)
<<<<<<< HEAD
    
    step1 = abs(step1)
    step2 = abs(step2)
    step3 = abs(step3)
    
=======
    
    step1 = abs(step1)
    step2 = abs(step2)
    step3 = abs(step3)
    
>>>>>>> refs/remotes/jayhopeter/master
    iterator = max(step1, step2, step3)
            
    T = sqrt(step1 ** 2 + step2 ** 2) / speed      #total time
    dt = T / (step1 + step2)                #time delay every micro_step

    #Setup the Ratio Values.
    M1Ratio = float(step1) / float(iterator)
    M2Ratio = float(step2) / float(iterator)
    M3Ratio = float(step3) / float(iterator)

    M1Holder = float(0)
    M2Holder = float(0)
    M3Holder = float(0)

    M1ctr = 0
    M2ctr = 0
    M3ctr = 0
    
    for i in range(0, iterator):
        M1Holder = float(M1Holder) + float(M1Ratio)
        M2Holder = float(M2Holder) + float(M2Ratio)
        M3Holder = float(M3Holder) + float(M3Ratio)

        if(M1Holder >= 1):
            M1Holder = float(M1Holder) - 1
            stepper1.move(dir1,1,dt)
            M1ctr = M1ctr + 1

        if(M2Holder >= 1):
            M2Holder = float(M2Holder) - 1
            stepper2.move(dir2,1,dt)
            M2ctr = M2ctr + 1

        if(M3Holder >= 1):
            M3Holder = float(M3Holder) - 1
<<<<<<< HEAD
            stepper3.move(dir3,1)
=======
            stepper3.move(dir3,1,dt)
>>>>>>> refs/remotes/jayhopeter/master
            M3ctr = M3ctr + 1

	#clean-up any missed or over steps...
    if(M1ctr < step1):
            stepper1.move(dir1,1,dt)
    if(M2ctr < step2):
            stepper2.move(dir2,1,dt)
    if(M3ctr < step3):
<<<<<<< HEAD
            stepper3.move(dir3,1)
=======
            stepper3.move(dir3,1,dt)
>>>>>>> refs/remotes/jayhopeter/master
	#overstep?
    if(M1ctr > step1):
            stepper1.move(dir1 * -1,1,dt)
    if(M2ctr > step2):
            stepper2.move(dir2 * -1,1,dt)
    if(M3ctr > step3):
<<<<<<< HEAD
            stepper3.move(dir3 * -1,1)
=======
            stepper3.move(dir3 * -1,1,dt)
>>>>>>> refs/remotes/jayhopeter/master
    return 0
