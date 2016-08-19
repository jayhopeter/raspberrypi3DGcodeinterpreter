import RPi.GPIO as GPIO
import time

#sequence for a1, b2, a2, b1
#phase_seq=[[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]];
#sequence for a, b (not gate/hex inverter) drive
phase_seq=[[1,0],[0,0],[0,1],[1,1]];
#full step sequence. maximum torque
#phase_seq=[[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1]]
#half-step sequence. double resolution. But the torque of the stepper motor is not constant 
num_phase=len(phase_seq);



#to do:  Create seperate class for 2 pin stepper control and 4 pin stepper control
#see http://www.arduino.cc/en/Reference/StepperBipolarCircuit  I use not gate/hex inverter for the 2 pin setup
#We maybe able to do it all with this class using default values in the constructor
#We can also pass another variable to specify full or half steping
#The phase sequence will then be set in the constructor itself 
class Bipolar_Stepper_Motor:
    
    phase=0;
    dirction=0;
    position=0;
    
    a=0;#pin numbers
    b=0;
    enable=0;

    def __init__(self,a,b,enable=0):
    #initial a Bipolar_Stepper_Moter objects by assigning the pins
    
        GPIO.setmode(GPIO.BCM);
        
        self.a=a;
        self.b=b;
        self.enable=enable;
        
        GPIO.setup(self.a,GPIO.OUT);
        GPIO.setup(self.b,GPIO.OUT);
        #GPIO.setup(self.enable,GPIO.IN);
        
        self.phase=0;
        self.dirction=0;        
        self.position=0;
        
    def move(self, dirction, steps, delay=0.009):
        #if(GPIO.gpio_function(self.enable) == GPIO.OUT)
        #    GPIO.setup(self.enable,GPIO.IN);
        if(delay < 0.005):
            delay = 0.005;
            
        for _ in range(steps):
            next_phase=(self.phase+dirction) % num_phase;
            
            GPIO.output(self.a,phase_seq[next_phase][0]);
            GPIO.output(self.b,phase_seq[next_phase][1]);
            
            self.phase=next_phase;
            self.dirction=dirction;
            self.position+=dirction;
            
            time.sleep(delay);

    def unhold(self):
        self.phase=0;
        #GPIO.setup(self.enable, GPIO.OUT, initial=GPIO.LOW);
        
